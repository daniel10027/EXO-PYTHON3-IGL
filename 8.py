"""
○ Énoncé
■ Pour le code suivant quel est le résultat de chaque impression (print)
après exécution
numList = [1,2,3,4,5]
alphaList = ["a","b","c","d","e"]
print(numList is alphaList)
print(numList == alphaList)
numList = alphaList
print(numList is alphaList)
print(numList == alphaList)
"""
numList = [1,2,3,4,5]
alphaList = ["a","b","c","d","e"]
print(numList is alphaList)
print(numList == alphaList)

numList = alphaList

print(numList is alphaList)
print(numList == alphaList)