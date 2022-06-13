"""
○ Énoncé
■ Écrire une fonction supprimeDoublon(liste) qui supprime les doublons
d’une liste saisie par l’utilisateur.
■ Si l’utilisateur à saisie la liste suivante: ([3,4,5,3,4,5,1]) l’appel de la
fonction renvoie [3,4,5,1].
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
        listedenombre.append(int(entier))
    else:
        break
print(supprimeDoublon(listedenombre))

