from flask import Blueprint, render_template
import time

def create_backendblueprint(db_conn):
    backend = Blueprint("backend", __name__)

    mysql = db_conn

    @backend.route('/test', methods=['GET'])
    def test():
        return "TEST DATA"
        

    
    return backend