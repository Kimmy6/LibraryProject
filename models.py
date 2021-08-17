from db_connect import db
from datetime import datetime
from sqlalchemy_utils import EmailType, URLType

class myMember(db.Model): # 도서관 회원 정보 저장
    __tablename__ = 'myMember'

    userID = db.Column(EmailType, primary_key = True)
    userPW = db.Column(db.String(255), nullable = False) # Issue_NO1 : 조건 추가하는 방법?
    username = db.Column(db.String(20)) # Issue_NO1 영어 / 한글로만

    def __init__(self, userID, userPW, username):
        self.userID   = userID
        self.userPW   = userPW
        self.username = username

class myBooks(db.Model): # 도서관 내 책 정보 저장
    __tablename__ = 'myBooks'

    id                   = db.Column(db.Integer, primary_key = True, nullable = False)
    book_name            = db.Column(db.String(255))
    publisher            = db.Column(db.String(50))
    author               = db.Column(db.String(20))
    publication_date     = db.Column(db.Date)
    pages                = db.Column(db.Integer) 
    isbn                 = db.Column(db.String(13)) 
    description          = db.Column(db.String(511)) 
    link                 = db.Column(URLType)
    left                 = db.Column(db.Integer)
    # cover_pic            = db.Column(db.) Issue_NO2 : 이미지 파일 넣는 방법?

class bookReviews(db.Model): # 책 리뷰 저장
    __tablename__ = 'bookReviews'

    id       = db.Column(db.Integer, primary_key = True)
    book_id  = db.Column(db.Integer, db.ForeignKey('myBooks.id'))
    userID   = db.Column(EmailType, db.ForeignKey('myMember.userID'))
    avgrank  = db.Column(db.Integer)
    comments = db.Column(db.String(511))

class rentHistory(db.Model): # 책 빌린 기록 저장
    __tablename__ = 'rentHistory'

    id          = db.Column(db.Integer, primary_key = True)
    userID    = db.Column(EmailType, db.ForeignKey('myMember.userID'))
    book_id     = db.Column(db.Integer, db.ForeignKey('myBooks.id')) 
    book_name   = db.Column(db.String(255), db.ForeignKey('myBooks.book_name')) 
    Ldate       = db.Column(db.Date)
    Rdate       = db.Column(db.Date)