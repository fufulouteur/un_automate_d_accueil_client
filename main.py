def acceillir():
    nom_visiteur = input('merci de contacter Minikea ! Je peux avoir votre prenom ? ').capitalize()
    print(f'Bienvenue chez minikea, {nom_visiteur}')
    return
def choisi_categ():
    print('*** Menu general MINIKEA *** \n[1] Horaires & acces \n[2] Gestion de commande \n[3] suivi de lavraison '
          '\n4 suggestion de produit \n[5] autre sujet ')
    cCatego = input('choisissez une des categories en tapant un chiffre entre 1 et 5 : ')

    if cCatego == '1':
        infos_boutique()
        return
    if cCatego == '2':
        gestion_commande()
        return
    if cCatego == '3':
        suivi_liraisons()
        return
    if cCatego == '4':
        service_marketing()
        return
    if cCatego == '5':
        autre()
        return
    if cCatego not in ['1', '2', '3', '4', '5']:
        choisi_categ()

def infos_boutue():
    adrph = "58 rue de Zwicheau 75011 PARIS"
    hora = 'du lundi au samidi 10h-18h'
    print(F'\nMinikea se trouve au {adrph}. \nLa boutique est ouverte {hora}.')
    cStopEncore = input('autre chose ? [o/n] ').lower()
    if cStopEncore == 'o':
        choisi_categ()
    else:
        print('Merci de nous avoir contacte.')
    return
def gestion_boutique():
    print('\nvous etre au service de guestion des commandes.')
    nom_client = input('nom indique sur le bon de commande : ')
    num_commande = input('Indiquez le numero de commande : ')
    transfert_Elliot()
    return
def suivi_livraisons():
    print("Nous sommes desole que vous avez subi un souci avec votre commande.")
    nom_client = input('non indique sur le bon de commande : ')
    num_commande = input('Indiquez le numero de commande : ')
    souci = ('Decrivez votre probleme : ')
    transfert_Christine()
    return