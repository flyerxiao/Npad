#!/usr/bin/python
# -*- coding: utf-8 -*-
# 导入各种库和类
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)
# wtf 强制加密
app.config['SECRET_KEY'] = 'kfasd(&F(8'
# 数据库路径+名字
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# 自动提交数据库变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.debug = True

# 实例化各组件
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
manager = Manager(app)


# 定义留言表格
class MessageForm(Form):
    message = TextAreaField(u'请留下你的想法', validators=[DataRequired()])
    submit = SubmitField(u'提交')


# 定义留言数据模型
class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.UnicodeText)

    def __repr__(self):
        return '<Message %r>' % self.text


# 定义路由
@app.route('/', methods=['GET', 'POST'])
def index():
    # 初始化留言-设为空
    message = None
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
        message = form.message.data
        # 清空留言
        form.message.data = ''
    # 查询留言列表并赋值
    messagelist = Message.query.order_by(Message.id.desc()).all()
    # 定义分页路由
    page = request.args.get('page', 1, type=int)
    # 使用Flask-SQLAlechemy的paginate()方法
    pagination = Message.query.order_by(Message.id.desc()).paginate(
        page, per_page=10, error_out=False)
    # 设置需要分页的项目
    messagelist = pagination.items
    # form和message分别赋值传递到index
    return render_template('index.html', form=form, message=message,
                           messagelist=messagelist, pagination=pagination)


if __name__ == '__main__':
    manager.run()
