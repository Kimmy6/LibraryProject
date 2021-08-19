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
    
    user_info = myMember.query.filter(myMember.userID == session['userID']).first()
    user_book = nowRenting.query.filter(nowRenting.userID == session['userID']).all()
    history = rentHistory.query.filter(rentHistory.userID == session['userID']).all()
    
    return render_template('bannap.html', user_book = user_book , user_info = user_info, history = history, homecoming = True)

@bp.route('/bannap/<int:book_id>') # 버튼의 목표 url을 bannap/book_id로 지정 (반납하기)
def bannap_button(book_id):

    now_info = nowRenting.query.filter(nowRenting.book_id == book_id).first()
    book_info = myBooks.query.filter(myBooks.id == book_id).first()

    # 재고 수 + 1
    _left = book_info.left
    book_info.left = _left + 1
    db.session.commit()

    # 대여 기록 남기기
    rent = rentHistory.query.filter(rentHistory.book_id == book_id).first()
    db.session.add(rent)
    db.session.commit()

    # 책을 다시 도서관에 반납
    db.session.delete(now_info)
    db.session.commit()

    flash(f"요청하신 {now_info.book_name}의 반납이 완료되었습니다.")
    return redirect(url_for('main.bannap'))

@bp.route('/book_intro/<int:book_id>', methods = ["POST", "GET"]) # 책 소개 및 리뷰 작성 페이지
def intro(book_id):
    if request.method == "GET":
        book_info = myBooks.query.filter(myBooks.id == book_id).first()
        user_comments = bookReviews.query.filter(bookReviews.book_id == book_id).all()
        return render_template('book_intro.html', book_info = book_info, user_comments = user_comments, homecoming = True) # 진자로 책 정보 보내서 정보 페이지를 출력해야 함 

    comments = request.form['writingComments']
    rank = int(request.form['bookRank'])

    book_info = myBooks.query.filter(myBooks.id == book_id).first()
    user_comments = bookReviews.query.filter(bookReviews.book_id == book_id).all()
    
    # 댓글과 점수 추가
    written_comments = bookReviews(userID = session['userID'], username = session['username'], book_id = book_id, rank = rank, comments = comments)
    db.session.add(written_comments)
    db.session.commit()

    # 평점을 갱신하는 코드(추가)
    if user_comments:
        hap = 0
        for i in range(0, len(user_comments)):
            hap += int(user_comments[i].rank)

        new_avg_rank = (rank + hap) / (len(user_comments) + 1)
        book_info.avg_rank = new_avg_rank
        db.session.commit()

    else:
        book_info.avg_rank = rank
        db.session.commit()
        
    return redirect(f'/book_intro/{book_id}')


@bp.route('/deleting/<int:book_id>/<int:comment_id>') # 리뷰 삭제 (작성과 마찬가지)
def deleting(book_id, comment_id):
    if session:
        user_comments = bookReviews.query.filter(bookReviews.id == comment_id).first()
        book_info = myBooks.query.filter(myBooks.id == book_id).first()
        _user_comments = bookReviews.query.filter(bookReviews.book_id == book_id).all()
        if user_comments.userID != session['userID']:
            flash("내 댓글만 삭제할 수 있습니다.")
        else:
            # 댓글과 점수 삭제
            db.session.delete(user_comments)
            db.session.commit()

        # 평점을 갱신하는 코드(삭제)
        if _user_comments:
            rank = int(user_comments.rank)
            hap = 0
            for i in range(0, len(_user_comments)):
                hap += int(_user_comments[i].rank)
            if len(_user_comments) > 1:
                new_avg_rank = (hap - rank) / (len(_user_comments) - 1)
                book_info.avg_rank = new_avg_rank
                db.session.commit()
            else:
                book_info.avg_rank = 0
                db.session.commit()
    else:
        flash("로그인 후 댓글을 삭제할 수 있습니다.")

    return redirect(f'/book_intro/{book_id}')
    