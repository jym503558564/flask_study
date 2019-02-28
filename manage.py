from flask_script import Manager
from config import app

manager = Manager(app)

from app.articles import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/articles')

from app.admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint)


if __name__ == '__main__':
    manager.run()