from tinydb import TinyDB, where, Query
from Controleur_valeur_menu import *

def initialisation_bdd_joueur():
    joueurs_bdd = TinyDB("joueurs_bdd.json")
    joueur_aj = joueurs_bdd.table("joueur_aj")
    return joueur_aj

def recherche_joueur_bdd(categorie_recherche, mot_recherche):
    bdd_joueur = initialisation_bdd_joueur()
    #Regarde si le joueur avec le classement en argument existe
    joueur_trouve=bdd_joueur.search(where(categorie_recherche) == mot_recherche)
    #Si la réponse est vide, ne retourne rien
    return (joueur_trouve)

def modif_joueur_bdd(position,categorie_recherche):
    Joueur = Query()
    bdd_joueur = initialisation_bdd_joueur()
    valeur_modif = input("Si vous voulez modifier, merci de saisir la nouvelle valeur, sinon valider simplement : ")
    if valeur_modif:
        if categorie_recherche == "classement" :
            valeur_modif = ctrl_valeur_utilisateur(valeur_modif)
        bdd_joueur.update({categorie_recherche:valeur_modif}, Joueur.position == position)
        return valeur_modif
    return

def initialisation_bdd_tournoi():
    tournoi_bdd = TinyDB("tournoi_bdd.json")
    tournoi = tournoi_bdd.table("tournoi_bdd")
    return tournoi