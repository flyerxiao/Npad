#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from app import create_app, db
from app.models import Message, User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


# 注册实例而导入shell
def make_shell_context():
    return dict(app=app, db=db, Message=Message, User=User)


# 为shell命令注册初始化上下文
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# shell加入单元测试
@manager.command
def test():
    """Run the unit test"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
