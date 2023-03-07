from Controleur.bdd_json import initialisation_bdd_tournoi
from Controleur.bdd_json import recherche_joueur_bdd
from Controleur.menu_deroulement_tournoi import deroulement_tournoi
from Controleur.valeur_menu import ctrl_valeur_menu
from Modele.joueur import Joueur
from Modele.joueur_tournoi import JoueurTournoi
from Modele.tournoi import Tournoi
from Vue.menu_tournoi_existant import vue_menu_revoir_reprendre_affichage_tournoi
from Vue.menu_tournoi_existant import vue_menu_revoir_reprendre_tournoi_accueil
"""
    Procédure pour le menu de reprise d'un tournoi
    Comprend:
    - La recherche d'un tournoi
    - Le passage d'un tournoi Json en objet
    - Le passage d'un joueur Json en objet
"""


# Permet de lancer le menu reprise de tournoi
def ctrl_reprise_tournoi_existant():
    tournoi_selectionne = ctrl_menu_recherche_tournoi()
    if tournoi_selectionne:
        tournoi_actif = ctrl_menu_passage_tournoi_json_objet(tournoi_selectionne)
        deroulement_tournoi(tournoi_actif)
    else:
        return


# Permet de selectionner un tournoi à reprendre
def ctrl_menu_recherche_tournoi():
    tournoi_existant = initialisation_bdd_tournoi()

    reponse_utilisateur_menu_tournoi = 0
    # Affichage de la vue menu joueur
    reponse_utilisateur = vue_menu_revoir_reprendre_tournoi_accueil(tournoi_existant)

    menu_max_tournoi = reponse_utilisateur[1]
    reponse_menu = reponse_utilisateur[0]

    while reponse_utilisateur_menu_tournoi != menu_max_tournoi:

        reponse_utilisateur_menu_tournoi = ctrl_valeur_menu(menu_max_tournoi, reponse_menu)

        if reponse_utilisateur_menu_tournoi != menu_max_tournoi:
            compteur = 0
            for tournoi in tournoi_existant:
                compteur += 1
                if compteur == reponse_utilisateur_menu_tournoi:
                    tournoi_selectionne = tournoi
                    nombre_trouve = compteur
            print("Vous avez choisi le tournoi :\n")
            vue_menu_revoir_reprendre_affichage_tournoi(nombre_trouve, tournoi_selectionne)
            input("Appuyer sur Entrée pour continuer")
            return tournoi_selectionne
    return


# Permet de transformer un tournoi JSON en tournoi Objet
def ctrl_menu_passage_tournoi_json_objet(tournoi):
    tournoi_objet = Tournoi(
                        tournoi["nom"],
                        tournoi["lieu"],
                        tournoi["date"],
                        tournoi["nbr_tour"],
                        tournoi["tour_actif"],
                        tournoi["tournee"],
                        tournoi["nbr_joueur"],
                        {},
                        tournoi["ctrl_temps"],
                        tournoi["description"],
                        tournoi["status"],
                        tournoi["round"],
                        tournoi["round_global"],
                        tournoi["position"])
    for joueur in tournoi["joueurs"]:
        nouveau_joueur = Joueur(
                        tournoi["joueurs"][joueur]["nom"],
                        tournoi["joueurs"][joueur]["prenom"],
                        tournoi["joueurs"][joueur]["naissance"],
                        tournoi["joueurs"][joueur]["sexe"],
                        tournoi["joueurs"][joueur]["classement"],
                        tournoi["joueurs"][joueur]["position"])

        # Vérifie que le classement n'a pas changé depuis le dernier accès au tournoi
        joueur_temporel = recherche_joueur_bdd("position", nouveau_joueur.position)
        if joueur_temporel[0]["classement"] != nouveau_joueur.classement:
            nouveau_joueur.classement = joueur_temporel[0]["classement"]

        nouveau_joueur = JoueurTournoi(
                        nouveau_joueur,
                        tournoi["joueurs"][joueur]["couleur"],
                        tournoi["joueurs"][joueur]["paires"],
                        tournoi["joueurs"][joueur]["points"],
                        tournoi["joueurs"][joueur]["ordre"])

        tournoi_objet.joueurs[int(joueur)] = nouveau_joueur
    return tournoi_objet
