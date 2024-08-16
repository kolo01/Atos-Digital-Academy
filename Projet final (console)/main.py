import services.etab_DB as DB
from template.menuPrincipal import Menu
class Main :

    

    def Default():
        DB.Connection.creer_base_de_donnees()
        isConnected = False
        
        print("             *************************************************************************\n ")
        print("                               BIENVENUE DANS L'APPLICATION ETAB v1.3                 \n ")
        print("             *************************************************************************")
        print("                                         CONNEXION")
        
        while isConnected == False:   
            id = input("Identifiant : ")
            pwd = input("Mot de passe : ")
            isConnected= DB.Connection.authenticate(id,pwd)
            # print(isConnected)
            if isConnected:
                print("Connexion réussie!")
                break
            else:
                print("Identifiants incorrects!")
        Menu.MenuPrincipal(isConnected=isConnected ) 

        
    
if __name__ == "__main__":
    monApp= Main
    monApp.Default()