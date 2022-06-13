"""
○ Énoncé
■ Écrivez un programme qui trouvera tous les nombres divisibles par 7
mais non multiples de 5 et 2,
entre 700 et 1099 (les deux inclus).Les nombres obtenus doivent être
imprimés dans une liste.
■ Affichez le nombre des nombres obtenus
"""

liste = list(range(700,1100))
liste_final = []
for nombre in liste:
    if nombre%7==0:
        if nombre%5 ==0 or nombre%2==0:
            pass 
        else:
            liste_final.append(nombre)

print(liste)
print('-----------------------------------------------------------------------------------')
print(liste_final)
print('-----------------------------------------------------------------------------------')
print(len(liste_final))
       
