from flask import Blueprint, flash, render_template, request, url_for, session, redirect, jsonify
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
bp = Blueprint('main', __name__, url_prefix = '/') # bp.route 하면 기본적으로 url주소는 /~으로 시작

@bp.route('/') # 메인 페이지
def home():
    book_list = myBooks.query.all()
    return render_template('main.html', book_list = book_list) # 진자로 책 정보 보내서 책 리스트 페이지를 출력해야 함

@bp.route('/<int:book_id>') # 버튼의 목표 url을 book_id로 지정 (대여하기)
def rent_button(book_id):
    if not session:
        flash("로그인 후 대여할 수 있습니다.")
        return redirect('/')

    book_info = myBooks.query.filter(myBooks.id == book_id).first()
    now_info = nowRenting.query.filter(nowRenting.userID == session['userID'] and nowRenting.book_id == book_id).all()

    if book_info.left >= 1:
        # 재고 수 - 1
        past_left = book_info.left
        book_info.left = past_left - 1
        db.session.commit()

        # 대여기록을 DB에 추가
        rent = rentHistory(userID = session['userID'], book_id = book_info.id, book_name = book_info.book_name, Ldate = datetime.today())
        db.session.add(rent)
        db.session.commit()

        # 책을 도서관에서 빼와서 DB에 옮김
        outside = nowRenting(book_id = book_info.id, book_name = book_info.book_name, userID = session['userID'], Ldate = datetime.today())
        db.session.add(outside)
        db.session.commit()
        return redirect('/')
    else:
        flash("재고가 없습니다. 다른 책을 선택해 주세요.")
        return redirect('/')

@bp.route('/login', methods = ["POST", "GET"]) # 로그인 페이지
def login():
    if request.method == "GET":
        return render_template('login.html', homecoming = True)

    user_ID = request.form['userID']
    user_PW = request.form['userPW']

    user_info = myMember.query.filter(myMember.userID == user_ID).first()
    if not user_info:
        flash("유효하지 않은 아이디입니다.")
        return redirect("/login")
    
    if not check_password_hash(user_info.userPW, user_PW):
        flash("올바른 비밀번호를 입력하십시오.")
        return redirect("/login")
    
    session.clear() # 혹시 모르니 세션을 미리 비워 둠
    session['userID'] = user_ID
    session['username'] = user_info.username
    flash(f"{user_info.username}님 반갑습니다.")
    return redirect("/")

@bp.route('/logout') # 로그아웃
def logout():
    user_name = session['username']
    session.clear()
    return redirect('/')

@bp.route('/submit', methods = ["POST", "GET"]) # 회원가입 페이지
def submit():
    if request.method == "GET":
        return render_template('submit.html', homecoming = True)

    user_ID   = request.form['SuserID']
    user_PW   = request.form['SuserPW']
    user_PW_C = request.form['SuserPW_C']
    user_Name = request.form['Susername']
    
    user_info = myMember.query.filter(myMember.userID == user_ID).first()

    # 아이디 중복 확인
    if user_info:
        flash("중복된 아이디입니다.")
        return redirect("/submit")

    # 비밀번호 확인
    if user_PW != user_PW_C:
        flash("비밀번호를 다시 입력하세요.")
        return redirect("/submit")

    # 패스워드 해시화 (초기데이터를 DB에 넣을 때 해시함수를 거친 뒤 넣어야됨)
    user_pw = generate_password_hash(user_PW)
    submit = myMember(userID = user_ID, userPW = user_pw, username = user_Name)
    db.session.add(submit)
    db.session.commit()

    return redirect('/')

@bp.route('/history', methods = ["GET"]) # 대여기록 페이지
def history():
    if not session:
        flash("로그인 후 이용해 주세요.")
        return redirect('/')

    user_info = myMember.query.filter(myMember.userID == session['userID']).first()
    rent_history = rentHistory.query.filter(rentHistory.userID == session['userID']).all()
    return render_template('history.html', user_info = user_info, rent_history = rent_history, homecoming = True) # 진자로 유저 정보 보내서 유저 정보에 맞는 페이지 출력해야 함

@bp.route('/bannap', methods = ["GET"]) # 책 반납 페이지
def bannap():
    if not session:
        flash("로그인 후 이용해 주세요.")
        return redirect('/')
        
    return render_template('bannap.html', homecoming = True)

@bp.route('/book_intro/<int:book_id>') # 책 소개 페이지 (리뷰 포함)
def intro():
    return render_template('book_intro.html') # 진자로 책 정보 보내서 정보 페이지를 출력해야 함 

@bp.route('/writing/<int:book_id>', methods = ["POST"]) # 리뷰 작성 (책 id를 받아와서 그에 따라 url을 이동)
def writing():
    return redirect(f'/book_intro/{book_id}')

@bp.route('/deleting/<int:book_id>') # 리뷰 삭제 (작성과 마찬가지)
def deleting():    
    return redirect(f'/book_intro/{book_id}')

