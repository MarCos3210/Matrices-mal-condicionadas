import numpy as np

# Función que calcula la matriz inv(a) * b, el determinante de a, la condicional de a y a * inv(a)
def matriz_operaciones(a, b):
    if a.shape[0] != a.shape[1]:
        raise ValueError("La matriz a debe ser cuadrada para calcular la inversa.")
    
    # Calcular el determinante de a
    determinante = np.linalg.det(a)
    
    if determinante == 0:
        raise ValueError("La matriz a es singular y no tiene inversa.")
    
    # Calcular la matriz inversa de a
    a_inv = np.linalg.inv(a)
    
    # Multiplicar la matriz inversa de a por la matriz b
    resultado = np.dot(a_inv, b)
    
    # Calcular la condicional de la matriz a
    condicional = np.linalg.cond(a)
    
    # Calcular a * inv(a) para mostrar la matriz identidad
    identidad = np.dot(a, a_inv)
    
    return resultado, determinante, condicional, identidad

# Ejemplo de uso con matrices 3x3
a = np.array([[2, 4, 5],
              [6, 9, 8],
              [4.2, 5, 3]])

b = np.array([220,
              490,
              274])

resultado, determinante, condicional, identidad = matriz_operaciones(a, b)

print("Matriz inv(a) * b:")
print(resultado)
print("\nDeterminante de a:")
print(determinante)
print("\nCondicional de a:")
print(condicional)
print("\nMatriz identidad (a * inv(a)):")
print(identidad)
