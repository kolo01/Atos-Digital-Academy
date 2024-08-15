from abc import ABC,abstractmethod
#Class abstraite ICRUDProfesseur
class ICRUDProfesseur(ABC):
    
    #Interface ajouter
    @abstractmethod
    def ajouter(self, professeur):
        pass
    
    #Interface modifier
    @abstractmethod
    def modifier(self, professeur):
        pass
    
    #Interface supprimer
    @abstractmethod 
    def supprimer(self, identifiant: int):
        pass
    
    #Interface obtenir
    @abstractmethod
    def obtenir(self, identifiant: int):
        pass
    
    #Interface lister
    @abstractmethod
    def ObtenirProfesseur(self):
        pass