# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, ' app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#
# CSRF_ENABLED = True
# SECRET_KEY = 'you-will-never-guess'
#
# '''
# 十分简单吧，我们的 Flaks-WTF 扩展只需要两个配置。 CSRF_ENABLED 配置是为了激活 跨站点请求伪造 保护。在大多数情况下，你需要激活该配置使得你的应用程序更安全些。
#
# SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。当你编写自己的应用程序的时候，请务必设置很难被猜测到密钥。
#
# 既然我们有了配置文件，我们需要告诉 Flask 去读取以及使用它。我们可以在 Flask 应用程序对象被创建后去做，方式如下(文件 app/__init__.py):
# '''
#
# OPENID_PROVIDERS = [
#     {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
#     {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
#     {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
#     {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
#     {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
# ]

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
