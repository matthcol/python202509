# Exemple de code incorrect vis à vis de la déclaration de type

villes: list[str] = ['Saint-Etienne', 'Bayonne', 'Rennes', 'Bordeaux', 'Montauban', 'La Rochelle']
print(villes)
villes[2] = ['Rennes', 'Bordeaux', 'Montauban']
print(villes)
villes[:2] = 'Saint-Remy-en-Bouzemont-Saint-Genest-et-Isson'
print(villes)
villes[0] = None
villes[1] = 123