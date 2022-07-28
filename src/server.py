from flask import Flask, Blueprint, current_app, redirect, request
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import jwt
import config

# main init
app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()
#db 커넥트
db = SQLAlchemy()
migrate = Migrate()
from models import Users
db.init_app(app)
db.create_all()
migrate.init_app(app, db)

import Router
@app.route('/')
def hello():
    return redirect('/home')
    
app.register_blueprint(Router.blueprint)

# @app.route('/')
# def hello():
#     return redirect('/home')

#jwt 세팅
jwt = JWTManager(app)
# flask-login 세팅
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.init_app(app)

# flask_login에서 제공하는 login_required를 실행하기 전 사용자 정보를 조회한다.
@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(id = user_id).first()

# 요청 헤더에서 jwt를 분리해 유효한 jwt인지 검증 로직
@login_manager.request_loader
def load_user_from_request(user_id):
    jwt_headers = request.headers.get('Authorization', '').split()
    if len(jwt_headers) != 2:
        return None
    token = jwt_headers[1]
    data = jwt.decode(token, current_app.config['SECRET_KEY'])
    user = Users.query.filter_by(id = user_id).first()
    if user:
        return user
    
# 로그인이 필요한 서비스에 로그인이 되어있지 않을 때 처리
@login_manager.unauthorized_handler
def unauthorized():
    # 로그인되어 있지 않은 사용자일 경우 첫화면으로 이동
    return Router.errorMessage("인증되지 않은 유저입니다.")

if __name__ == '__main__':
    app.run(
        debug=app.config['FLASK_DEBUG'],
        host=app.config['FLASK_HOST'],
        port=app.config['FLASK_PORT']
    )