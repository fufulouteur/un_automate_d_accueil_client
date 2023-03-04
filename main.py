def acceillir():
    nom_visiteur = input('merci de contacter Minikea ! Je peux avoir votre prenom ? ').capitalize()
    print(f'Bienvenue chez minikea, {nom_visiteur}')
    return
def choisi_categ():
    print('*** Menu general MINIKEA *** \n[1] Horaires & acces \n[2] Gestion de commande \n[3] suivi de lavraison '
          '\n4 suggestion de produit \n[5] autre sujet ')
    cCatego = input('choisissez une des categories en tapant un chiffre entre 1 et 5 : ')

    if cCatego == '1':
        infos_boutique = ()
        return