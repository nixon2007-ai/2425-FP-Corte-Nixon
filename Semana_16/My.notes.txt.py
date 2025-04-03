# Escritura de Archivo de Texto

# Abrimos (o creamos) el archivo my_notes.txt en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Nota 1: Sacar la ropa de la lavadora.\n")
    file.write("Nota 2: Comprar ingredientes para la cena.\n")
    file.write("Nota 3: Llamar a mamá.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo my_notes.txt en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # Usamos strip() para eliminar saltos de línea

# No es necesario cerrar el archivo manualmente al usar 'with', ya que se cierra automáticamente.