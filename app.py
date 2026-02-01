from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import config

db = SQLAlchemy() 


def create_app(): 
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return redirect(url_for('signup'))


    bcrypt = Bcrypt(app)
    from routes import register_routes
    register_routes(app, db, bcrypt)
    migrate = Migrate(app, db)  

    return app
