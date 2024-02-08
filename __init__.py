from flask import Flask, render_template
from dotenv import load_dotenv
from flask_mysqldb import MySQL
import os

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["MYSQL_USER"] = os.environ["MYSQL_USER"]
    app.config["MYSQL_PASSWORD"] = os.environ["MYSQL_PASSWORD"]
    app.config["MYSQL_DB"] = os.environ["MYSQL_DB"]
    app.config["MYSQL_CURSORCLASS"] = "DictCursor"

    mysql = MySQL(app)

    from .frontend import frontend

    app.register_blueprint(frontend, url_prefix='/',)




