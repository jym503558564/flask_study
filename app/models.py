from config import db, login_manager
from flask_login import UserMixin


#创建用户表
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return 'users表: id为:{}, name为:{}'.format(self.id, self.name)

    def check(self, password):
        return password == self.password


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#创建文章表
class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256))
    content = db.Column(db.Text)# 关联表，这里要与相关联的表的类型一直, user.id 表示关联到user表下的id字段

    # author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 给这个article模型添加一个author属性（关系表），User为要连接的表，backref为定义反向引用
    # author = db.relationship('User', backref=db.backref('articles'), lazy='dynamic')









if __name__ == '__main__':
    db.drop_all()
    db.create_all()

