import os
from flask import Flask, redirect, url_for, session, flash, render_template

from flask_script import Manager

from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Required

from flask_sqlalchemy import SQLAlchemy


# 我们要把数据库放在当下的文件夹,这个basedir就是当下文件夹的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
db = SQLAlchemy(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#创建表
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))


#验证表单
class NameForm(FlaskForm):
    name = StringField('用户名', validators=[Required()])
    password = StringField('密码')
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = NameForm()
    print('form===', form)
    name = None

    if form.validate_on_submit():
        # print('form2===', form)
        # print('form.name==', form.name)
        # name = form.name.data
        # print('form.name.data==', form.name.data)
        # form.name.data = ''
        #============================================
        # old_name = session.get('name', None)
        # if old_name is not None and old_name != form.name.data:
        #     flash('您更改了名字')
        #
        # session['name'] = form.name.data
        #============================================
        user =User.query.get(name=form.name.data, password=form.password.data)
        if user is None:
            user = User(name=form.name.data, password=form.password.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('login.html', name=session.get('name', None), form=form)


@app.route('/index')
def index():
    name = session.get('name', None)
    return render_template('index.html', name=name)


@app.route('/<username>')
def user(username):
    return render_template('user.html', name=username)


# @app.route('/login')
# def login():
#     return '登录页面'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
