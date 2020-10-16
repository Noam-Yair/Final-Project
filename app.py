from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    notify = db.Column(db.Integer, nullable=False)

    searches = db.relationship('Search', backref='user')

# association table


search_item = db.Table('search_item',
                       db.Column("search_id", db.Integer, db.ForeignKey('search.id'), primary_key=True),
                       db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True)
                       )


class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    items = db.relationship('Item', secondary=search_item)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    max_price = db.Column(db.Integer, nullable=False)
