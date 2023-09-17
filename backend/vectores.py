"""
Modulo de operaciones vectoriales.
"""
from random import uniform, randint


def vrandom(n):
    """Genera un vector aleatorio con `n` elementos"""
    return [uniform(-10, 10) for _ in range(n)]


def mrandom(a, b=None):
    """Genera una matriz aleatorio con `a` columnas y `b` filas.

    Si :param:`b` es `None`, se realiza una matriz cuadrada.
    """
    if b is None:
        b = a
    return [vrandom(a) for _ in range(b)]


def vadd(x: list, y: list):
    """Suma dos vectores"""
    return (x_i + y_i for x_i, y_i in zip(x, y))


def vsub(x: list, y: list):
    """Resta dos vectores"""
    return (x_i - y_i for x_i, y_i in zip(x, y))


def vprod_dot(x: list, y: list) -> float:
    """Realiza el producto punto entre dos vectores"""
    return sum((x_i * y_i for x_i, y_i in zip(x, y)), 0.0)


def vprod_k(k, x: list):
    """Multiplica un vector por un escalar"""
    return (k * x_i for x_i in x)


def mprod_cross(A, x):
    """Realiza el producto cruz entre una matriz y un vector"""
    if x is not list:
        x = list(x)

    if len(A[0]) != len(x):
        raise ValueError(
            "La matriz A, no contiene el mismo número de filas que elementos en el vector x.")

    return [vprod_dot(a_x, x) for a_x in A]
