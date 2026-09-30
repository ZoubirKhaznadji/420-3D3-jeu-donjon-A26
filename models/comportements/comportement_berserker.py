# models/comportements/comportement_berserker.py
from models.comportement import Comportement
from models.actions.action_attaque import ActionAttaque
from models.actions.action_attaque_double import ActionAttaqueDouble
from models.action import Action
 
 
class ComportementBerserker(Comportement):
 
    def agir(self, ennemi) -> Action:
        if ennemi.hp < ennemi.hp_max * 0.3:
            return ActionAttaqueDouble()
        return ActionAttaque()