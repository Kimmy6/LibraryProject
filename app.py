from flask import Flask
from db_connect import db
import os
import _blueprints
from secret import secret

def create_app():
    app = Flask(__name__)
    BASE_DIR = os.path.dirname(__file__) # 폴더 구조가 달라져도 현재 폴더를 가져와서 사용 가능토록 설정

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'MyLibrary.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = secret

    db.init_app(app) # db와 app 연결
    app.register_blueprint(_blueprints.bp) # 블루프린트 가져오기

    return app

if __name__ == "__main__":
    create_app().run(debug = True, port = 5000)