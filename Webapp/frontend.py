from flask import Blueprint, render_template, request, redirect, url_for

def create_frontendblueprint(db_conn):
    frontend = Blueprint("frontend", __name__)

    mysql = db_conn

    @frontend.route('/', methods=['GET', 'POST'])
    def index():
        return render_template("home.html")

##################################################################################################################################################



# $$$$$$$\                  $$\       $$\                     
# $$  __$$\                 $$ |      $$ |                    
# $$ |  $$ | $$$$$$\   $$$$$$$ | $$$$$$$ | $$$$$$\  $$$$$$$\  
# $$$$$$$\ |$$  __$$\ $$  __$$ |$$  __$$ |$$  __$$\ $$  __$$\ 
# $$  __$$\ $$$$$$$$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ |
# $$ |  $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |
# $$$$$$$  |\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |
# \_______/  \_______| \_______| \_______| \_______|\__|  \__|



        
    @frontend.route('/bedden', methods=['GET', 'POST'])
    def bedden():
        curr = mysql.connection.cursor()
        curr.execute("SELECT a.naam, a.id FROM afdeling as a")
        B_afdeling = curr.fetchall()
        curr.execute("SELECT b.id, a.naam, a.id, b.is_beschikbaar, b.afdeling_id FROM bed as b INNER JOIN afdeling AS a ON b.afdeling_id = a.id")
        bedden = curr.fetchall()
        if request.method == 'POST':
            search = request.form['search']
            status = request.form['status']
            curr.execute("SELECT b.id, a.naam, b.is_beschikbaar FROM bed as b INNER JOIN afdeling AS a ON b.afdeling_id = a.id WHERE (a.naam LIKE %s OR b.id LIKE %s) AND b.is_beschikbaar LIKE %s", ('%' + search + '%', '%' + search + '%', '%' + status + '%'))
            bedden = curr.fetchall()
        print(bedden)
        return render_template("bedden.html", bedden=bedden, B_afdeling=B_afdeling)



    @frontend.route('/delete_bed/<int:id>', methods=['GET', 'POST'])
    def delete_bed(id):
        curr = mysql.connection.cursor()
        curr.execute("DELETE FROM bed WHERE id = %s", (id,))
        mysql.connection.commit()
        return redirect (url_for('frontend.bedden'))

    

    @frontend.route('/edit_bed', methods=['GET', 'POST'])
    def edit_bed():
        if request.method == 'POST':
            ID = request.form['id']
            afdeling = request.form['afdeling']
            status = request.form['status']
            curr = mysql.connection.cursor()
            curr.execute("UPDATE bed SET afdeling_id=%s,is_beschikbaar=%s WHERE id = %s", (afdeling, status, ID))
            mysql.connection.commit()
            return redirect(url_for('frontend.bedden'))
        return redirect(url_for('frontend.bedden'))
    


    @frontend.route('/create_bed', methods=['GET', 'POST'])
    def create_bed():
        if request.method == 'POST':
            afdeling = request.form['afdeling']
            status = request.form['status']
            curr = mysql.connection.cursor()
            curr.execute("INSERT INTO bed (id, afdeling_id, is_beschikbaar) VALUES (NULL, %s, %s)", (afdeling, status,))
            mysql.connection.commit()
            curr.close()
            return redirect(url_for("frontend.bedden"))

##################################################################################################################################################



