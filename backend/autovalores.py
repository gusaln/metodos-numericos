"""
Modulo de calculo de eigenvalues o autovectores.


Las matrices se expresan como listas de filas
"""

from vectores import vadd, vprod_k, vprod_dot, mprod_cross
from fastapi.logger import logger


def calcular_autovalor(A):
    """Calcula el autovalor de una matriz usando el método de las potencias"""
    x, y = len(A[0]), len(A)
    if x != y:
        raise ValueError("La matriz no es cuadrada.")

    v = [None] * x

    for i in range(x):
        v[i] = sum(A[i])

    for i in range(0, 8):
        p = max(map(abs, v))
        b = list(vprod_k(1/p, v))
        v = list(mprod_cross(A, b))

    return max(map(abs, v))


if __name__ == '__main__':
    from pprint import pprint

    B = [
        [3.556, -1.778, 0],
        [-1.778, 3.556, -1.778],
        [0, -1.778, 3.556],
    ]

    autovalor = calcular_autovalor(B)

    pprint(B)
    pprint(autovalor)
