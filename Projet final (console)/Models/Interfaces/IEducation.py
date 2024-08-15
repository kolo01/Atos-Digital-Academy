from abc import ABC,abstractmethod

#Class abstraite IEducation
class IEducation(ABC):
    
    #Interface enseigner
    @abstractmethod
    def enseigner(self, matiere):
        pass
    #Interface préparerCours
    @abstractmethod
    def preparerCours(self, cours):
        pass
    #Interface assisterReunion
    @abstractmethod
    def assisterReunion(self, sujet):
        pass