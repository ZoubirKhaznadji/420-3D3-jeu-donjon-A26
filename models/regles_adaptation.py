# models/regles_adaptation.py
 
from models.comportements.comportement_agressif import ComportementAgressif
from models.comportements.comportement_defensif import ComportementDefensif
 
def devenir_defensif_si_faible(ennemi):
    """Bascule en mode défensif sous 30% de HP."""
    if ennemi.hp < ennemi.hp_max * 0.3:
        ennemi.set_comportement(ComportementDefensif())
        print(f"  ⚡ {ennemi.nom} change de tactique — il devient Défensif !")
 
 
def devenir_agressif_si_fort(ennemi):
    """Bascule en mode agressif au-dessus de 50% de HP (ennemi soigné)."""
    if ennemi.hp > ennemi.hp_max * 0.5:
        ennemi.set_comportement(ComportementAgressif())
        print(f"  ⚡ {ennemi.nom} change de tactique — il redevient Agressif !")