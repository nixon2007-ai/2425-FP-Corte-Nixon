# Crear un diccionario con información personal
información_personal = {
    "nombre": "Dario",
    "edad": 25,
    "ciudad": "Nueva Loja",
    "profesión": "Abogado"
}

# Acceder y modificar la ciudad
información_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para "profesión"
información_personal["profesión"] = "Master penalista"

# Verificar existencia de la clave "telefono"
if "telefono" not in información_personal:
    información_personal["telefono"] = "394-546-4342"  # Corrección aquí

# Eliminar la clave "edad"
if "edad" in información_personal:
    del información_personal["edad"]

# Imprimir el diccionario Final
print(información_personal)