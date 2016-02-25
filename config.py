# -*- coding: utf-8 -*-
# 导入os灵活载入可变配置
import os

basedir = os.path.abspath(os.path.dirname(__name__))

# 创建配置类,设定通用设置
class Config:
    SECRET_KEY = 'Ol[\xe0\xd2rJHp\xe6\x10\xfe'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

# 分别创建3个配置类,分开单独设置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,
                                                           'post-dev.db')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,
                                                            'post-test.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'post-dev.db')

# 配置的字典,默认开发配置
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
