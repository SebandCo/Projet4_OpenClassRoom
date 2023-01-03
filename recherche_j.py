# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query, where
from pprint import pprint

def recherche_joueur(reponse_recherche, mot_recherche):
    joueurs_bdd = TinyDB("joueurs_bdd.json")
    joueur_aj = joueurs_bdd.table("joueur_aj")
    resultat_joueur = Query()
    #Regarde si le joueur avec le classement en argument existe
    joueur_trouve=joueur_aj.search(where(reponse_recherche) == mot_recherche)
    #Si la réponse est vide, ne retourne rien
    if len(joueur_trouve) == 0:
        return ()
    #Sinon renvoi la position
    else:
        return (joueur_trouve)
    #Sinon c'est que le classement n'est pas défini

        #Demande à l'utilisateur le nom recherché
        mot_recherche=input("Quel joueur recherché vous? : ")
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