"""
Modulo de resolución de ecuaciones lineales.


Las matrices se expresan como listas de filas.
"""


from vectores import vadd, vprod_k, vprod_dot


def calcular_gauss(A, v):
    """Calcula la solución de un sistema de ecuaciones utilizando la eliminación Gaussiana"""
    A_reducida = list(A)
    v_reducida = list(v)

    n = len(A)
    # Volvemos la matriz triangular
    for i in range(n):
        a_i = A_reducida[i]
        a_ii = a_i[i]
        for j in range(i+1, n):
            a_j = A_reducida[j]
            a_ji = a_j[i]
            factor = - a_ji/a_ii
            A_reducida[j] = list(vadd(a_j, vprod_k(factor, a_i)))
            v_reducida[j] += factor * v_reducida[i]

    # Llenamos el vector de resultados con ceros
    incognitas = [0] * n

    # Calculamos los valores de cada incognita desde la última fila hacia la primera.
    incognitas[n-1] = v_reducida[n-1] / A_reducida[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum_i = 0
        for j in range(i+1, n):
            sum_i += A_reducida[i][j]*incognitas[j]

        incognitas[i] = (v_reducida[i] - sum_i)/A_reducida[i][i]

    return A_reducida, v_reducida, incognitas


if __name__ == '__main__':
    from pprint import pprint

    A, v, x = calcular_gauss(
        [
            [5.76, 9.95, 7.35, 9.05],
            [-2.56, -1.25, -3.06, 8.04],
            [-1.44, -5.25, 2.81, -6.23],
            [-1.22, -8.88, 2.11, -1.21]
        ],
        [0.41, -4.17, -1.5, -5.47],
    )

    pprint(A)
    pprint(v)
    pprint(x)
    print("Debería ser", [0.34899076,  0.54208124, -0.37690125, -0.46670397])
