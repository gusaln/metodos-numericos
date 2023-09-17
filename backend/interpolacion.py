"""
Modulo de resolución de interpolación polinómica de Lagrange para estimar el valor de y en x_interp.
"""

def lagrange_interpolation(x, y, x_interp):
    """
    Realiza la interpolación polinómica de Lagrange para estimar el valor de y en x_interp.
    
    :param x: Lista de coordenadas x conocidas.
    :param y: Lista de coordenadas y conocidas correspondientes a x.
    :param x_interp: Valor de x en el cual se desea estimar y.
    :return: Estimación de y en x_interp.
    """
    n = len(x)
    if n != len(y):
        raise ValueError("Las listas x e y deben tener la misma longitud.")
    
    # Inicializa el valor interpolado
    y_interp = 0.0
    
    for i in range(n):
        # Calcula el término del polinomio de Lagrange
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_interp - x[j]) / (x[i] - x[j])
        # Agrega el término al valor interpolado
        y_interp += term
    
    return y_interp
  
# Ejemplo de como usar el algoritmo: => Descomentar a partir de la siguiente línea con ctrl+F4 para probar funcionalidad
##
### Datos conocidos
##x = [0.0, 1.0, 2.0, 3.0]
##y = [1.0, 2.0, 4.0, 8.0]
##
### Valor en el cual se desea estimar y
##x_interp = 1.5
##
### Realiza la interpolación
##y_interp = lagrange_interpolation(x, y, x_interp)
##
### Imprime el resultado
##print(f"Interpolación en x=%s: y=%s" % (str(x_interp), str(y_interp)) )
