from Controleur_valeur_menu import *
from Controleur_bdd_json import *
from Vue_menu_rapport import *
from Vue_menu_recherche_joueur import *
from Modele_joueur import *


def ctrl_menu_rapport():

    #Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_joueur = 0
    # Affichage de la vue menu joueur
    reponse_utilisateur = vue_menu_rapport()

    menu_max_joueur = reponse_utilisateur[1]
    reponse_menu = reponse_utilisateur[0]

    while reponse_utilisateur_menu_joueur != menu_max_joueur:
        

        reponse_utilisateur_menu_joueur = ctrl_valeur_menu(menu_max_joueur, reponse_menu)

        # Choix 1 : rapport joueur par ordre alphabetique
        if reponse_utilisateur_menu_joueur == 1:
            ctrl_rapport_joueur_alphabetique("nom")
        # Choix 2 : rapport joueur par ordre de classement
        elif reponse_utilisateur_menu_joueur == 2:
            ctrl_rapport_joueur_alphabetique("classement")
        # Choix 3 : rapport tournoi général
        elif reponse_utilisateur_menu_joueur == 3:
            pass
        # Choix 4 : rapport tournoi liste des joueurs par ordre alphabetique
        elif reponse_utilisateur_menu_joueur == 4:
            pass
        # Choix 5 : rapport tournoi liste des joueurs par ordre de classement
        elif reponse_utilisateur_menu_joueur == 5:
            pass
        # Choix 6 : rapport tournoi liste des tours
        elif reponse_utilisateur_menu_joueur == 6:
            pass
        # Choix 7 : rapport tournoi liste des matchs
        elif reponse_utilisateur_menu_joueur == 7:
            pass
        
        reponse_utilisateur = vue_menu_rapport()
        reponse_menu = reponse_utilisateur[0]
    
    # Choix 8 : Retour au menu principal
    pass

def ctrl_rapport_joueur_alphabetique(critere):
    base_joueur = initialisation_bdd_joueur()
    liste_joueur = {}
    liste_nom = []
    compteur = 1
    # Extrait les noms de tous les joueurs
    for joueur in base_joueur:
        liste_joueur[joueur['position']] = joueur[critere]
        liste_nom.append(joueur[critere])
    # Les tris par ordre alphabétique
    liste_nom.sort()
    
    for nom_joueur in liste_nom:
        position_trouvee = -1
        for position, nom in liste_joueur.items():
            if position_trouvee == -1:
                if nom_joueur == nom:
                    position_trouvee = position

        joueur_affiche = recherche_joueur_bdd("position", position_trouvee)
        del liste_joueur[position_trouvee]
        vue_menu_affichage_joueur_recherche_joueur(joueur_affiche[0],compteur)
        compteur += 1

    input("Appuyer sur ""Entrée"" pour continuer")
    return

