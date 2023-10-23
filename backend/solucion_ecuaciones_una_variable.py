#Si no tienes la librería sympy instalar con el siguiente comando -> pip install sympy
import sympy as sp

# Diccionario de operadores y funciones con descripciones
ayuda_operadores = {
    'a*b': 'Producto',
    'a+b': 'Suma',
    'a-b': 'Resta',
    'a/b': 'División',
    'a**b': 'Exponenciación',
    'sin(a)': 'Seno',
    'cos(a)': 'Coseno',
    'sqrt(a)': 'Raíz cuadrada',
    'ln(a)': 'Logaritmo natural',
    'log10(a)': 'Logaritmo en base 10',
    'exp(a)': 'Exponencial',
    'abs(a)': 'Valor absoluto',
    'sign(a)': 'Función signo'
}

# Mostrar la ayuda
def mostrar_ayuda():
    print("Operadores y funciones disponibles:")
    for operador, descripcion in ayuda_operadores.items():
        print(f"{operador} = {descripcion}")
        
def resolver_ecuacion(datos = True, ecuacion_str = ""):
    # Solicitar al usuario que ingrese una ecuación
    if datos:
        print("Introduce 'help' en cualquier momento para ver los operadores y funciones disponibles.")
        ecuacion_str = input("Ingresa una ecuación (por ejemplo, 'x**2 - 4'): ")
    
    if ecuacion_str.lower() == 'help':
        mostrar_ayuda()
        print("\n")
    else:
        try:
            # Convertir la entrada del usuario en una expresión simbólica
            ecuacion = sp.sympify(ecuacion_str)
            
            # Definir una variable simbólica
            x = sp.symbols('x')
            
            # Intentar resolver la ecuación
            soluciones = sp.solve(ecuacion, x)
            if len(soluciones) == 0:
                return "No se encontraron soluciones."
            if len(soluciones) == 1:
                print(f"Solución única: x = {soluciones[0]}")
                return soluciones[0]
            
            print(f"Soluciones múltiples:")
            for n, solucion in enumerate(soluciones):
                print(f"Solución {n+1}: {solucion}")
            return soluciones
        except Exception as e:
            print("La ecuación ingresada no es válida o no se pudo resolver. %s" % e)
            return None

# Ejemplo de uso
resultado = resolver_ecuacion(False, "x**2")#Se almacenan las soluciones posibles