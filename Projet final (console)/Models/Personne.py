from datetime import datetime

class Personne:
    def __init__(self,id,dateNaissance,ville,prenom,nom):
        self.__id = id
        self.__dateNaissance = dateNaissance
        self.__ville = ville
        self.__prenom = prenom
        self.__nom = nom
       
    
    def supprimer(self,id):
        All = self.getAll()
     
        for personne in All:
            if personne[0] == id:
                All.remove(personne)
                break
        self.setAll(All)
        print("Personne avec l'id {} supprimé avec succès".format(id))
       
    
    def lister(self):
        counter = 0
        All = self.getAll()
        if All is not None:
            for personne in All:
                counter += 1
                print("\n N° {} \n ID : {} \n Name : {} \n Prenom : {} \n Date de naissance : {} \n Ville : {}".format(counter,personne[0],personne[1],personne[2],personne[3],personne[4]))
        else:
            return "Aucune personne enregistrée"

    def obtenirAge(age):
        
        today = datetime.today()
        age = today.year - int(self.__dateNaissance[:4]) - ((today.month, today.day) < (int(self.__dateNaissance[5:7]), int(self.__dateNaissance[8:])))
        return age
    
    def obtenirDernier(self):
        All = self.getAll()
        if All is not None:
            Dernier = All[-1]
            print("\n ID : {} \n Name : {} \n Prenom : {} \n Date de naissance : {} \n Ville : {}".format(Dernier[0],Dernier[1],Dernier[2],Dernier[3],Dernier[4]))

    def getId(self):
        return self.__id
    
    def getDateNaissance(self):
        return self.__dateNaissance
    
    def getVille(self):
        return self.__ville
    
    def getPrenom(self):
        return self.__prenom
    
    def getNom(self):
        return self.__nom
    
    def setDateNaissance(self, dateNaissance):
        self.__dateNaissance = dateNaissance
    
    def setVille(self, ville):
        self.__ville = ville
    
    def setPrenom(self, prenom):
        self.__prenom = prenom

    def setNom(self, nom):
        self.__nom = nom
    
 
