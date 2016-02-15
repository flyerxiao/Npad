#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kfasd(&F(8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class MessageForm(Form):
    message = TextAreaField(u'请留下你的想法', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText)

    def __repr__(self):
        return '<Message %r>' % self.name


@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    form = MessageForm()
    if form.validate_on_submit():
        message = form.message.data
        form.message.data = ''
    return render_template('index.html', form=form, message=message)


if __name__ == '__main__':
    app.run(debug=True)
