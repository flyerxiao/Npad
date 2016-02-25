# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# 定义留言表格
class TextForm(Form):
    text = StringField(u'请留下你的想法',
                       validators=[DataRequired(message=u'请留言')])
    submit = SubmitField(u'提交')
