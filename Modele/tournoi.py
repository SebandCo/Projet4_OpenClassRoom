# -*- coding: utf-8 -*-
from Controleur.bdd_json import initialisation_bdd_tournoi
from Controleur.bdd_json import recherche_bdd_position
from Controleur.bdd_json import suppression_item_bdd
from Controleur.valeur_menu import ctrl_valeur_menu
from Controleur.valeur_menu import ctrl_valeur_utilisateur
from datetime import datetime
from random import randint
from Vue.menu_nouveau_tournoi import vue_choix_type_partie
from Vue.menu_nouveau_tournoi import vue_tournoi_recuperation_score
"""
    Classe objet qui permet de stocker les informations d'un tournoi
    Permet aussi de suivre le déroulement d'un tournoi
    - nom : Nom du tournoi (aucune restriction)
            Par défault : "Tournoi du {date du jour}"
    - lieu : Lieu du tournoi (aucune restriction)
    - date : Date du tournoi (aucune restriction)
             Par défault : "{Date du jour}"
    - nbr_tour : Nombre de manche du tournoi (nombre entier positif non nul)
                 Par défault : 4
    - tour_actif : Manche actuellement en cours ou prochaine manche à jouer
                   Non modifiable par l'utilisateur
    - tournee : Paramêtre demandé par l'énoncé mais ne sert à rien
    - nbr_joueur : Nombre de joueur participant au tournoi (nombre entier positif pair)
                   Par défault : 8
    - joueurs : Parametre contenant les objets joueurs participant au tournoi
    - ctrl_temps : Type de tournoi. Aucune incidence sur le tournoi
                   (Valeur possible "Bullet", "Blitz", "Coup rapide")
    - description : Description facultative du tournoi (aucune restriction)
    - status : Donne l'état du tournoi ("En cours" ou "Terminé")
               Non modifiable par l'utilisateur
    - round : Met en mémoire la liste des duels prévus dans le round en cours
              Non modifiable par l'utilisateur
    - round_global : Met en mémoire la liste de tous les duels déjà joués afin d'éviter les doublons
              Non modifiable par l'utilisateur
    - position : Position du joueur dans la base Json. Défini par la fonction
                 Non modifiable par l'utilisateur

"""


