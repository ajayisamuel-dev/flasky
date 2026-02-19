from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
database_name="database.db"

def create_database(app):
    with app.app_context():
        db.create_all()

    return app

def create_app():
    app=Flask(__name__)
    app.secret_key="watashiwastar"
    app.config["SQLALCHEMY_DATABASE_URI"]=f'sqlite:///{database_name}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    app.permanent_session_lifetime=timedelta(minutes=1)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from models import User, Products

    create_database(app=app)

    return app
