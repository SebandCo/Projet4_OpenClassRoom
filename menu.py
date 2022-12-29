# Logo de démarrage
print("\
===========================================\n\
      Logiciel de tournois d'Echec\n\
===========================================\n\n")

# Menu de selection pour l'utilisateur
print("Que souhaitez vous faire?")
print("\
1 --> Ajout d'un nouveau joueur\n\
2 --> Création d'un nouveau tournoi\n\
3 --> Revoir un tournoi\n\
4 --> Sortir du programme")

# Récupération du choix de l'utilisateur
reponse_menu=input("Merci de saisir le numéro de menu : ")
# Initialisation du controle de valeur de reponse_menu
reponse_correct=0

while reponse_correct==0:# Tant que le controle n'est pas valide
    try:
        # Vérifie si reponse_menu est un entier
        int(reponse_menu) 
        reponse_menu=int(reponse_menu)# Met le string en integer
        # Vérifie que reponse_menu est compris entre 1 et 4
        if 1<=reponse_menu<=4:
            reponse_correct=1 # Valide le controle pour sortir de la boucle
            reponse_menu=int(reponse_menu)# Met le string en integer
        else:
            # Si reponse_menu n'est pas compris entre 1 et 4
            reponse_menu=input("Merci de choisir un menu existant : ")
    except:
        # Si reponse_menu n'est pas un entier
        reponse_menu=input("Merci de choisir un menu existant : ")

# Redirection en fonction du choix de l'utilisateur
if reponse_menu==1:
    print ("Vous avez choisi le menu 1")
elif reponse_menu==2:
    print ("Vous avez choisi le menu 2")
elif reponse_menu==3:
    print ("Vous avez choisi le menu 3")
elif reponse_menu==4:
    print ("A une prochaine fois")

