# models/comportements/comportement_agressif.py
from models.comportement import Comportement


class ComportementAgressif(Comportement):

    def agir(self, ennemi) -> str:
        return "attaque"