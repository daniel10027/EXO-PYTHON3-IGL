"""
○ Énoncé
■ Soit la liste suivante:
stock = ["Ordinateur de bureau", "Ordinateur portable", 100,
"Caméra",310.28,"Haut-parleurs", 27.00,"Télévision",
1000,"Cartes mères","souris","clavier",500,"barrettes de
mémoire"]
■ Afficher la liste "stock"
■ ِCréer des listes séparées composées de chaînes et de
nombres.
■ Compter le nombre d’élément de chaque liste
■ Trier la liste de chaînes par ordre croissant
■ Trier la liste de chaînes par ordre décroissant
■ Trier la liste des numéros du plus petit au plus grand
■ Trier la liste des numéros du plus grand au plus petit
"""

stock = ["Ordinateur de bureau", "Ordinateur portable", 100,"Caméra",310.28,"Haut-parleurs", 27.00,"Télévision",1000,"Cartes mères","souris","clavier",500,"barrettes de mémoire"]
print(stock)
nombre = []
chaine = []
for valeur in stock:
    if type(valeur) == type(2) or type(valeur) == type(2.0):
        nombre.append(valeur)
    else:
        chaine.append(valeur)
print(chaine)
print(nombre)
print('Le nombre de chaine est : ', len(chaine))
print('Le nombre de nomnre est : ', len(nombre))

print(chaine)
chaine.sort()
print(chaine)
chaine.sort(reverse=True)
print(chaine)

print(nombre)
nombre.sort()
print(nombre)
nombre.sort(reverse=True)
print(nombre)