# définition de fonction avec Hints ou Annotation Type
# depuis python 3.6

def pgcd(a: int, b: int) -> int:
    """ Calcule le plus grand commun diviseur des nombres entiers strictement positifs a et b

    Paramètres:
    - a : 1er entier (strictement positif)
    - b : 2ème entier (strictement positif)

    Renvoie: le pgcd

    Exceptions:
    - ValueError si a ou b sont négatifs ou nul
    """
    if a <= 0 or b <= 0:
        raise ValueError("Les arguments de pgcd doivent être strictement positifs")
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# g = pgcd(12, 16)
# print(g)