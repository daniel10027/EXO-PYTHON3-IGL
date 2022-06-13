"""
○ Énoncé
■ Écrire un programme qui demande à l’utilisateur de saisir une liste
d’entiers, puis à l’aide de parcours successifs de la liste effectuer les
actions suivantes :
■ Afficher la liste
■ Afficher la liste en colonne de manière à afficher l’index et sont
contenu
■ Additionner tous les éléments de la liste.
■ Créer une nouvelle liste qui sera le multiple (3) de tous les
éléments de la liste.
■ Obtenir le plus grand nombre de la liste.
■ Obtenir le plus petit nombre de la liste.
■ Compter le nombre des nombres pairs présents dans la liste
■ Calculer la somme de tous les nombres impairs de la liste
"""

print('Veuillez saisir un nombre....')
listedenombre = []
while True:
    entier = input('Veuillez saisir un nombre : ')
    if entier:
        listedenombre.append(int(entier))
    else:
        break
print('La liste est : ',listedenombre)
print(listedenombre)

position = []
for nombre in listedenombre:
    position.append(listedenombre.index(nombre))
print(position)

somme = 0
for nombre in listedenombre:
    somme = somme + nombre 
print(somme)

liste_multiple = [i*3 for i in listedenombre]
print(liste_multiple)
print('Le plus grandn element est : ',max(listedenombre))
print('Le plus petit element est : ',min(listedenombre))


nombrePair = 0
for nombre in listedenombre:
    if nombre%2==0:
        nombrePair=nombrePair+1
print('Le nombre de nombres pairs est :', nombrePair)


SommeImpair = 0
for nombre in listedenombre:
    if nombre%2!=0:
        SommeImpair=SommeImpair+nombre
print('La somme  desnombres impairs est :', SommeImpair)