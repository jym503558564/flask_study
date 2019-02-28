import os

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
# http://docs.sqlalchemy.org/en/latest/dialects/mysql.html


#数据库配置相关
#连接mysql数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask_blog'

#连接sqlite数据库
# app.config['SQLALCHEMY_DATABASE_URI '] = 'sqlite:///' + os.path.join(basedir,
#                                                           'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

app.debug = True


