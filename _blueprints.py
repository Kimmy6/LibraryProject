from flask import Blueprint, flash, render_template, request, url_for, session, redirect, jsonify
from models import *
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__, url_prefix = '/') # bp.route 하면 기본적으로 url주소는 main/~으로 시작

@bp.route('/') # 메인 페이지
def home():
    book_list = myBooks.query.all()
    return render_template('main.html', book_list = book_list) # 진자로 책 정보 보내서 책 리스트 페이지를 출력해야 함

@bp.route('/login', methods = ["POST", "GET"]) # 로그인 페이지
def login():
    return redirect("/")

@bp.route('/logout') # 로그아웃
def logout():
    user_name = session['username']
    session.clear()
    return redirect('/')

@bp.route('/submit', methods = ["POST", "GET"]) # 회원가입 페이지
def register():
    return redirect('/')

@bp.route('/history', methods = ["GET"]) # 대여기록 페이지
def history():
    return render_template('history.html') # 진자로 유저 정보 보내서 유저 정보에 맞는 페이지 출력해야 함

@bp.route('/bannap', methods = ["POST"]) # 책 반납 페이지
def bannap():
    return render_template('bannap.html') # 진자로 유저 정보 보내서 유저 정보에 맞는 페이지 출력해야 함

@bp.route('/book_intro/<int:book_id>') # 책 소개 페이지 (리뷰 포함)
def intro():
    return render_template('book_intro.html') # 진자로 책 정보 보내서 정보 페이지를 출력해야 함 

@bp.route('/writing/<int:book_id>', methods = ["POST"]) # 리뷰 작성 (책 id를 받아와서 그에 따라 url을 이동)
def writing():
    return redirect(f'/book_intro/{book_id}')

@bp.route('/deleting/<int:book_id>') # 리뷰 삭제 (작성과 마찬가지)
def deleting():    
    return redirect(f'/book_intro/{book_id}')

