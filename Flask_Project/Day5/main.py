from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''sno, name, phone_num, msg, date, email'''
    sno = db.Column(db.Integer, Primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    phone_num = db.Column(db.Integer(12), nullable = False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable =False)
    email = db.Column(db.String(20), nullable=False)
    