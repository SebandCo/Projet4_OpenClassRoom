# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query
from pprint import pprint

def recherche_joueur():
    joueurs_bdd = TinyDB("joueurs_bdd.json")
    joueur_aj = joueurs_bdd.table("joueur_aj")
    #Demande à l'utilisateur le nom recherché
    mot_recherche=input("Quel joueur recherché vous? : ")
    resultat_joueur = Query()
    #Recherche toutes les occurences du mot recherché
    joueur_trouve=joueur_aj.search(resultat_joueur.nom == mot_recherche)
    #Si la réponse est vide, l'indique à l'utilisateur
    if len(joueur_trouve) == 0:
        print("\n Aucun résultat n'a été trouvé")
    #Sinon affiche les resultats
    else:
        for resultat in joueur_trouve:
            pprint(resultat)
    #Pause pour permettre à l'utilisateur de lire le resultat
    input("\n Appuyer sur ""Entrée"" pour continuer")    