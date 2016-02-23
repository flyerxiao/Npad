# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    name = StringField(u'用户名', validators=[
        DataRequired(message=u'请输入6-18位用户名'), Length(6, 18)])
    password = PasswordField(u'密码', validators=[
        DataRequired(message=u'请输入密码')])
    remember = BooleanField(u'记住我')
    submit = SubmitField(u'登陆')
