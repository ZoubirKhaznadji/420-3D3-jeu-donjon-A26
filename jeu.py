from models.ennemi import Ennemi
from models.comportements.comportement_agressif import ComportementAgressif
from models.comportements.comportement_defensif import ComportementDefensif
from models.comportements.comportement_aleatoire import ComportementAleatoire
from models.comportements.comportement_furtif import ComportementFurtif
from models.comportements.comportement_berserker import ComportementBerserker
from models.regles_adaptation import devenir_defensif_si_faible, devenir_agressif_si_fort


class Jeu:
    def __init__(self):
        self.heros_hp = 100
        self.heros_hp_max = 100
        self.heros_attaque = 20
        

        self.ennemis = [
            Ennemi("Goblin", 50, 10, ComportementAgressif()),
            Ennemi("Dragon", hp=100, attaque=12,
                comportement=ComportementAgressif(),
                regles_adaptation=[devenir_defensif_si_faible, devenir_agressif_si_fort]),
            Ennemi("Voleur", 30, 15, ComportementFurtif()),
            Ennemi("Spectre", 40, 10, ComportementAleatoire()),
            Ennemi("Troll", 150, 20, ComportementBerserker())
        ]


    def ennemis_vivants(self):
        return [e for e in self.ennemis if e.est_vivant()]

    def demarrer(self):
        print("\n===========================================")
        print("        LE DONJON DES ALGORITHMES")
        print("===========================================\n")

        tour = 1

        while self.heros_hp > 0 and self.ennemis_vivants():
            # Afficher l'état
            print(f"Tour {tour} — Héros (HP: {self.heros_hp}/{self.heros_hp_max})")
            print("\nEnnemis :")
            vivants = self.ennemis_vivants()
            for i, ennemi in enumerate(vivants, 1):
                print(f"[{i}] {ennemi.nom} (HP: {ennemi.hp}/{ennemi.hp_max}) — {type(ennemi.get_comportement).__name__}")
        
            print()

            # Demander l'action du héros
            while True:
                action = input("Votre action ? (a)ttaquer / (d)éfendre : ").strip().lower()
                if action in ["a", "d"]:
                    break
                print("Choix invalide.")
            action_heros = "attaque" if action == "a" else "defend"

            # Demander la cible si attaque
            cible = None
            if action_heros == "attaque":
                if len(vivants) == 1:
                    cible = vivants[0]
                else:
                    while True:
                        try:
                            choix = int(input(f"Quel ennemi ? (1-{len(vivants)}) : "))
                            if 1 <= choix <= len(vivants):
                                cible = vivants[choix - 1]
                                break
                        except ValueError:
                            pass
                        print("Choix invalide.")

            # Chaque ennemi décide de son action
            actions_ennemis = {e: e.agir() for e in vivants}

            print("--- Résultats ---")

            # Résoudre l'attaque du héros
            if action_heros == "attaque" and cible:
                if actions_ennemis.get(cible) == "defend":
                    degats = self.heros_attaque // 2
                    print(f"Vous attaquez {cible.nom} — il se défend ! Seulement {degats} dégâts infligés.")
                else:
                    degats = self.heros_attaque
                    print(f"Vous attaquez {cible.nom} pour {degats} dégâts !")
                cible.recevoir_degats(degats)

            # Résoudre les actions des ennemis
            for ennemi in self.ennemis:
                if not ennemi.est_vivant():
                    continue
                action = ennemi.agir()                                          # ← un objet Action
                self.heros_hp, msg = action.appliquer(ennemi, self.heros_hp, action_heros)
                print(msg)

            # Adaptation des comportements
            for ennemi in self.ennemis_vivants():
                if ennemi.hp < ennemi.hp_max * 0.3 and type(ennemi.get_comportement)!=ComportementDefensif:
                    ennemi.set_comportement(ComportementDefensif())
                    print(f"  ⚡ {ennemi.nom} change de tactique — il devient Défensif !")

            print()
            tour += 1

        if self.heros_hp > 0:
            print("\n===========================================")
            print("  🏆 VICTOIRE ! Tous les ennemis sont vaincus !")
            print("===========================================\n")
        else:
            print("\n===========================================")
            print("  💀 DÉFAITE ! Le héros est tombé...")
            print("===========================================\n")
