from sqlalchemy import UniqueConstraint
from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(50))
    image = db.Column(db.String(255))
    description = db.Column(db.Text, nullable=True)
    likes = db.Column(db.Integer, default=0)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    post_Id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'post_Id', name='user_post_unique')
