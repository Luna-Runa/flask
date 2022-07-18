from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask import Blueprint

import config

api = Api(
        version='1.0',
        title='flask 과제 API 문서',
        description='Swagger 문서',
)
#db 커넥트
db = SQLAlchemy()
migrate = Migrate()

blueprint = Blueprint('api', __name__, url_prefix='/')

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    #DB, ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    #db.create_all()

    #Router 블루프린트, Swagger 세팅
    from .routes.mainRouter import main
    from .routes.authRouter import auth
    api.init_app(app)
    api.add_namespace(main)
    api.add_namespace(auth)
    app.register_blueprint(blueprint)

    if __name__ == '__main__':
        app.run(debug=True)

    return app
