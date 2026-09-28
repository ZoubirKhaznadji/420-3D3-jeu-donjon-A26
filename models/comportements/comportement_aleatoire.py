# models/comportements/comportement_aleatoire.py
import random
from models.comportement import Comportement


class ComportementAleatoire(Comportement):

    def agir(self, ennemi) -> str:
        return random.choice(["attaque", "defend"])