from datetime import datetime
# import menuEleve
# import menuEleve
# import menuUtilisateurs
import services.etab_DB as DB
# import menuPrincipal


class MenuUsers:

    def MenuUtilisateur():
        isConnected =True
        while (isConnected):
            try : 
                print("             *************************************************************************\n ")
                print("                                      GESTION DES UTILISATEURS                        \n ")
                print("             *************************************************************************")
                print(" MENU: ")
                print("\n 1. Ajouter un Utilisateur\n 2. Supprimer un Utilisateur\n 3. Modifier les informations d'un Utilisateur\n 4. Lister les Utilisateur\n 5. Retour \n0. Accueil")
                
            
                print("Date système : {}:{}".format(datetime.now().hour, datetime.now().minute))
                answer = int(input("\n Aller à : "))
                match answer:
                    case 1:
                        
                        Pseudo = input("Identifiant : ")
                        motDePasse = input("Mot de passe : ")
                       
                        DB.Connection.AjouterUtilisateurs(identifiant=Pseudo,motDePasse=motDePasse)
                        
                    case 2:
                        Pseudo = input("Identifiant : ")
                        motDePasse = input("Mot de passe : ")
                        DB.Connection.supprimerUser(identifiant=Pseudo,motDePasse=motDePasse)
                    case 3:
                        Pseudo = input("Identifiant : ")
                        motDePasse = input("Mot de passe : ")
                        
                        
                        continues = DB.Connection.rechercheUser(identifiant=Pseudo,Password=motDePasse)
                        if continues:
                            while continues:
                                motDePasse = input("Le nouveau mot de passe : ")
                                DB.Connection.editUser(identifiant=Pseudo,NewPassword=motDePasse)
                                break
                            print("Modifiaction Effectué")
                        else:
                            print("Utilisateur introuvable")

                                            
                    case 4:
                        result = DB.Connection.obtenirUsers()
                        if len(result)>=1:
                            print("\n ID | Pseudo | Mot de passe | Date de creation")
                            for eleve in result:
                                print(f"\n {eleve[0]} | {eleve[1]} | {eleve[2]} | {eleve[3]}")
                                
                        else: 
                            print("Aucun eleve enregistré")
                    case 5:
                        result = DB.Connection.obtenirUsers()

                        if len(result)>=1:
                            last = result[-1]
                            print("\n ID | Pseudo | Mot de passe | Date de creation")
                            print(f"\n {eleve[0]} | {eleve[1]} | {eleve[2]} | {eleve[3]}")
                        else:
                            print("Aucun eleve enregistré")
                    case 6:
                        break
                        # menuPrincipal.MenuPrincipal()
                    case 0:
                        # isConnected = False
                        # Default()
                        break
                        
                    case _:
                        print("Erreur choix indisponible")


            except Exception as e : 
                print("Erreur : ", e)
