from config import app

from .articles import main as main_blueprint
app.register_blueprint(main_blueprint)



