from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from .frontend import create_frontendblueprint
from .backend import create_backendblueprint
import os

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["MYSQL_USER"] = os.environ["MYSQL_USER"]
    app.config["MYSQL_PASSWORD"] = os.environ["MYSQL_PASSWORD"]
    app.config["MYSQL_DB"] = os.environ["MYSQL_DB"]
    app.config["MYSQL_CURSORCLASS"] = "DictCursor"

    mysql = MySQL(app)

    frontend = create_frontendblueprint(mysql)
    backend = create_backendblueprint(mysql)

    app.register_blueprint(frontend, url_prefix='/',)
    app.register_blueprint(backend, url_prefix='/backend/',)

    return app


