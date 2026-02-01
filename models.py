from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150), unique=True, nullable=False)
    company_email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def get_id(self):
        return self.id