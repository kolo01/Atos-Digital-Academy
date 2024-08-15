from datetime import datetime
# import menuEleve
# import menuProfesseur
# import menuUtilisateurs
import services.etab_DB as DB
# import menuPrincipal


class MenuProfesseur:

    def MenuProf():
        isConnected =True
        while (isConnected):
            try : 
                print("             *************************************************************************\n ")
                print("                                      GESTION DES PROFESSEURS                         \n ")
                print("             *************************************************************************")
                print(" MENU: ")
                print("\n 1. Ajouter un professeur\n 2. Supprimer un professeur\n 3. Modifier les informations du professeur\n 4. Lister les professeurs\n 5. Obtenir le dernier professeur ajouté\n 6. retour\n0. Accueil")
                
            
                print("Date système : {}:{}".format(datetime.now().hour, datetime.now().minute))
                answer = int(input("\n Aller à : "))
                match answer:
                    case 1:
                        
                        nom = input("Nom : ")
                        prenom = input("Prenom : ")
                        # vacant = input("Classe : ")
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
                        email = input("Email: ")
                        matiere = input("Matiere enseignée : ")
                        prochain = input("Prochain cours : ")
                        telephone = input("Telephone : ")
                        sujetReunion = input("Sujet de la prochaine reunion : ")


                        
                        ville = input('Ville : ')
                        DB.Connection.AjouterProfesseur(dateNaissance=birthDay,ville=ville,prenom=prenom,email=email,vacant=False,matiereEnseigne=matiere,prochainCours=prochain,nom=nom,sujetProchaineReunion=sujetReunion,telephone=telephone)
                        
                    case 2:
                        id = input(" ID : ")
                        DB.Connection.supprimerProfesseur(id=id)
                    case 3:
                        id = input("L'id à modifier : ")
                        
                        continues = DB.Connection.rechercheProfesseur(id=id)
                        
                        while continues:
                            # print("\n   1. Modifier le nom \n   2. Modifier le prenom \n   3. Modifier la date de naissance \n   4. Modifier Vacant \n   5. Modifier la ville \n   6. Retour")
                            print("\n 1. Modifier le nom \n 2. Modifier le prenom \n 3. Modifier la date de naissance \n 4. Modifier la vacation \n 5. modifier l'email  \n 6. Modifier la ville \n 7. Modifier la matiere enseignée \n 8. Modifier le prochain cours \n 9. Modifier le sujet de reunion \n 10. Modifier le numero \n 11. Retour")
                            Res = int(input("Choisir une option : "))
                            match Res:
                                case 1:
                                    nom = input("Le nouveau nom du professeur : ")
                                    DB.Connection.editProfesseur(id,nom=nom)
                                    
                                case 2:
                                    prenom = input("Le nouveau prénom du professeur : ")
                                    DB.Connection.editProfesseur(id,prenom=prenom)
                                    
                                case 3:
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
                                case 4:
                                    vacant = input("Vacant? Oui/Non : ")
                                    if vacant.upper() == "OUI":
                                        DB.Connection.editProfesseur(id, vacant=True)
                                    elif vacant.upper() == "NON":
                                        DB.Connection.editProfesseur(id, vacant=False)
                                    else:
                                        print("Reponse invalide")
                                case 5:
                                    email = input("Le nouvel email du professeur : ")
                                    DB.Connection.editProfesseur(id,email=email)
                                case 6:
                                    ville = input("La nouvelle ville du professeur : ")
                                    DB.Connection.editProfesseur(id,ville=ville)
                                    #  continue
                                    # print("Ville modifiée avec succès")
                                    # continue
                                    # else:
                                    #     print("Ville invalide")
                                    #     continue
                                case 7:
                                    matiere = input("La nouvelle matiere enseignée du professeur : ")
                                    DB.Connection.editProfesseur(id,matiereEnseigne=matiere)
                                    
                                case 8:
                                    prochain = input("Le  prochain cours du professeur : ")
                                    DB.Connection.editProfesseur(id,prochainCours=prochain)
                                    
                                case 9:
                                    sujetReunion = input("Le nouveau sujet de reunion du professeur : ")
                                    DB.Connection.editProfesseur(id,sujetProchaineReunion=sujetReunion)
                                    
                                case 10:
                                    telephone = input("Le nouveau numero de telephone du professeur : ")
                                    DB.Connection.editProfesseur(id,telephone=telephone)
                                    
                                case 11:
                                    break


                                            
                    case 4:
                        result = DB.Connection.obtenirProfesseur()
                        if len(result)>=1:
                            print("\n ID | Nom | Prenom | Date de naissance | Vacant | Ville | Matiere enseignée | Prochain cours | Email | Telephone | Sujet de la prochaine reunion")
                            for prof in result:
                                print(f"\n {prof[0]} | {prof[4]} | {prof[3]} | {prof[1]} | {bool(prof[6])} | {prof[2]} | {prof[8]} | {prof[9]} | {prof[5]} | {prof[7]} | {prof[10]}")
                                
                        else: 
                            print("Aucun professeur enregistré")
                    case 5:
                        result = DB.Connection.obtenirProfesseur()

                        if len(result)>=1:
                            last = result[-1]
                            print("\n ID | Nom | Prenom | Date de naissance | Vacant | Ville | Matiere enseignée | Prochain cours | Email | Telephone | Sujet de la prochaine reunion")
                            print(f"\n {last[0]} | {last[4]} | {last[3]} | {last[1]} | {bool(last[6])} | {last[2]} | {last[8]} | {last[9]} | {last[5]} | {last[7]} | {last[10]}")
                            # print(f" | {last[2]} | {last[3]} | {last[4]} | {last[5]} | {last[6]} | {last[7]} | {last[8]} | {last[9]} | {last[10]}")
                        else:
                            print("Aucun professeur enregistré")
                    case 6:
                        break
                        # menuPrincipal.MenuPrincipal()
                    case 0:
                        isConnected = False
                        # Default()
                        break
                        
                    case _:
                        print("Erreur choix indisponible")


            except Exception as e : 
                print("Erreur : ", e)
