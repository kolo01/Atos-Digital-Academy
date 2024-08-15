import mysql.connector
class Connection:
     
    def creer_base_de_donnees():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        try:
        
            if conn.is_connected():
                cursor = conn.cursor()

                # cursor.execute("CREATE DATABASE IF NOT EXISTS etab_db")

                cursor.execute("USE etab_db")

                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Utilisateurs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    pseudo VARCHAR(50) NOT NULL,
                    motDePasse VARCHAR(50) NOT NULL,
                    dateCreation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """)
                # cursor.execute("""
                # INSERT INTO Utilisateurs (pseudo, motDePasse) VALUES ('admin', 'admin')
                # """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Professeur (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    dateNaissance DATE NOT NULL,
                    ville VARCHAR(50) NOT NULL,
                    prenom VARCHAR(50) NOT NULL,
                    nom VARCHAR(50) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    vacant BOOLEAN NOT NULL,
                    telephone VARCHAR(15) NOT NULL,
                    matiereEnseigne VARCHAR(100),
                    prochainCours VARCHAR(100),
                    sujetProchaineReunion VARCHAR(100)
                )
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Eleve (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    classe VARCHAR(50),
                    matricule VARCHAR(50) UNIQUE,
                    dateNaissance DATE NOT NULL,
                    ville VARCHAR(100) NOT NULL,
                    prenom VARCHAR(50) NOT NULL,
                    nom VARCHAR(50) NOT NULL,
                    telephone VARCHAR(15) NOT NULL
                )
                """)
                conn.commit()
                cursor.close()
                conn.close()
                # print('Base de donnée crée avec succés')
                return True
            
        except Exception as e:
                print("Base de donnée inexistante :: Tentative de creation")
                cursor = conn.cursor()

                cursor.execute("CREATE DATABASE IF NOT EXISTS etab_db")

                cursor.execute("USE etab_db")

                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Utilisateurs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    pseudo VARCHAR(50) NOT NULL,
                    motDePasse VARCHAR(50) NOT NULL,
                    dateCreation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """)
                cursor.execute("""
                INSERT INTO Utilisateurs (pseudo, motDePasse) VALUES ('admin', 'admin')
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Professeur (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    dateNaissance DATE NOT NULL,
                    ville VARCHAR(50) NOT NULL,
                    prenom VARCHAR(50) NOT NULL,
                    nom VARCHAR(50) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    vacant BOOLEAN NOT NULL,
                    telephone VARCHAR(15) NOT NULL,
                    matiereEnseigne VARCHAR(100),
                    prochainCours VARCHAR(100),
                    sujetProchaineReunion VARCHAR(100)
                )
                """)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Eleve (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    classe VARCHAR(50),
                    matricule VARCHAR(50) UNIQUE,
                    dateNaissance DATE NOT NULL,
                    ville VARCHAR(100) NOT NULL,
                    prenom VARCHAR(50) NOT NULL,
                    nom VARCHAR(50) NOT NULL,
                    telephone VARCHAR(15) NOT NULL
                )
                """)
                conn.commit()
                cursor.close()
                conn.close()
                print('Base de donnée crée avec succés')
                return True

    #Fonction d'ajout des utilisateurs
    def AjouterEleve(classe,matricule,dateNaissance,ville,prenom,nom,telephone):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        request = ("INSERT INTO Eleve (classe,matricule,dateNaissance,ville,prenom,nom,telephone) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    
        val = (classe,matricule,dateNaissance,ville,prenom,nom,telephone)
        cursor.execute(request,val)
        conn.commit()
        cursor.close()
        conn.close()
        


    def AjouterProfesseur(dateNaissance,ville,prenom,nom,email,vacant,telephone,matiereEnseigne,prochainCours,sujetProchaineReunion):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        request = ("INSERT INTO Professeur (dateNaissance,ville,prenom,nom,email,vacant,telephone,matiereEnseigne,prochainCours,sujetProchaineReunion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        val = (dateNaissance,ville,prenom,nom,email,vacant,telephone,matiereEnseigne,prochainCours,sujetProchaineReunion)
        cursor.execute(request,val)
        conn.commit()
        cursor.close()
        conn.close()

    def AjouterUtilisateurs(identifiant, motDePasse):
        val = (identifiant,motDePasse)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        request = ("SELECT * FROM Utilisateurs WHERE pseudo=%s AND motDePasse=%s ")
        cursor.execute(request,val)
        
        verificationId = cursor.fetchone()
        if verificationId is None:
        
            request = ("INSERT INTO Utilisateurs (pseudo,motDePasse) VALUES (%s, %s)")
            cursor.execute(request,val)
            conn.commit()
            cursor.close()
            conn.close()
            print( "Utilisateur enregistré")
        else:
            print( "Identifiant déjà existant")


    #Fonction de modification de users
    def editUser(identifiant,NewPassword):
        try:
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=""
                )
            cursor = conn.cursor()
            cursor.execute("USE etab_db")
            request = ("UPDATE Utilisateurs SET motDePasse=%s WHERE pseudo=%s")
            val = (NewPassword, identifiant)
            cursor.execute(request, val)
            conn.commit()
            cursor.close()
            conn.close()
            print("Succes")
        except:
            print("Erreur lors de la modification")

    def editEleve(id):
        pass

    def editProfesseur(id,dateNaissance=None,ville=None,prenom=None,nom=None,email=None,vacant=None,telephone=None,matiereEnseigne=None,prochainCours=None,sujetProchaineReunion=None):
        exist = True
        if exist :
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = conn.cursor()
            cursor.execute("USE etab_db")
            if dateNaissance is not None:
                request = ("UPDATE Professeur SET dateNaissance=%s WHERE id=%s")
                val = (dateNaissance, id)
                cursor.execute(request, val)
            if ville is not None:
                request = ("UPDATE Professeur SET ville=%s WHERE id=%s")
                val = (ville, id)
                cursor.execute(request, val)
            if prenom is not None:
                request = ("UPDATE Professeur SET prenom=%s WHERE id=%s")
                val = (prenom, id)
                cursor.execute(request, val)
            if nom is not None:
                request = ("UPDATE Professeur SET nom=%s WHERE id=%s")
                val = (nom, id)
                cursor.execute(request, val)
            if email is not None:
                request = ("UPDATE Professeur SET email=%s WHERE id=%s")
                val = (email, id)
                cursor.execute(request, val)
            if vacant is not None:
                request = ("UPDATE Professeur SET vacant=%s WHERE id=%s")
                val = (vacant, id)
                cursor.execute(request, val)
            if telephone is not None:
                request = ("UPDATE Professeur SET telephone=%s WHERE id=%s")
                val = (telephone, id)
                cursor.execute(request, val)
            if matiereEnseigne is not None:
                request = ("UPDATE Professeur SET matiereEnseigne=%s WHERE id=%s")
                val = (matiereEnseigne, id)
                cursor.execute(request, val)
            if prochainCours is not None:
                request = ("UPDATE Professeur SET prochainCours=%s WHERE id=%s")
                val = (prochainCours, id)
                cursor.execute(request, val)
            if sujetProchaineReunion is not None:
                request = ("UPDATE Professeur SET sujetProchaineReunion=%s WHERE id=%s")
                val = (sujetProchaineReunion, id)
                cursor.execute(request, val)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            return False

    #fonction de suppression en BD
    def supprimerEleve(id):
        try:
                
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=""
                )
            cursor = conn.cursor()
            cursor.execute("USE etab_db")
            val=(int(id))
            request = ("DELETE FROM Professeur WHERE id=%d")
            sql = "DELETE FROM Eleve WHERE id = '%d'" % (int(id))
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            print("Success")
        except :
            print("Error deleting record with id =", id)
    def supprimerProfesseur(id):
        try:
                
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=""
                )
            cursor = conn.cursor()
            cursor.execute("USE etab_db")
           
            sql = "DELETE FROM Professeur WHERE id = '%d'" % (int(id))
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            print("Success")
        except :
            print("Error deleting record with id =", id)


    def supprimerUser(identifiant,motDePasse):
        try:
                
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=""
                )
            cursor = conn.cursor()
            cursor.execute("USE etab_db")
            # delete_query = '''
            #      DELETE FROM utilisateur
            #       WHERE pseudo = %s
            #        AND mot_de_passe = %s;
            #         '''

          
            # cursor.execute(delete_query, (pseudo, mot_de_passe))
            val=(identifiant,motDePasse)
            request = ("DELETE FROM utilisateurs WHERE pseudo = %s AND motDePasse = %s")
            cursor.execute(request,val)
            conn.commit()
            cursor.close()
            conn.close()
            print("Success")
        except Exception as e:
            print("Error : ",e)
            print("Error deleting record with pseudo =", identifiant)

    #fonction pour avoir tout les utilisateurs d'un champ
    def obtenirUsers():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        cursor.execute("SELECT * FROM Utilisateurs")
        request = cursor.fetchall()
        return request
        

    def obtenirEleve():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        cursor.execute("SELECT * FROM Eleve")
        request = cursor.fetchall()
        return request

    def obtenirProfesseur():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        cursor.execute("SELECT * FROM Professeur")
        request = cursor.fetchall()
        return request





    #authentification
    def authenticate(identifiant,mdp):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        request = ("SELECT * FROM Utilisateurs WHERE pseudo=%s AND motDePasse=%s")
        val=(identifiant,mdp)
        cursor.execute(request,val)
        
        if cursor.fetchone() == None:
            return False
        else: 
            return True
    
    #fonction de recherche
    def rechercheEleve(matricule):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        request = ("SELECT * FROM Eleve WHERE matricule=%s")
        val=(matricule,)
        cursor.execute(request,val)
        
        if cursor.fetchone() == None:
            return False
        else: 
            return True
    
    def rechercheProfesseur(id):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        request = ("SELECT * FROM Professeur WHERE id=%s")
        val=(id,)
        cursor.execute(request,val)
        
        if cursor.fetchone() == None:
            return False
        else: 
            return True
    
    def rechercheUser(identifiant,Password):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("USE etab_db")
        request = ("SELECT * FROM Utilisateurs WHERE pseudo=%s AND motDePasse=%s")
        val=(identifiant,Password)
        cursor.execute(request,val)
        
        if cursor.fetchone() == None:
            return False
        else: 
            return True