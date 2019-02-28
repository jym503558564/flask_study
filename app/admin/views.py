from flask import redirect, flash
from flask import url_for
from flask import render_template


from . import admin
from config import db
from ..models import User
from .forms import LoginForm, RegistrationForm


from flask_login import login_user, logout_user
from flask_login import current_user,login_required


@admin.route('/')
def index():
    print('current_user.is_authenticated====', current_user.is_authenticated)

    if not current_user.is_authenticated:
        return redirect(url_for('admin.login'))
    return render_template('index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user is not None:
            if user.check(form.password.data):
                login_user(user)
                return redirect(url_for('admin.index'))
            else:
                flash('密码错误！')
                return redirect(url_for('admin.login'))
        else:
            flash('没有这个用户，请重新注册')
    return render_template('admin/login.html', form=form)


@admin.route('/logout')
def logout():
    logout_user()
    flash('退出登录！')
    return redirect(url_for('admin.login'))


@admin.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data, password=form.password.data)
            db.session.add(user)
            flash('注册成功！')
            return redirect(url_for('admin.index'))
        except:
            flash('账号已经存在！')
            return redirect(url_for('admin.register'))
    return render_template('admin/register.html', form=form)


