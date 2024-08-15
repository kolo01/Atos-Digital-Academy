from datetime import datetime

from template import menuProfesseur, menuEleve, menuUtilisateurs


class Menu:

      def MenuPrincipal(isConnected):
        while (isConnected):
            try : 
                print("             *************************************************************************\n ")
                print("                               BIENVENUE DANS L'APPLICATION ETAB v1.2                 \n ")
                print("             *************************************************************************")
                print(" MENU: ")
                print("\n 1. Gestion des élèves\n 2. Gestion des professeurs\n 3. Gestion des utilisateurs\n 4. Deconnexion\n 0. Quitter")
                print("Date système : {}:{}".format(datetime.now().hour, datetime.now().minute))

                answer = input("\n Aller à : ")
                match answer:
                    case "1":
                        menuEleve.MenuEleve.MenuStudent()
                        # menuEleve()
                    case "2":
                        menuProfesseur.MenuProfesseur.MenuProf()
                    case "3":
                        menuUtilisateurs.MenuUsers.MenuUtilisateur()
                        # menuUtilisateurs()
                    case "4":
                        isConnected = False
                        # Default
                    case "0":
                        isConnected = False
                        print('Au revoir Mr/Mme')
                        break
                    case _:
                        print("Erreur choix indisponible")


            except Exception as e: 
                print ("Veuillez verifier votre choix ")
          