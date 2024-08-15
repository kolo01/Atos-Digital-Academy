from Models.Interfaces.ICRUDProfesseur import ICRUDProfesseur
from Models.Interfaces.IEducation import IEducation
from Personne import Personne
class Professeur(Personne, ICRUDProfesseur, IEducation):
    def __init__(self, id,dateNaissance,ville,prenom,nom,vacant=False,All =[]):
        super().__init__(id, dateNaissance, ville, prenom, nom)
        self.__vacant = vacant
        Found = 0
        All.append([id, nom, prenom, dateNaissance, ville,vacant] )

        self.__All = All
        for personne in self.__All:
            if personne[0] == id:
                Found += 1
                
        # return selected if Found == 1 else "Elève introuvable"
        if Found > 1:
            self.__All.remove([id, nom, prenom, dateNaissance, ville,vacant])
            raise Exception("\033[31;1m ID déjà existant \033[0m")
        else:    
            self.__vacant = vacant
            
            print( '\033[32;1mProfesseur Enregistré avec succès \033[0m')
            print("\033[1;32m \n ID : {} \n Nom : {} \n Prenom : {} \n date de naissance : {} \n ville : {} \n Vacant : {} \n\033[0m".format(id,nom,prenom,dateNaissance,ville,vacant))
       
        
    def mettreAJour(self,id,newDateNaissance = None,newVille = None,newPrenom = None,newNom = None,vacant = None):
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
        if vacant:
            All[index][5] = vacant
            
        
        self.setAll(All)
        

    def ajouter(self):
        return self.__vacant

    def getAll(self):
        return self.__All

    def setAll(self,newAll):
        self.__All = newAll
