# models/comportements/comportement_defensif.py
from models.actions.action_defense import ActionDefense
from models.comportement import Comportement
from models.action import Action
 
class ComportementDefensif(Comportement):
    def agir(self, ennemi) -> Action:
        return ActionDefense()