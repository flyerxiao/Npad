# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms.validators import ValidationError
from ..models import User


class LoginForm(Form):
    name = StringField(u'用户名', validators=[
        DataRequired(message=u'请输入6-18位用户名'), Length(6, 18)])
    password = PasswordField(u'密码', validators=[
        DataRequired(message=u'请输入密码')])
    remember = BooleanField(u'记住我')
    submit = SubmitField(u'登陆')


class RegisterForm(Form):
    name = StringField(u'用户名', validators=[
        DataRequired(message=u'用户名必须为6-18位大小写字母,数字'), Length(6, 18),
        Regexp('^[A-Za-z0-9]*$', 0, u'用户名必须为6-18位大小写字母,数字')])
    password = PasswordField(u'密码', validators=[
        DataRequired(message=u'请输入8-20位密码'), Length(8, 20)])
    password2 = PasswordField(u'确认密码', validators=[
        DataRequired(message=u'请重复输入密码'),
        EqualTo('password', message=u'密码必须相同')])
    submit = SubmitField(u'注册')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError(u'用户名已经存在')
