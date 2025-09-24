# tests unitaires avec:
# - factorisation des cas
# - cas d'erreurs

import pytest
from euclide import pgcd


@pytest.mark.parametrize(
        "a, b, expected_gcd",
        [
            (1, 1, 1),
            (1, 5, 1),
            (5, 1, 1),
            (12, 16, 4),
            (16, 12, 4),
            (1_836_311_903, 1_134_903_170, 1)
        ],
        ids = [
            "when_both_1",
            "when_first_1",
            "when_second_1",
            "when_a_greater_than_b",
            "when_b_greater_than_a",
            "when_iterate_a_lot",
        ]
)
def test_pgcd_ok(a, b, expected_gcd):
    assert expected_gcd == pgcd(a, b)


@pytest.mark.parametrize(
        "a, b",
        [
            (0, 1),
            (1, 0),
            (0, 0),
            (-1, 1),
            (1, -1),
            (-1, -1),
        ]
)
def test_pgcd_ko(a, b):
    with pytest.raises(ValueError):
        pgcd(a, b)