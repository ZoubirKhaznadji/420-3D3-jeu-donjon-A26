from models.comportement import Comportement
from models.action import Action
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefense
from models.actions.action_attaque_double import ActionAttaqueDouble

class boss(Comportement):
    def agir(self, ennemi) -> Action:
        if ennemi.hp > ennemi.hp_max * 0.6:
            return ActionDefense()
        elif ennemi.hp > ennemi.hp_max * 0.3 and ennemi.hp <= ennemi.hp_max * 0.6:
            return ActionAttaque()
        elif ennemi.hp <= ennemi.hp_max * 0.3:
            return ActionAttaqueDouble
        