# $$$$$$$\            $$\     $$\                      $$\                         
# $$  __$$\           $$ |    \__|                     $$ |                        
# $$ |  $$ |$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$$$$$$\  
# $$$$$$$  |\____$$\\_$$  _|  $$ |$$  __$$\ $$  __$$\\_$$  _|  $$  __$$\ $$  __$$\ 
# $$  ____/ $$$$$$$ | $$ |    $$ |$$$$$$$$ |$$ |  $$ | $$ |    $$$$$$$$ |$$ |  $$ |
# $$ |     $$  __$$ | $$ |$$\ $$ |$$   ____|$$ |  $$ | $$ |$$\ $$   ____|$$ |  $$ |
# $$ |     \$$$$$$$ | \$$$$  |$$ |\$$$$$$$\ $$ |  $$ | \$$$$  |\$$$$$$$\ $$ |  $$ |
# \__|      \_______|  \____/ \__| \_______|\__|  \__|  \____/  \_______|\__|  \__|
                                                                                 
                                                                                 
                                                                                 

    @frontend.route('/patienten', methods=['GET', 'POST'])
    def patienten():        
        curr = mysql.connection.cursor()
        curr.execute("SELECT * FROM patient")
        patienten = curr.fetchall()
        if request.method == 'POST':
            search = request.form['search']
            curr.execute("SELECT * FROM patient WHERE voornaam LIKE %s OR achternaam LIKE %s OR telefoon_nr LIKE %s OR id_nr LIKE %s OR geboorte_datum LIKE %s OR geslacht LIKE %s OR id LIKE %s", 
             ('%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%'))
            patienten = curr.fetchall()
        print(patienten)
        return render_template("patienten.html", patienten=patienten)



    @frontend.route('/delete_patient/<int:id>', methods=['GET', 'POST'])
    def delete_patient(id):
        curr = mysql.connection.cursor()
        curr.execute("DELETE FROM patient WHERE id = %s", (id,))
        mysql.connection.commit()
        return redirect (url_for('frontend.patienten'))
    


    @frontend.route('/edit_patient', methods=['GET', 'POST'])
    def edit_patient():
        if request.method == 'POST':
            ID = request.form['id']
            voornaam = request.form['voornaam']
            achternaam = request.form['achternaam']
            telefoon_nr = request.form['telefoon_nr']
            id_nr = request.form['id_nr']
            geboorte_datum = request.form['geboorte_datum']
            geslacht = request.form['geslacht']
            curr = mysql.connection.cursor()
            curr.execute("UPDATE patient SET voornaam=%s,achternaam=%s,telefoon_nr=%s,id_nr=%s,geboorte_datum=%s,geslacht=%s WHERE id = %s", (voornaam, achternaam, telefoon_nr, id_nr, geboorte_datum, geslacht, ID))
            mysql.connection.commit()
            return redirect(url_for('frontend.patienten'))
        return redirect(url_for('frontend.patienten'))
    


    @frontend.route('/create_patient', methods=['GET', 'POST'])
    def create_patient():
        if request.method == 'POST':
            voornaam = request.form['voornaam']
            achternaam = request.form['achternaam']
            telefoon_nr = request.form['telefoon_nr']
            id_nr = request.form['id_nr']
            geboorte_datum = request.form['geboorte_datum']
            geslacht = request.form['geslacht']
            curr = mysql.connection.cursor()
            curr.execute("INSERT into patient (id,voornaam,achternaam,telefoon_nr,id_nr,geboorte_datum,geslacht) VALUES (NULL, %s, %s, %s, %s, %s, %s)", (voornaam, achternaam, telefoon_nr, id_nr, geboorte_datum, geslacht))
            mysql.connection.commit()
            return redirect(url_for('frontend.patienten'))
        return redirect(url_for('frontend.patienten'))

##################################################################################################################################################



#  $$$$$$\   $$$$$$\       $$\           $$\ $$\                                         
# $$  __$$\ $$  __$$\      $$ |          $$ |\__|                                        
# $$ /  $$ |$$ /  \__|$$$$$$$ | $$$$$$\  $$ |$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\  
# $$$$$$$$ |$$$$\    $$  __$$ |$$  __$$\ $$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
# $$  __$$ |$$  _|   $$ /  $$ |$$$$$$$$ |$$ |$$ |$$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ |
# $$ |  $$ |$$ |     $$ |  $$ |$$   ____|$$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |
# $$ |  $$ |$$ |     \$$$$$$$ |\$$$$$$$\ $$ |$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |
# \__|  \__|\__|      \_______| \_______|\__|\__|\__|  \__| \____$$ | \_______|\__|  \__|
#                                                          $$\   $$ |                    
#                                                          \$$$$$$  |                    
#                                                           \______/                     




    @frontend.route('/afdelingen', methods=['GET', 'POST'])
    def afdelingen():
        curr = mysql.connection.cursor()
        curr1 = mysql.connection.cursor()
        curr.execute("SELECT count(*) as count, a.id, a.naam, a.etage, b.id, b.is_beschikbaar FROM afdeling as a INNER JOIN bed as b ON a.id = b.afdeling_id WHERE b.is_beschikbaar=1 GROUP BY a.naam")
        curr1.execute("SELECT COUNT(*) OVER (ORDER BY a.id) AS aantal_bedden, a.naam, (SELECT COUNT(*) FROM bed AS b WHERE b.afdeling_id = a.id AND b.is_beschikbaar = 1) AS beschikbare_beden FROM afdeling AS a INNER JOIN bed AS b ON a.id = b.afdeling_id;")
        afdelingen = curr.fetchall()
        aantalBedden = curr1.fetchall()
        return render_template("afdelingen.html", aantalBedden = aantalBedden, afdelingen=afdelingen)
    


    @frontend.route('/create_afdeling', methods=['GET', 'POST'])
    def create_afdeling():
        if request.method == 'POST':
            naam = request.form['naam']
            etage = request.form['etage']
            curr = mysql.connection.cursor()
            curr.execute("INSERT into afdeling (id,naam,etage) VALUES (NULL, %s, %s)", (naam, etage))
            mysql.connection.commit()
            return redirect(url_for('frontend.afdelingen'))
        
