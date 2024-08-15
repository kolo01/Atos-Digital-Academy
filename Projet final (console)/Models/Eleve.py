from Models.Interfaces import ICRUDEleve
from Personne import Personne
class Eleve (Personne, ICRUDEleve):
    def __init__(self, id,dateNaissance,ville,prenom,nom,classe,All =[]):
        super().__init__(id, dateNaissance, ville, prenom, nom)
        self.__classe = classe
        Found = 0
        All.append([id, nom, prenom, dateNaissance, ville,classe] )

        self.__All = All
        for personne in self.__All:
            if personne[0] == id:
                Found += 1
                
        # return selected if Found == 1 else "Elève introuvable"
        if Found > 1:
            self.__All.remove([id, nom, prenom, dateNaissance, ville,classe])
            raise Exception("\033[31;1m ID déjà existant \033[0m")
        else:    
            self.__classe = classe
            
            print( '\033[32;1mElève Enregistré avec succès \033[0m')
            print("\033[1;32m \n ID : {} \n Nom : {} \n Prenom : {} \n date de naissance : {} \n ville : {} \n classe : {} \n\033[0m".format(id,nom,prenom,dateNaissance,ville,classe))
       
        

 

    def mettreAJour(self,id,newDateNaissance = None,newVille = None,newPrenom = None,newNom = None,newClasse = None):
        All = self.getAll()
        index = 0
        for personne in All:
            if personne[0] == id:
                index = All.index(personne)
                print(index)
                break
        if newDateNaissance:
            All[index][3] = newDateNaissance
        if newVille:
            All[index][4] = newVille
        if newPrenom:
           All[index][2] = newPrenom
        if newNom:
            All[index][1] = newNom
        if newClasse:
            All[index][5] = newClasse
            
        
        self.setAll(All)
        




    def getClasse(self):
        return self.__classe
    
    def setClasse(self, newClasse):
        self.__classe = newClasse
        
    def getAll(self):
        return self.__All

    def setAll(self,newAll):
        self.__All = newAll