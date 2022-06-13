"""
■ Écrire un programme Python qui permet de :
■ Demander à l’utilisateur de saisir une liste d’entiers (en cas
d’erreur le programme redemande la saisie sans être planté),
la liste sera imprimé devant l’utilisateur chaque fois qu’il réussi
d’ajouter un élément à la liste.
■ Compter le nombre des éléments dupliqués de la liste.
■ Supprimer les éléments dupliqués de la liste et afficher la
nouvelle liste.
"""


def supprimeDoublon(liste):
    secondListe = []
    for nombre in liste:
        if nombre in secondListe:
            pass 
        else:
            secondListe.append(nombre)
    return secondListe


print('Veuillez saisir un nombre....')
listedenombre = []
while True:
    entier = input('Veuillez saisir un nombre : ')
    if entier:
        try:
            listedenombre.append(int(entier))
        except ValueError:
            continue
    else:
        break
print(supprimeDoublon(listedenombre))