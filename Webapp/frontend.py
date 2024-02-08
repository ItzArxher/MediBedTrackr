from flask import Blueprint, render_template
import requests

def create_frontendblueprint(db_conn):
    frontend = Blueprint("frontend", __name__)

    mysql = db_conn

    @frontend.route('/', methods=['GET', 'POST'])
    def index():
        return render_template("home.html")
        
    @frontend.route('/bedden', methods=['GET', 'POST'])
    async def bedden():
        curr = mysql.connection.cursor()
        curr.execute("SELECT b.id, a.naam, a.type_zorg, b.is_beschikbaar FROM bed as b INNER JOIN afdeling AS a ON b.afdeling_id = a.id")
        bedden = curr.fetchall()
        print(bedden)
        return render_template("bedden.html", bedden=bedden)

    @frontend.route('/patienten', methods=['GET', 'POST'])
    def patienten():
        return render_template("patienten.html")

    @frontend.route('/afdelingen', methods=['GET', 'POST'])
    def afdelingen():
        return render_template("afdelingen.html")
    
    return frontend