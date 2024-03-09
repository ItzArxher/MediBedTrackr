from flask import Blueprint, render_template, request, redirect, url_for

def create_frontendblueprint(db_conn):
    frontend = Blueprint("frontend", __name__)

    mysql = db_conn

    @frontend.route('/', methods=['GET', 'POST'])
    def index():
        return redirect(url_for("frontend.bedden"))


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
        curr.execute("SELECT b.id, a.naam, a.id, b.is_beschikbaar, b.afdeling_id FROM bed as b INNER JOIN afdeling AS a ON b.afdeling_id = a.id ORDER BY b.id")
        bedden = curr.fetchall()
        if request.method == 'POST':
            search = request.form['search']
            status = request.form['status']
            if status == "":
                curr.execute("SELECT b.id, a.naam, a.id, b.is_beschikbaar, b.afdeling_id FROM bed as b INNER JOIN afdeling AS a ON b.afdeling_id = a.id WHERE (a.naam LIKE %s OR b.id LIKE %s) ORDER BY b.id", ('%' + search + '%', '%' + search + '%',))
            else:
                curr.execute("SELECT b.id, a.naam, a.id, b.is_beschikbaar, b.afdeling_id FROM bed as b INNER JOIN afdeling AS a ON b.afdeling_id = a.id WHERE (a.naam LIKE %s OR b.id LIKE %s) AND b.is_beschikbaar=%s ORDER BY b.id", ('%' + search + '%', '%' + search + '%',status))
            bedden = curr.fetchall()
        print(bedden)
        return render_template("bedden.html", bedden=bedden, B_afdeling=B_afdeling)



    @frontend.route('/delete_bed/<int:id>', methods=['GET', 'POST'])
    def delete_bed(id):
        curr = mysql.connection.cursor()
        curr.execute("DELETE FROM bed WHERE id = %s", (id,))
        mysql.connection.commit()
        return redirect(url_for("frontend.bedden"))

    

    @frontend.route('/edit_bed', methods=['GET', 'POST'])
    def edit_bed():
        if request.method == 'POST':
            ID = request.form['id']
            afdeling = request.form['afdeling']
            status = request.form['status']
            print(ID)
            print(afdeling)
            print(status)
            curr = mysql.connection.cursor()
            curr.execute("UPDATE bed SET afdeling_id=%s,is_beschikbaar=%s WHERE id = %s", (afdeling, status, ID))
            mysql.connection.commit()
            return redirect(url_for('frontend.bedden'))
        return redirect(url_for('frontend.bedden'))
    


    @frontend.route('/create_bed', methods=['GET', 'POST'])
    def create_bed():
        if request.method == 'POST':
            afdeling = request.form['afdeling']
            aantal_bedden = int(request.form['aantal_bedden'])
            curr = mysql.connection.cursor()
            for i in range(aantal_bedden):
                curr.execute("INSERT INTO bed (afdeling_id, is_beschikbaar) VALUES (%s, 1)", (afdeling,))
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
            curr.execute("INSERT into patient (voornaam,achternaam,telefoon_nr,id_nr,geboorte_datum,geslacht) VALUES (%s, %s, %s, %s, %s, %s)", (voornaam, achternaam, telefoon_nr, id_nr, geboorte_datum, geslacht))
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
        curr1.execute("SELECT a.id, a.naam, a.etage, COUNT(b.id) AS beschikbare_bedden  FROM afdeling AS a LEFT JOIN bed AS b ON a.id = b.afdeling_id GROUP BY a.naam ORDER BY a.id")
        
        aantalBedden = curr1.fetchall()
        afdelingen = curr.fetchall()
        if request.method == 'POST':
            search = request.form['search']
            print("Search is")
            print(search)
            curr1.execute("SELECT a.id, a.naam, a.etage, COUNT(b.id) AS beschikbare_bedden  FROM afdeling AS a LEFT JOIN bed AS b ON a.id = b.afdeling_id  WHERE a.naam LIKE %s GROUP BY a.naam ORDER BY a.id", ('%' + search + '%',))
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
        

        
        
    @frontend.route('/edit_afdeling', methods=['GET', 'POST'])
    def edit_afdeling():
        if request.method == 'POST':
            ID = request.form['id']
            afdeling_naam = request.form['afdeling_naam']
            etage = request.form['etage']
            curr = mysql.connection.cursor()
            curr.execute("UPDATE afdeling SET naam=%s,etage=%s WHERE id = %s", (afdeling_naam, etage, ID))
            mysql.connection.commit()
            return redirect(url_for('frontend.afdelingen'))
        return redirect(url_for('frontend.afdelingen'))   

    @frontend.route('/delete_afdeling/<int:id>', methods=['GET', 'POST'])
    def delete_afdeling(id):
        curr = mysql.connection.cursor()
        curr.execute("DELETE FROM afdeling WHERE id = %s", (id,))
        mysql.connection.commit()
        return redirect (url_for('frontend.afdelingen'))
 
        
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
        curr.execute("SELECT o.id, o.bed_id, o.patient_id, o.opname_datumtijd, o.ontslag_datumtijd, p.id, p.voornaam, p.achternaam, b.id, b.afdeling_id, a.id, a.naam FROM opname as o INNER JOIN patient as p ON p.id = o.patient_id INNER JOIN bed as b ON b.id = o.bed_id INNER JOIN afdeling as a ON a.id = b.afdeling_id ORDER BY o.id DESC")
        curr1.execute("SELECT * From patient")
        curr2.execute("SELECT * From afdeling")
        curr3.execute("SELECT b.id, b.afdeling_id, b.is_beschikbaar, a.naam From bed AS b INNER JOIN afdeling AS a ON b.afdeling_id=a.id WHERE b.is_beschikbaar=1")
        curr4.execute("SELECT * From patient WHERE is_opgenomen=0")
        curr5.execute("SELECT a.id, a.naam, a.etage, b.id, b.afdeling_id, b.is_beschikbaar From bed as b INNER JOIN afdeling as a ON b.afdeling_id = a.id where is_beschikbaar = 1 ORDER BY a.naam ASC")
        opnameTable = curr.fetchall()
        PatientenInput = curr4.fetchall()
        
        PatientenQuery = curr1.fetchall()
        AfdelingQuery = curr2.fetchall()
        BedQuery = curr3.fetchall()
        BedInput = curr5.fetchall()
        if request.method == 'POST':
            search = request.form['search']
            print("Search is")
            print(search)
            curr.execute("SELECT o.id, o.bed_id, o.patient_id, o.opname_datumtijd, o.ontslag_datumtijd, p.id, p.voornaam, p.achternaam, b.id, b.afdeling_id, a.id, a.naam FROM opname as o INNER JOIN patient as p ON p.id = o.patient_id INNER JOIN bed as b ON b.id = o.bed_id INNER JOIN afdeling as a ON a.id = b.afdeling_id WHERE p.voornaam LIKE %s or p.achternaam LIKE %s or CONCAT(p.voornaam, ' ' ,p.achternaam) LIKE %s OR a.naam LIKE %s ORDER BY o.id DESC ", ('%' + search + '%','%' + search + '%','%' + search + '%','%' + search + '%'))
            opnameTable = curr.fetchall()
        return render_template("opnames.html", opnameTable = opnameTable, BedInput = BedInput, PatientenInput = PatientenInput, BedQuery = BedQuery, AfdelingQuery = AfdelingQuery, PatientenQuery = PatientenQuery)
    


    @frontend.route('/create_opname', methods=['GET', 'POST'])
    def create_opname():
        if request.method == 'POST':
            patient = request.form['patient']
            bed_id = request.form['bed_id']
            opname_datumtijd = request.form['opname_datumtijd']
            curr = mysql.connection.cursor()
            curr1 = mysql.connection.cursor()
            curr2 = mysql.connection.cursor()
            curr1.execute("UPDATE patient SET is_opgenomen=1 WHERE id = %s", (patient,))
            curr2.execute("UPDATE bed SET is_beschikbaar=0 WHERE id = %s", (bed_id,))
            curr.execute("INSERT into opname (id,bed_id,patient_id,opname_datumtijd,ontslag_datumtijd) VALUES (NULL, %s, %s, %s, %s)", (bed_id, patient, opname_datumtijd, None))
            mysql.connection.commit()
            return redirect(url_for('frontend.opnames'))
    
    @frontend.route('/delete_opname/<int:id>', methods=['GET', 'POST'])
    def delete_opname(id):
        curr = mysql.connection.cursor()
        curr.execute("SELECT patient_id, bed_id FROM opname WHERE id=%s", (id,))
        data = curr.fetchone()
        bed_id = data["bed_id"]
        patient_id = data["patient_id"]
        print("BED ID")
        print(bed_id)
        curr.execute("DELETE FROM opname WHERE id = %s", (id,))
        curr.execute("UPDATE patient SET is_opgenomen=0 WHERE id=%s", (patient_id,))
        curr.execute("UPDATE bed SET is_beschikbaar=1 WHERE id=%s", (bed_id,))
        mysql.connection.commit()
        return redirect (url_for('frontend.opnames'))
    
    @frontend.route('/ontslaan_opname', methods=['POST'])
    def ontslaan_opname():
        id = request.form['id']
        bed_id = request.form['bed_id']
        ontslag_datumtijd = request.form['ontslag_datumtijd']
        curr = mysql.connection.cursor()
        curr.execute("UPDATE opname SET ontslag_datumtijd = %s WHERE id = %s", (ontslag_datumtijd,id))
        curr.execute("UPDATE bed SET is_beschikbaar = 1 WHERE id = %s", (bed_id,))
        mysql.connection.commit()
        return redirect (url_for('frontend.opnames'))
    
    @frontend.route('/edit_opname', methods=['POST'])
    def edit_opname():
        if request.method == 'POST':
            id = request.form['id']
            oudeBed_id = request.form['oudeBed_id']
            oudePatient_id = request.form['oudePatient_id']
            patient_id = request.form['patient']
            bed_id = request.form['bed_id']
            opname_datumtijd = request.form['opname_datumtijd']
            ontslag_datumtijd = request.form.get('ontslag_datumtijd') or None
            curr = mysql.connection.cursor()
            curr.execute("UPDATE opname SET patient_id=%s,bed_id=%s,opname_datumtijd=%s,ontslag_datumtijd=%s WHERE id = %s", (patient_id, bed_id, opname_datumtijd, ontslag_datumtijd, id))
            if oudeBed_id != bed_id:
                curr.execute("UPDATE bed SET is_beschikbaar=1 WHERE id=%s", (oudeBed_id,))
                curr.execute("UPDATE bed SET is_beschikbaar=0 WHERE id=%s", (bed_id,))
            if oudePatient_id != patient_id:
                curr.execute("UPDATE patient SET is_opgenomen=0 WHERE id=%s", (oudePatient_id,))
                curr.execute("UPDATE patient SET is_opgenomen=1 WHERE id=%s", (patient_id,))

            mysql.connection.commit()
            return redirect(url_for('frontend.opnames'))
        return redirect(url_for('frontend.opnames'))   

    
    return frontend