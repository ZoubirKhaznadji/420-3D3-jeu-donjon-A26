from random import random
from models.comportement import Comportement

class Ennemi:
    def __init__(self, nom : str , hp :int , attaque : int , comportement : Comportement):
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self.comportement = comportement  # "agressif", "defensif", "aleatoire", "furtif"
        

    def agir(self) -> str:
        self.comportement.agir(self)

    def recevoir_degats(self, degats):
        self.hp = max(0, self.hp - degats)

    def est_vivant(self):
        return self.hp > 0