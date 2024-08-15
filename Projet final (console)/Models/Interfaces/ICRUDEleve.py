from abc import ABC,abstractmethod
class ICRudeleve(ABC):

    #Interface ajouter
    @abstractmethod
    def ajouter(eleve):
        pass
    
    #Interface modifier
    @abstractmethod
    def modifier(eleve):
        pass
    
    #Interface supprimer
    @abstractmethod
    def supprimer(identifiant):
        pass

    #Interface obtenir
    @abstractmethod
    def obtenir(identifiant):
        pass

    #Interface lister
    @abstractmethod
    def ObtenirEleve(identifiant):
        pass