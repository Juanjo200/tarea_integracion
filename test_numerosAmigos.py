import pytest
from numerosAmigos import numeros_amigos


@pytest.mark.parametrize(
    "in_x,in_y,result",
    [
        (220, 284, f"{220} y {284} son amigos"),
        (6, 6, f"{6} y {6} no son amigos"),
        (1184, 1210, f"{1184} y {1210} son amigos"),
        (2620, 2924, f"{2620} y {2924} no son amigos"),
        (5020, 5564, f"{5020} y {5564} son amigos"),
        (10, 20, f"{10} y {20} son amigos"),
        (40, 55, f"{40} y {55} no son amigos"),
        (78, 90, f"{78} y {90} son amigos"),
        (110, 120, f"{110} y {120} no son amigos"),
        (20, 35, f"{20} y {35} son amigos"),
    ]
)
def test_numeros_amigos_param(in_x, in_y, result):
    assert numeros_amigos(in_x, in_y) == result
