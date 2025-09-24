from euclide import pgcd
# import euclide as eu


data = [
    (12, 16), (1_836_311_903, 1_134_903_170), (21, 13), 
    # ('M', 12)
]

for a, b in data:
    g = pgcd(a, b)
    # g = eu.pgcd(a, b)
    print(f"Le pgcd de {a} et {b} est {g}.")

# pgcd('M', 12)

# g + 'M'

# pgcd(0, 12)
# pgcd(5, -12)
pgcd(0, -12)