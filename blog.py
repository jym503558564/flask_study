import os
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField


app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


class NameForm(FlaskForm):
    name = StringField('用户名')
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    # print('form===', form)
    name = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', name=name, form=form)


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
