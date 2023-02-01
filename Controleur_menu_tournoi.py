from Vue_menu_nouveau_tournoi import *
from Modele_tournoi import *


def ctrl_menu_tournoi():
    vue_menu_nouveau_tournoi()
    nouveau_tournoi = Tournoi()
    nouveau_tournoi.creation_tournoi()
    vue_recap_menu_nouveau_tournoi(nouveau_tournoi)
    input("Tournoi crée")