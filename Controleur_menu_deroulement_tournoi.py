from Vue_menu_nouveau_tournoi import *


def deroulement_tournoi(tournoi):
    if tournoi.tour_actif == 1:
        #Début du tournoi
        tournoi.creation_premier_tour()
        vue_tournoi_liste_duel(tournoi)
    else:
        #Boucle sur les tours suivant
        while tournoi.tour_actif <= tournoi.nbr_tour:
            tournoi.tour_actif += 1