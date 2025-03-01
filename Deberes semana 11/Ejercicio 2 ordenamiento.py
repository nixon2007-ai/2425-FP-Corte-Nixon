def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar

def ordenar_fila(matriz, fila_index):
    if 0 <= fila_index < len(matriz):
        bubble_sort(matriz[fila_index])
    else:
        print("Índice de fila no válido.")

# Definición de la matriz 3x3
matriz = [
    [9, 2, 5],
    [4, 8, 1],
    [6, 3, 7]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Solicitar al usuario el índice de la fila a ordenar
fila_a_ordenar = int(input("Introduce el índice de la fila a ordenar (0-2): "))

# Llamada a la función para ordenar la fila
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
