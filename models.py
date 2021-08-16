from db_connect import db
from datetime import datetime
from sqlalchemy_utils import EmailType, URLType
import arrow
class myMember(db.Model): # 도서관 회원 정보 저장
    __tablename__ = 'myMember'

    id     = db.Column(db.String(30), primary_key = True, nullable = False)
    userID = db.Column(EmailType)
    userPW = db.Column(db.String(255), nullable = False) # Issue_NO1 : 조건 추가하는 방법?
    username = db.Column(db.String(20)) # Issue_NO1 영어 / 한글로만

    def __init__(self, userID, userPW, username):
        self.userID   = userID
        self.userPW   = userPW
        self.username = username

class myBooks(db.Model): # 도서관 내 책 정보 저장
    __tablename__ = 'myBooks'

    id                   = db.Column(db.String(30), primary_key = True, nullable = False)
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

    def __init__(self, book_name, publisher, author, publication_date, pages, isbn, description, link, left):
        self.book_name        = book_name
        self.publisher        = publisher
        self.author           = author
        self.publication_date = publication_date 
        self.pages            = pages
        self.isbn             = isbn
        self.description      = description
        self.link             = link
        self.left             = left

class bookReviews(db.Model): # 책 리뷰 저장
    __tablename__ = 'bookReviews'

    id     = db.Column(db.String(30), primary_key = True, nullable = False)
    username = db.Column(db.String(20))
    avgrank  = db.Column(db.Integer)
    comments = db.Column(db.String(511))

    def __init__(self, username, avgrank, comments):
        self.username = username
        self.rank     = rank
        self.comments = comments
