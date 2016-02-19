#!/usr/bin/python
# -*- coding: utf-8 -*-
# 导入各种库和类
from flask import Flask, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell

app = Flask(__name__)
# wtf 强制加密
app.config['SECRET_KEY'] = 'kfasd(&F(8'
# 数据库路径+名字
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
# 自动提交数据库变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.debug = True

# 实例化各组件
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
manager = Manager(app)


# 注册实例而导入shell
def make_shell_context():
    return dict(app=app, db=db, Message=Message)


# 为shell命令注册初始化上下文
manager.add_command('shell', Shell(make_context=make_shell_context))


# 定义留言表格
class MessageForm(Form):
    message = StringField(u'请留下你的想法',
                          validators=[DataRequired(message=u'请留言')])
    submit = SubmitField(u'提交')


# 定义留言数据模型
class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return '<Message %r>' % self.text


# 定义路由
@app.route('/')
def index():
    # 查询留言列表并赋值
    messagelist = Message.query.order_by(Message.id.desc()).all()
    # 定义查询字符串,默认渲染第1页
    page = request.args.get('page', 1, type=int)
    # 使用Flask-SQLAlchemy的paginate()方法
    pagination = Message.query.order_by(Message.id.desc()).paginate(
        page, per_page=10, error_out=False)
    # 设置需要分页的项目
    messagelist = pagination.items
    # 传递到变量参数到模版
    return render_template('index.html', messagelist=messagelist,
                           pagination=pagination)


@app.route('/post', methods=['GET', 'POST'])
def add_post():
    # 实例化留言表格
    form = MessageForm()
    # 判断是否成功提交
    if form.validate_on_submit():
        # 查询数据是否有存在相同的留言内容
        message = Message.query.filter_by(text=form.message.data).first()
        # 如果不相同的话,执行下列命令
        if message is None:
            # 实例化数据模型,并取出表格中的值,再赋予message
            message = Message(text=form.message.data)
            # 数据库操作,添加刚输入的内容
            db.session.add(message)
        # 重新赋值用来传递给视图
        session['message'] = form.message.data
        # 清空留言
        form.message.data = ''
        return redirect(url_for('add_post'))

    # 传递到变量参数到模版
    return render_template('post.html', form=form,
                           message=session.get('message'))


if __name__ == '__main__':
    manager.run()
