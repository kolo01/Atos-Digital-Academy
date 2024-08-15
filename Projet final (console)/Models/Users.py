class Utilisateur:
    def __init__(self, id, identifiant, motDePasse):
        self.__id = id
        self.__identifiant = identifiant
        self.__motDePasse = motDePasse

    def authentication(self,identifiant, motDePasse) -> bool:
        return True
    
    def ajouterCompte(self,identifiant, motDePasse) -> bool:
        return True
    
    def modifierMotDePasse(self,identifiant, motDePasse) -> bool:
        return True
    
    def supprimerCompte(self, identifiant, motDePasse) -> bool:
        return True
    
    def listerUtilisateur(self) -> list : 
        return []