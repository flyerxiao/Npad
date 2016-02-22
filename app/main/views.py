# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, request, session, redirect, url_for

from . import main
from .forms import TextForm
from .. import db
from ..models import Message


@main.route('/')
def index():
    # 查询留言列表并赋值
    messagelist = Message.query.order_by(Message.id).all()
    # 定义查询字符串,默认渲染第1页
    page = request.args.get('page', 1, type=int)
    # 使用Flask-SQLAlchemy的paginate()方法
    pagination = Message.query.order_by(Message.id).paginate(
        page, per_page=10, error_out=False)
    # 设置需要分页的项目
    messagelist = pagination.items
    # 传递到变量参数到模版
    return render_template('index.html', messagelist=messagelist,
                           pagination=pagination)


@main.route('/post/', methods=['GET', 'POST'])
def post():
    # 实例化留言表格
    form = TextForm()
    # 判断是否成功提交
    if form.validate_on_submit():
        # 查询数据是否有存在相同的留言内容
        text = Message.query.filter_by(text=form.text.data).first()
        # 如果不相同的话,执行下列命令
        if text is None:
            # 实例化数据模型,并取出表格中的值,再赋予message
            newtext = Message(text=form.text.data)
            # 数据库操作,添加刚输入的内容
            db.session.add(newtext)
        # 重新赋值用来传递给视图
        session['text'] = form.text.data
        return redirect(url_for('.post'))
    # 传递到变量参数到模版
    return render_template('post.html', form=form,
                          text=session.get('text'))
