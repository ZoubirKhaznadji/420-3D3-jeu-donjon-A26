# models/comportements/comportement_agressif.py
from models.actions.action_attaque import ActionAttaque
from models.comportement import Comportement
from models.action import Action

 
class ComportementAgressif(Comportement):
    def agir(self, ennemi) -> Action:
        return ActionAttaque()
 
