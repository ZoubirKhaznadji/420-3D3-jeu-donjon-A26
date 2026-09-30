# models/comportements/comportement_furtif.py
from models.action import Action
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefense
from models.comportement import Comportement


class ComportementFurtif(Comportement):

    def __init__(self) -> None:
        self._tour = 0   # ← valeur initiale ?

    def agir(self, ennemi) -> Action:
        self._tour += 1
        if self._tour % 2 == 0:
            return ActionAttaque()
        return ActionDefense()