##################################################################################################################################################




#  $$$$$$\                                                                  
# $$  __$$\                                                                 
# $$ /  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$$\ 
# $$ |  $$ |$$  __$$\ $$  __$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$  _____|
# $$ |  $$ |$$ /  $$ |$$ |  $$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |\$$$$$$\  
# $$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____| \____$$\ 
#  $$$$$$  |$$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$$$$$$  |
#  \______/ $$  ____/ \__|  \__| \_______|\__| \__| \__| \_______|\_______/ 
#           $$ |                                                            
#           $$ |                                                            
#           \__|                                                            




    @frontend.route('/opnames', methods=['GET', 'POST'])
    def opnames():
        curr = mysql.connection.cursor()
        curr1 = mysql.connection.cursor()
        curr2 = mysql.connection.cursor()
        curr3 = mysql.connection.cursor()
        curr4 = mysql.connection.cursor()
        curr5 = mysql.connection.cursor()
        curr.execute("SELECT o.id, o.bed_id, o.patient_id, o.opname_datumtijd, o.ontslag_datumtijd, p.id, p.voornaam, p.achternaam, b.id, b.afdeling_id, a.id, a.naam FROM opname as o INNER JOIN patient as p ON p.id = o.patient_id INNER JOIN bed as b ON b.id = o.bed_id INNER JOIN afdeling as a ON a.id = b.afdeling_id;")
        curr1.execute("SELECT * From patient")
        curr2.execute("SELECT * From afdeling")
        curr3.execute("SELECT * From bed")
        curr4.execute("SELECT * From patient where opgenomen = 0")
        curr5.execute("SELECT a.id, a.naam, a.etage, b.id, b.afdeling_id, b.is_beschikbaar From bed as b INNER JOIN afdeling as a ON b.afdeling_id = a.id where is_beschikbaar = 1")
        opnameTable = curr.fetchall()
        PatientenInput = curr4.fetchall()
        PatientenQuery = curr1.fetchall()
        AfdelingQuery = curr2.fetchall()
        BedQuery = curr3.fetchall()
        BedInput = curr5.fetchall()
        return render_template("opnames.html", opnameTable = opnameTable, BedInput = BedInput, PatientenInput = PatientenInput, BedQuery = BedQuery, AfdelingQuery = AfdelingQuery, PatientenQuery = PatientenQuery)
    


    @frontend.route('/create_opname', methods=['GET', 'POST'])
    def create_opname():
        if request.method == 'POST':
            patient = request.form['patient']
            bed_id = request.form['bed_id']
            opname_datumtijd = request.form['opname_datumtijd']
            ontslag_datumtijd = request.form['ontslag_datumtijd']
            curr = mysql.connection.cursor()
            curr1 = mysql.connection.cursor()
            curr2 = mysql.connection.cursor()
            curr1.execute("UPDATE patient SET opgenomen=1 WHERE id = %s", (patient,))
            curr2.execute("UPDATE bed SET is_beschikbaar=0 WHERE id = %s", (bed_id,))
            curr.execute("INSERT into opname (id,bed_id,patient_id,opname_datumtijd,ontslag_datumtijd) VALUES (NULL, %s, %s, %s, %s)", (bed_id, patient, opname_datumtijd, ontslag_datumtijd))
            mysql.connection.commit()
            return redirect(url_for('frontend.opnames'))
    
    return frontend