class Tournoi:
    # Permet de créer un tournoi
    def __init__(self,
                 nom="",
                 lieu="",
                 date="",
                 nbr_tour=4,
                 tour_actif=1,
                 tournee="",
                 nbr_joueur=8,
                 joueurs="",
                 ctrl_temps="",
                 description="",
                 status="En cours",
                 round={},
                 round_global=[],
                 position=0):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbr_tour = nbr_tour
        self.tour_actif = tour_actif
        self.tournee = tournee
        self.nbr_joueur = nbr_joueur
        self.joueurs = joueurs
        self.ctrl_temps = ctrl_temps
        self.description = description
        self.status = status
        self.round = round
        self.round_global = round_global
        self.position = position

    # Méthode pour compiler l'ensemble des étapes de création d'un tournoi
    # Renvoi un objet tournoi crée
    def creation_tournoi(self):
        self.date = self.generate_date()
        self.nom = self.generate_nom()
        self.lieu = self.generate_lieu()
        self.nbr_tour = self.generate_nbr_tour()
        self.tournee = self.generate_tournee()
        self.nbr_joueur = self.generate_nbr_joueur()
        self.joueurs = self.generate_joueurs()
        self.ctrl_temps = self.generate_ctrl_temps()
        self.description = self.generate_description()
        self.position = self.generate_position()

    # Méthode pour demander la date du tournoi
    # Renvoie le texte saisie par l'utilisateur ou par défaut la date du jour
    def generate_date(self):
        # Par défaut met la date du jour
        self.date = (datetime.today().strftime("%d-%m-%Y"))
        print(f"\nLe tournoi a t'il lieu aujourd'hui le {self.date} ?")
        date_tournoi = input("Si oui, merci de valider. Sinon mettre la nouvelle date : ")
        # Si la valeur saisie par l'utilisateur n'est pas vide alors on la remplace
        if len(date_tournoi) != 0:
            self.date = date_tournoi
        return self.date

    # Méthode pour demander le nom du tournoi
    # Renvoie le nom saisie par l'utilisateur ou par défaut "Tournoi du date du jour"
    def generate_nom(self):
        # Par défaut met "Tournoi du" suivi de la date du jour
        self.nom = (f"Tournoi du {self.date}")
        print(f"\nUn nom possible du tournoi est : {self.nom}")
        nom_tournoi = input("Si le nom vous satisfait, merci de valider. Sinon mettre le nouveau nom : ")
        # Si la valeur saisie par l'utilisateur n'est pas vide alors on la remplace
        if len(nom_tournoi) != 0:
            self.nom = nom_tournoi
        return self.nom

    # Méthode pour demander le lieu du tournoi
    # Renvoie le lieu saisie par l'utilisateur
    def generate_lieu(self):
        self.lieu = input("\nMerci de saisir le lieu du tournoi : ")
        return self.lieu

    # Méthode pour trouver un numéro de position non utilisé dans la base de donnée json
    # Renvoie le premier numéro de position non utilisé
    def generate_position(self):
        bdd_tournoi = initialisation_bdd_tournoi()
        self.position = recherche_bdd_position(bdd_tournoi)
        return self.position

    # Méthode pour demander le nombre de tour du tournoi
    # Renvoie le nombre saisie par l'utilisateur ou la valeur de l'__init__ par défaut
    def generate_nbr_tour(self):
        print(f"\nEst ce que le tournoi va se dérouler en {self.nbr_tour} tour ?")
        nbr_tour_tournoi = input(f"Si il se déroule en {self.nbr_tour} tours, merci de valider."
                                 f"Sinon mettre le nombre de tour : ")
        # Si la valeur saisie par l'utilisateur n'est pas vide alors on la remplace
        if len(nbr_tour_tournoi) != 0:
            nbr_tour_tournoi = ctrl_valeur_utilisateur(nbr_tour_tournoi)
            self.nbr_tour = nbr_tour_tournoi
        return self.nbr_tour

    # Méthode pour demander le nombre de joueur
    # Renvoie le nombre pair saisie par l'utilisateur ou la valeur de l'__init__ par défaut
    def generate_nbr_joueur(self):
        nbr_joueur = input("\nMerci de dire combien de joueur participerons au tournoi : ")
        controle = False
        # Si la valeur saisie par l'utilisateur n'est pas vide alors on la remplace
        while controle is False:
            # A condition que la saisie utilisateur soit un nombre
            if nbr_joueur != self.nbr_joueur:
                nbr_joueur = ctrl_valeur_utilisateur(nbr_joueur)
                # Et a condition que le nombre soit positif (divisible par 0)
                if (nbr_joueur % 2) == 0:
                    self.nbr_joueur = nbr_joueur
                    controle = True
                else:
                    nbr_joueur = input("Merci de rentrer un nombre de joueur pair : ")
        return self.nbr_joueur

    # Méthode pour demander la tournée ????
    # Ne renvoi rien car pas d'utiliter apparente
    def generate_tournee(self):
        pass

    # Méthode pour demander les joueurs participants au tournoi
    def generate_joueurs(self):
        self.joueurs = {}
        return self.joueurs

    # Méthode pour demander le type de jeu
    # Renvoie le type saisie par l'utilisateur
    def generate_ctrl_temps(self):
        menu_max = 3
        # Demande à l'utilisateur le nom du tournoi
        reponse_temps = vue_choix_type_partie()
        self.ctrl_temps = ctrl_valeur_menu(menu_max, reponse_temps)
        # Suivant la réponse de l'utilisateur affecte le type de partie
        if self.ctrl_temps == 1:
            self.ctrl_temps = "Blitz"
        elif self.ctrl_temps == 2:
            self.ctrl_temps = "Bullet"
        else:
            self.ctrl_temps = "Coup rapide"
        return self.ctrl_temps

    # Méthode pour demander la description du tournoi
    # Renvoie le texte saisie par l'utilisateur
    def generate_description(self):
        self.description = input("\nSouhaitez vous rajouter une description : ")
        return self.description

    # Méthode pour demander sauvegarder l'ensemble des duels effectués
    # Renvoie le round actuel dans le round global
    def generate_round_global(self):
        round_actuel = (f"Round {self.tour_actif}")
        self.round_global.append(self.round[round_actuel])

    # Méthode pour ajouter un tournoi dans la base de donnée json
    # Ne renvoi rien, mais rajoute le tournoi à la base de donnée json
    def ajout_tournoi_bdd(self):
        bdd_tournoi = initialisation_bdd_tournoi()
        # Transforme les objets JoueurTournoi en dictionnaire pour  mettre en json
        dico_global_joueurs = {}
        dico_joueur = {}
        for joueur in self.joueurs:
            dico_joueur = {}
            dico_joueur["nom"] = self.joueurs[joueur].nom
            dico_joueur["prenom"] = self.joueurs[joueur].prenom
            dico_joueur["naissance"] = self.joueurs[joueur].naissance
            dico_joueur["sexe"] = self.joueurs[joueur].sexe
            dico_joueur["classement"] = self.joueurs[joueur].classement
            dico_joueur["position"] = self.joueurs[joueur].position
            dico_joueur["couleur"] = self.joueurs[joueur].couleur
            dico_joueur["paires"] = self.joueurs[joueur].paires
            dico_joueur["points"] = self.joueurs[joueur].points
            dico_joueur["ordre"] = self.joueurs[joueur].ordre
            dico_global_joueurs[joueur] = dico_joueur

        bdd_tournoi.insert({"nom": self.nom,
                            "lieu": self.lieu,
                            "date": self.date,
                            "nbr_tour": self.nbr_tour,
                            "tour_actif": self.tour_actif,
                            "tournee": self.tournee,
                            "nbr_joueur": self.nbr_joueur,
                            "joueurs": dico_global_joueurs,
                            "ctrl_temps": self.ctrl_temps,
                            "description": self.description,
                            "status": self.status,
                            "round": self.round,
                            "round_global": self.round_global,
                            "position": self.position})

    # Méthode pour sauvegarder un tournoi dans la base de donnée json
    # Ne renvoi rien, mais met à jour le tournoi dans la base de donnée json
    def sauvegarde_tournoi_bdd(self):
        bdd_tournoi = initialisation_bdd_tournoi()
        # Supprime le tournoi existant
        suppression_item_bdd(bdd_tournoi, "position", self.position)
        # Le remplace par le nouveau tournoi
        self.ajout_tournoi_bdd()

    # Méthode pour créer l'ordre des duels du premier tour
    # Affilie à la classe joueur l'ordre des duels
    def ordre_tour(self):
        liste_croissant = []
        # Classe la liste des valeurs de classement par ordre croissant
        for participant in self.joueurs:
            liste_croissant.append(self.joueurs[participant].points)
            liste_croissant.sort(reverse=True)
            # Remet à 0 l'ordre des joueurs
            self.joueurs[participant].ordre = ""

        # Donne l'ordre aux objet participant
        # Initialise le premier
        ordre = 1
        # Balaie la liste des nombres
        for nombre in liste_croissant:
            # Balaie la liste des joueurs
            for participant in self.joueurs:
                # Si un nombre est identique au classement. C'est le bon joueur
                if nombre == self.joueurs[participant].points:
                    # En cas de classement identique, affilie au premier joueur sans ordre
                    if self.joueurs[participant].ordre == "":
                        self.joueurs[participant].ordre = ordre
                        ordre += 1
        return

    # Méthode pour lancer le premier tour
    def creation_premier_tour(self):
        self.ordre_tour()
        self.creation_premiere_paire()
        self.round_global = []
        self.generate_round_global()

    # Méthode pour lancer les tours suivant
    def creation_tour(self):
        self.remise_a_zero()
        self.ordre_tour()
        self.creation_paire()
        self.generate_round_global()

    # Permet de remettre à zero les couleurs et paires des joueurs
    def remise_a_zero(self):
        for participant in self.joueurs:
            self.joueurs[participant].paires = ""
            self.joueurs[participant].couleur = ""

    # Permet de mettre la liste des rounds sous forme d'une liste
    def transformation_round_en_liste(self):
        liste_round_global = []
        for rang in self.round_global:
            for element in rang:
                liste_round_global.append(element)
        return liste_round_global

    # Permet d'affecter les couleurs à l'un des joueurs
    def affectation_couleur_concurrent(self, nbr_aleatoire, participant):
        if nbr_aleatoire == 1:
            self.joueurs[participant].couleur = "blancs"
        else:
            self.joueurs[participant].couleur = "noirs"

    # Permet d'affecter les couleurs à l'autre joueurs
    def affectation_couleur_adversaire(self, nbr_aleatoire, participant):
        if nbr_aleatoire == 1:
            self.joueurs[participant].couleur = "noirs"
        else:
            self.joueurs[participant].couleur = "blancs"

    # Permet de créer les paires de duel
    def creation_paire(self):
        numero_de_paires = 1
        round_actuel = (f"Round {self.tour_actif}")
        self.round[round_actuel] = []
        duel = ""
        # Création d'une liste comportant le rang des joueurs
        liste_rang_joueur = []
        nombre = 1
        while nombre <= self.nbr_joueur:
            liste_rang_joueur.append(nombre)
            nombre += 1
        # Boucle tant que toutes les paires n'ont pas été affecté
        while numero_de_paires <= (self.nbr_joueur)/2:
            nbr_aleatoire = randint(1, 2)
            concurrent = False
            adversaire = False
            duel_valide = False
            rang_joueur = 0
            # Boucle tant que les deux joueurs n'ont pas été trouvé
            while concurrent is False or adversaire is False:
                for participant in self.joueurs:
                    if self.joueurs[participant].ordre == liste_rang_joueur[rang_joueur]:
                        if self.joueurs[participant].paires == "":
                            if concurrent is False:
                                self.joueurs[participant].paires = numero_de_paires
                                self.affectation_couleur_concurrent(nbr_aleatoire, participant)
                                concurrent = True
                                # Supprime le jour de la liste
                                liste_rang_joueur.pop(rang_joueur)
                                # Sauvegarde le début du duel
                                duel = (f"{participant} /")

                            else:
                                if adversaire is False:
                                    if rang_joueur < len(liste_rang_joueur):
                                        # Vérifie que le duel n'existe pas déjà
                                        duel_provisoire = (f"{duel} {participant}")
                                        liste_round_global = self.transformation_round_en_liste()
                                        # Si le duel existe, il est dans la liste
                                        try:
                                            liste_round_global.index(duel_provisoire)
                                            rang_joueur += 1
                                        # Sinon il n'y est pas et le duel est validé
                                        except ValueError:
                                            duel_valide = True
                                    # Sinon la liste des joueurs a été balayé et il n'y a pas mieux qu'un doublon
                                    else:
                                        duel_valide = True

                                    if duel_valide is True:
                                        self.joueurs[participant].paires = numero_de_paires
                                        self.affectation_couleur_adversaire(nbr_aleatoire, participant)
                                        adversaire = True
                                        # Supprime le jour de la liste
                                        liste_rang_joueur.pop(rang_joueur)
                                        # Valide le duel
                                        duel = (f"{duel} {participant}")
                                        break
                        else:
                            pass

            self.round[round_actuel].append(duel)
            numero_de_paires += 1
            duel = ""

    # Permet de demander à l'utilisateur les résultats des duels
    def recuperation_resultat(self):
        numero_de_paires = 1
        joueur1 = ""
        joueur2 = ""
        while numero_de_paires <= (self.nbr_joueur)/2:
            for participant in self.joueurs:
                if self.joueurs[participant].paires == numero_de_paires:
                    if joueur1 == "":
                        joueur1 = participant
                    else:
                        joueur2 = participant

            reponse_utilisateur = vue_tournoi_recuperation_score(numero_de_paires, joueur1, joueur2, self)

            # Nombre de menu possible
            menu_max_vainqueur = reponse_utilisateur[1]
            reponse_menu_vainqueur = reponse_utilisateur[0]

            reponse_utilisateur_vainqueur = ctrl_valeur_menu(menu_max_vainqueur, reponse_menu_vainqueur)
            if reponse_utilisateur_vainqueur == 1:
                self.joueurs[joueur1].points += 1
            elif reponse_utilisateur_vainqueur == 2:
                self.joueurs[joueur2].points += 1
            else:
                self.joueurs[joueur1].points += 0.5
                self.joueurs[joueur2].points += 0.5

            numero_de_paires += 1
            joueur1 = ""
            joueur2 = ""

    # Permet de créer les paires des premiers duel (méthode suisse)
    def creation_premiere_paire(self):
        numero_de_paires = 1
        duel = ""
        self.round["Round 1"] = []
        # Vérifie que nous sommes bien dans la première moitié
        while numero_de_paires <= (self.nbr_joueur)/2:
            nbr_aleatoire = randint(1, 2)
            concurrent = numero_de_paires
            adversaire = ((self.nbr_joueur)/2) + numero_de_paires

            for participant in self.joueurs:

                if self.joueurs[participant].ordre == concurrent:
                    self.joueurs[participant].paires = numero_de_paires
                    if nbr_aleatoire == 1:
                        self.joueurs[participant].couleur = "blancs"
                    else:
                        self.joueurs[participant].couleur = "noirs"
                    # Sauvegarde le duel ou le met à jour
                    if len(duel) == 0:
                        duel = (f"{participant} /")
                    else:
                        duel = (f"{duel} {participant}")

                elif self.joueurs[participant].ordre == adversaire:
                    self.joueurs[participant].paires = numero_de_paires
                    if nbr_aleatoire == 1:
                        self.joueurs[participant].couleur = "noirs"
                    else:
                        self.joueurs[participant].couleur = "blancs"
                    # Sauvegarde le duel ou le met à jour
                    if len(duel) == 0:
                        duel = (f"{participant} /")
                    else:
                        duel = (f"{duel} {participant}")

            self.round["Round 1"].append(duel)
            numero_de_paires += 1
            duel = ""

    # Permet d'afficher les duels à réaliser
    def affichage_adversaire(self, numero_paire):
        joueur1 = ""
        joueur2 = ""
        for participant in self.joueurs:
            if self.joueurs[participant].paires == numero_paire:
                if joueur1 == "":
                    joueur1 = self.joueurs[participant]
                else:
                    joueur2 = self.joueurs[participant]
        return (joueur1, joueur2)
