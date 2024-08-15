from datetime import datetime
# import menuEleve
# import menuEleve
# import menuUtilisateurs
import services.etab_DB as DB
# import menuPrincipal


class MenuEleve:

    def MenuStudent():
        isConnected =True
        while (isConnected):
            try : 
                print("             *************************************************************************\n ")
                print("                                      GESTION DES ELEVES                              \n ")
                print("             *************************************************************************")
                print(" MENU: ")
                print("\n 1. Ajouter un eleve\n 2. Supprimer un eleve\n 3. Modifier les informations du eleve\n 4. Lister les eleves\n 5. Obtenir le dernier eleve ajouté\n 6. retour\n0. Accueil")
                
            
                print("Date système : {}:{}".format(datetime.now().hour, datetime.now().minute))
                answer = int(input("\n Aller à : "))
                match answer:
                    case 1:
                        
                        nom = input("Nom : ")
                        prenom = input("Prenom : ")
                        matricule = input("Matricule de l'eleve : ")
                        classe = input ("La classe : ") 
                        # vacant = input("Classe : ")
                        
                        telephone = input("Telephone : ")
                        birthDay = input("Birth Day (DD/MM/YYYY) : ")
                        while True:
                            
                            if len(birthDay) == 10:
                                # print("Valid date format")
                                try:

                                    day, month, year = map(int, birthDay.split('/'))
                                    # print(f"Day: {day}, Month: {month}, Year: {year}")
                                    # if    1<=day<=31 and 1<=month<=12:
                                    #     date_object = datetime(year, month, day)
                                    #     print(date_object)
                                    birthDay = datetime(year, month, day)
                                    break
                                except ValueError : 
                                    print("Date entrée invalide")
                                    birthDay = input("Birth Day (DD/MM/YYYY) : ")
                                    continue
                            
                            else :
                                print("Date entrée invalide")
                                birthDay = input("Birth Day (DD/MM/YYYY) : ")
                        ville = input('Ville : ')
                        DB.Connection.AjouterEleve(dateNaissance=birthDay,nom=nom,ville=ville,prenom=prenom,matricule=matricule,classe=classe,telephone=telephone)
                        
                    case 2:
                        id = input(" ID : ")
                        DB.Connection.supprimerEleve(id=id)
                    case 3:
                        id = input("L'id à modifier : ")
                        
                        continues = DB.Connection.rechercheEleve(matricule=id)
                        
                        while continues:
                            # print("\n   1. Modifier le nom \n   2. Modifier le prenom \n   3. Modifier la date de naissance \n   4. Modifier Vacant \n   5. Modifier la ville \n   6. Retour")
                            print("\n 1. Modifier le nom \n 2. Modifier le prenom \n 3. Modifier la date de naissance \n 4. Modifier la classe \n 6. Modifier la ville \n 7. Modifier la matiere enseignée \n 8. Modifier le prochain cours \n 9. Modifier le sujet de reunion \n 10. Modifier le numero \n 11. Retour")
                            Res = int(input("Choisir une option : "))
                            match Res:
                                case 1:
                                    nom = input("Le nouveau nom du eleve : ")
                                    DB.Connection.editEleve(id,nom=nom)
                                    
                                case 2:
                                    prenom = input("Le nouveau prénom du eleve : ")
                                    DB.Connection.editEleve(id,prenom=prenom)
                                    
                                case 3:
                                    while True:
                                        birthDay = input("Birth Day (DD/MM/YYYY) : ")
                                        try:
                                            day, month, year = map(int, birthDay.split('/'))
                                            birthDay = datetime(year, month, day)
                                            DB.Connection.editEleve(id,dateNaissance=birthDay)
                                            break
                                        except ValueError :
                                            print("Date entrée invalide")
                                            continue
                                case 4:
                                    classe = input("Classe : ")
                                    DB.Connection.editEleve(id, classe=classe)
                                case 6:
                                    ville = input("La nouvelle ville du eleve : ")
                                    DB.Connection.editEleve(id,ville=ville)
                                    #  continue
                                    # print("Ville modifiée avec succès")
                                    # continue
                                    # else:
                                    #     print("Ville invalide")
                                    #     continue
                                case 7:
                                    matiere = input("La nouvelle matiere enseignée du eleve : ")
                                    DB.Connection.editEleve(id,matiereEnseigne=matiere)
                                    
                             
                                    
                                case 11:
                                    break


                                            
                    case 4:
                        result = DB.Connection.obtenirEleve()
                        if len(result)>=1:
                            print("\n ID | Nom | Prenom | Date de naissance | Classe | Ville | Telephone")
                            for eleve in result:
                                print(f"\n {eleve[0]} | {eleve[6]} | {eleve[5]} | {eleve[3]} | {eleve[1]} | {eleve[4]} | {eleve[7]} ")
                                
                        else: 
                            print("Aucun eleve enregistré")
                    case 5:
                        result = DB.Connection.obtenirEleve()

                        if len(result)>=1:
                            last = result[-1]
                            print("\n ID | Nom | Prenom | Date de naissance | Classe | Ville | Telephone")
                            print(f"\n {last[0]} | {last[6]} | {last[5]} | {last[3]} | {last[1]} | {last[4]} | {last[7]} ")
                            # print(f" | {last[2]} | {last[3]} | {last[4]} | {last[5]} | {last[6]} | {last[7]} | {last[8]} | {last[9]} | {last[10]}")
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
