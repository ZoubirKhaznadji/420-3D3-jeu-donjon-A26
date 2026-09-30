# models/ennemi.py
from models.comportement import Comportement
from models.action import Action
 
class Ennemi:
 
    def __init__(self, nom: str, hp: int, attaque: int,
                 comportement: Comportement,
                 regles_adaptation=None) -> None:
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self._comportement = comportement
        self._regles_adaptation = regles_adaptation or []   # ← liste, vide par défaut

    def agir(self) -> "Action":
        return self._comportement.agir(self)
 
    def est_vivant(self) -> bool:
        return self.hp > 0

    def get_comportement(self) -> Comportement:
        return self._comportement

    def set_comportement(self, comportement: Comportement) -> None:
        self._comportement = comportement

    def recevoir_degats(self, degats: int) -> None:
        self.subir_degats(degats)
    
    def subir_degats(self, degats: int) -> None:
        self.hp = max(0, self.hp - degats)
        for regle in self._regles_adaptation:
            regle(self)                             # ← chaque règle est appelée dans l'ordre