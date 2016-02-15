#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'kfasd(&F(8'


class MessageForm(Form):
    message = TextAreaField(u'请留下你的想法', validators=[DataRequired()])
    submit = SubmitField(u'提交')


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
