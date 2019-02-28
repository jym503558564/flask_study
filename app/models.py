
#
# #创建表
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(64))
#     password = db.Column(db.String(64))

import config


class Role(config.db.Model):
    __tablename__ = 'roles'
    id = config.db.Column(config.db.Integer, primary_key=True)
    name = config.db.Column(config.db.String(64), unique=True)
    user = config.db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role {}> '.format(self.name)


class User(config.db.Model):
    __tablename__ = 'users'
    id = config.db.Column(config.db.Integer, primary_key=True)
    username = config.db.Column(config.db.String(64), unique=True, index=True)
    role_id = config.db.Column(config.db.Integer, config.db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)


if __name__ == '__main__':
    config.db.drop_all()
    config.db.create_all()

    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)

    config.db.session.add_all(
        [admin_role, mod_role, user_role, user_john, user_susan, user_david])
    # 提交会话到数据库
    config.db.session.commit()





