# models/comportements/comportement_aleatoire.py
import random
from models.comportement import Comportement
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefense
from models.action import Action


class ComportementAleatoire(Comportement):

    def agir(self, ennemi) -> Action:
        return random.choice([ActionAttaque(), ActionDefense()])