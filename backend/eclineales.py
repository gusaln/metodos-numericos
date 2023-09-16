"""
Modulo de resolución de ecuaciones lineales.


Las matrices se expresan como listas de filas.
"""


from vectores import vadd, vprod_k, vprod_dot


def calcular_gauss(A, v):
    """Calcula la solución de un sistema de ecuaciones utilizando la eliminación Gaussiana"""
    A_respuesta = list(A)
    v_respuesta = list(v)

    n = len(A)
    for i in range(n):
        a_i = A_respuesta[i]
        a_ii = a_i[i]
        for j in range(i+1, n):
            a_j = A_respuesta[j]
            a_ji = a_j[i]
            factor = - a_ji/a_ii
            A_respuesta[j] = list(vadd(a_j, vprod_k(factor, a_i)))
            v_respuesta[j] += factor * v_respuesta[i]

    k = n-1
    factor = 1/A_respuesta[k][k]
    A_respuesta[k] = list(vprod_k(factor, A_respuesta[k]))
    v_respuesta[k] = factor * v_respuesta[k]

    incognitas = list(v_respuesta)
    for i in range(2, n+1):
        x = 2 * incognitas[-i]
        incognitas[-i] = x - vprod_dot(A_respuesta[-i], incognitas)

    return A_respuesta, v_respuesta, incognitas


if __name__ == '__main__':
    from pprint import pprint

    A, v, r = calcular_gauss(
        [
            [1, 1, -1],
            [0, 1, 3],
            [-1, 0, -2],
        ],
        [9, 3, 2],
    )

    pprint(A)
    pprint(v)
    pprint(r)
