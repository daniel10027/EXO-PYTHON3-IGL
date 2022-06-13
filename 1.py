"""
2. Exercice 01
○ Énoncé
■ Écrire un programme python qui créé une liste semaine qui comprend
les jours de la semaine, puis à l’aide de parcours successifs de la liste
effectuer les actions suivantes :
■ Afficher la liste semaine
■ Afficher la valeur de semaine[4]
■ Échanger les valeurs de la première et de la dernière case de
cette liste
■ Afficher 12 fois la valeur du dernier élément de la liste
"""
semaine = ['Lundi','MArdi','Mercredi','Jeudi','Vendredi','SAmedi','Dimanche']
print('Lesjours de la semaine sont :', semaine)
print('Semaine[4] = ', semaine[4])
semaine[0] = 'Jour Changé'
semaine[-1] = 'Jour Changé'
print(semaine[-1]*12)