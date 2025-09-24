from euclide import pgcd


def test_pgcd_1er_arg_1():
    a = 1
    b = 5
    g = pgcd(a, b)
    assert g == 1

def test_pgcd_2e_arg_1():
    a = 5
    b = 1
    g = pgcd(a, b)
    assert g == 1

def test_pgcd_2_arg_1():
    a = 1
    b = 1
    g = pgcd(a, b)
    assert g == 1

def test_pgcd_a_greater_than_b():
    a = 16
    b = 12
    g = pgcd(a, b)
    assert g == 4

def test_pgcd_b_greater_than_a():
    a = 12
    b = 16
    g = pgcd(a, b)
    assert g == 4