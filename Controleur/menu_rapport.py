from Controleur.bdd_json import initialisation_bdd_joueur
from Controleur.bdd_json import initialisation_bdd_tournoi
from Controleur.bdd_json import recherche_joueur_bdd
from Controleur.menu_tournoi_existant import ctrl_menu_passage_tournoi_json_objet
from Controleur.menu_tournoi_existant import ctrl_menu_recherche_tournoi
from Controleur.rapport_flake import rapport_flake8
from Controleur.valeur_menu import ctrl_valeur_menu
from Vue.menu_rapport import vue_menu_rapport
from Vue.menu_rapport import vue_rapport_tours
from Vue.menu_recherche_joueur import vue_menu_affichage_joueur_recherche_joueur
from Vue.menu_tournoi_existant import vue_menu_revoir_reprendre_affichage_tournoi
"""
    Procédure pour le menu sur la gestion des rapports
    Comprend
    - Le menu d'orientation des rapports
    - L'affichage des différents rapports existant
"""


# Permet de lancer le menu rapport et la redirection en fonction des réponses
def ctrl_menu_rapport():

    # Initialisation de la réponse utilisateur
    reponse_utilisateur_menu_joueur = 0
    # Affichage de la vue menu joueur
    reponse_utilisateur = vue_menu_rapport()

    menu_max_joueur = reponse_utilisateur[1]
    reponse_menu = reponse_utilisateur[0]

    while reponse_utilisateur_menu_joueur != menu_max_joueur:

        reponse_utilisateur_menu_joueur = ctrl_valeur_menu(menu_max_joueur, reponse_menu)

        # Choix 1 : rapport joueur par ordre alphabetique
        if reponse_utilisateur_menu_joueur == 1:
            ctrl_rapport_tri_joueur("nom", "")
        # Choix 2 : rapport joueur par ordre de classement
        elif reponse_utilisateur_menu_joueur == 2:
            ctrl_rapport_tri_joueur("classement", "")
        # Choix 3 : rapport tournoi général
        elif reponse_utilisateur_menu_joueur == 3:
            ctrl_rapport_tournoi()
        # Choix 4 : rapport tournoi liste des joueurs par ordre alphabetique
        elif reponse_utilisateur_menu_joueur == 4:
            ctrl_rapport_tournoi_specifique("nom")
        # Choix 5 : rapport tournoi liste des joueurs par ordre de classement
        elif reponse_utilisateur_menu_joueur == 5:
            ctrl_rapport_tournoi_specifique("classement")
        # Choix 6 : rapport tournoi liste des tours
        elif reponse_utilisateur_menu_joueur == 6:
            ctrl_rapport_tournoi_tours()
        # Choix 7 : rapport tournoi liste des matchs
        elif reponse_utilisateur_menu_joueur == 7:
            ctrl_rapport_tournoi_tours()
        # Choix 8 : rapport flake8
        elif reponse_utilisateur_menu_joueur == 8:
            ctrl_rapport_flake8()
        # Choix 9 : Sortir du programme
        elif reponse_utilisateur_menu_joueur == 9:
            break

        reponse_utilisateur = vue_menu_rapport()
        reponse_menu = reponse_utilisateur[0]


# Permet de générer un rapport flake8 au format HTML
def ctrl_rapport_flake8():
    rapport_flake8()


# Permet de d'afficher le rapport des tours d'un tournoi
def ctrl_rapport_tournoi_tours():
    tournoi_selectionne = ctrl_menu_recherche_tournoi()
    # Si l'utilisateur choisi un tournoi, on continu
    if tournoi_selectionne:
        tournoi_actif = ctrl_menu_passage_tournoi_json_objet(tournoi_selectionne)
        vue_rapport_tours(tournoi_actif)
    # Sinon on arrete
    else:
        return


# Permet d'afficher la liste des joueurs d'un tournoi choisi
def ctrl_rapport_tournoi_specifique(critere):
    tournoi_actif = ctrl_menu_recherche_tournoi()
    # Si l'utilisateur choisi un tournoi, on continu
    if tournoi_actif:
        ctrl_rapport_tri_joueur(critere, tournoi_actif)
    # Sinon on arrete
    else:
        return


# Permet d'afficher la liste des tournoi
def ctrl_rapport_tournoi():
    print("\nVoici le rapport demandé: \n")
    base_tournoi = initialisation_bdd_tournoi()
    compteur = 1
    for tournoi in base_tournoi:
        vue_menu_revoir_reprendre_affichage_tournoi(compteur, tournoi)
        compteur += 1
    input("Appuyer sur ""Entrée"" pour continuer")
    return


# Permet d'afficher la liste générale des joueurs
def ctrl_rapport_tri_joueur(critere, base):
    print("\nVoici le rapport demandé: \n")
    if base == "":
        base_joueur = initialisation_bdd_joueur()
    else:
        base_joueur = base
    liste_joueur = {}
    liste_nom = []
    compteur = 1
    # Extrait les critere de recherche de tous les joueurs
    if base == "":
        for joueur in base_joueur:
            liste_joueur[joueur['position']] = joueur[critere]
            liste_nom.append(joueur[critere])
    else:
        for joueur in base_joueur['joueurs']:
            liste_joueur[base_joueur['joueurs'][joueur]['position']] = base_joueur['joueurs'][joueur][critere]
            liste_nom.append(base_joueur['joueurs'][joueur][critere])

    # Le tri par ordre alphabétique ou croissant
    liste_nom.sort()

    for nom_joueur in liste_nom:
        position_trouvee = -1
        for position, nom in liste_joueur.items():
            if position_trouvee == -1:
                if nom_joueur == nom:
                    position_trouvee = position

        joueur_affiche = recherche_joueur_bdd("position", position_trouvee)
        del liste_joueur[position_trouvee]
        vue_menu_affichage_joueur_recherche_joueur(joueur_affiche[0], compteur)
        compteur += 1

    input("Appuyer sur ""Entrée"" pour continuer")
    return
