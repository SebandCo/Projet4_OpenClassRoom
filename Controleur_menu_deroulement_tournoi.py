from Vue_menu_nouveau_tournoi import *
from Modele_tournoi import *


def deroulement_tournoi(tournoi):
    
    while tournoi.tour_actif <= tournoi.nbr_tour:

        tournoi.creation_tour()
        vue_tournoi_liste_duel(tournoi)
        tournoi.recuperation_resultat()
        tournoi.tour_actif += 1
    
    tournoi.ordre_tour()
    vue_tournoi_resultat(tournoi)