from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import  PasswordField
from wtforms.validators import Required
from wtforms.validators import EqualTo

from config import db
from flask import session, flash

# #方式一，提取基类，子类继承====》总感觉降低可读性
# class BaseForm(FlaskForm):
#     username = StringField('用户名', validators=[Required()])
#     password = PasswordField('密码', validators=[Required()])
#     submit = SubmitField('确认，提交')
#
#
# class RegistrationForm(BaseForm):
#     password2 = PasswordField('确认密码', validators=[Required(), EqualTo('password', message='两次输入的密码不一致')])
#
#
# class LoginForm(BaseForm):
#     pass


#方式二
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    password2 = PasswordField('确认密码', validators=[Required(), EqualTo('password', message='两次输入的密码不一致')])
    submit = SubmitField('提交')

    def save(self,username,password):
        try:
            user = User(username=self.username.data, password=self.password.data)
            db.session.add(user)
            flash('注册成功')
            return True
        except:
            flash('账号已存在！')
            return False


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('提交')

    def user_login(self, username, password):
        try:
            user = User.query.filter(username == username).first()
            if not user:
                flash('没有这个用户，请注册')
            else:
                if user.check(password):
                    flash('登录成功！')
        except:
            pass





