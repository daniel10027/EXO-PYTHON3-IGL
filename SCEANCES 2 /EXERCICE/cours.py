stock = ["Ordinateur de bureau", "Ordinateur portable", 100,"Caméra",310.28,"Haut-parleurs", 27.00,"Télévision",1000,"Cartes mères","souris","clavier",500,"barrettes de mémoire"]
for element in stock:
    if type(element)==str:
        print('{} est une chaine de charactere'.format(element))
    elif type(element)==int:
        print('{} est un entier'.format(element))
    else:
        print('{} est un nombre à virgule'.format(element))

