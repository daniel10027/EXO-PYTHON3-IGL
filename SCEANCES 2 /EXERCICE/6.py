"""
○ Énoncé
■ La liste suivante représenta les moyennes d’une classe
■ moyennes=[14.84,14.14,16.22,86,85,85,14.84,13,15.85,9.99,12.04,1
5.03,16.22,12,84,10.20,11.03,11.03]
■ Afficher les trois bonnes moyennes
■ Afficher les trois mauvaises moyennes (triées de plus petites
au plus grandes)
"""

moyennes=[14.84,14.14,16.22,86,85,85,14.84,13,15.85,9.99,12.04,15.03,16.22,12,84,10.20,11.03,11.03]
moyennes.sort(reverse=True)
print(moyennes[:3])
moyennes.sort()
print(moyennes[:3])