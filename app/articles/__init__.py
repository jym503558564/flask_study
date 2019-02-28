#创建蓝本
from flask import Blueprint

main = Blueprint('articles', __name__)
from . import views, error