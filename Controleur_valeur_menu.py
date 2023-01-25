
def ctrl_valeur_menu(menu_max, reponse_menu):
    reponse_correct = 0

    # Tant que le controle n'est pas valide
    while reponse_correct == 0:
        try:
            # Vérifie si reponse_menu est un entier
            int(reponse_menu)
            # Met le string en integer
            reponse_menu = int(reponse_menu)
            # Vérifie que reponse_menu est compris entre 1 et 3
            if 1 <= reponse_menu <= menu_max:
                # Valide le controle pour sortir de la boucle
                reponse_correct = 1
            else:
                # Si reponse_menu n'est pas compris entre 1 et 3
                reponse_menu = input("Merci de choisir un menu existant : ")
        except:
            # Si reponse_menu n'est pas un entier
            reponse_menu = input("Merci de choisir un menu existant : ")
    reponse_menu = int(reponse_menu)
    return reponse_menu