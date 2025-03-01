# Definición de la matriz bidimensional
matriz = [
    [3, 1, 2],
    [9, 5, 6],
    [4, 8, 7]
]


# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila):
    # Asegurarse de que la fila esté dentro del rango
    if fila < 0 or fila >= len(matriz):
        print("Índice de fila fuera de rango.")
        return

    # Implementación del algoritmo Bubble Sort
    for i in range(len(matriz[fila])):
        for j in range(0, len(matriz[fila]) - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]


# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 1 (segunda fila, índice 1)
ordenar_fila(matriz, 1)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)
