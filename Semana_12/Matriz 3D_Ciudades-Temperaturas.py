# Trabajo de la semana 12- Nixon Corte
# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (4 ciudades) del Ecuador
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   #   Ciudad 1-Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    [   # Ciudad 2-Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 15}
        ]
    ],
    [   # Ciudad 3-Lago Agrio
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [ # Ciudad 4-El Coca
[   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ]
    ]

]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["CIUDAD 1-QUITO", "CIUDAD 2-CUENCA", "CIUDAD 3-LAGO AGRIO", "CIUDAD 4-EL COCA"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"]
                                 for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")


# Pormedio de temperatura Ciudad 1
Promedio de temperaturas en CIUDAD 1-QUITO, Semana 1: 16.00 grados
Promedio de temperaturas en CIUDAD 1-QUITO, Semana 2: 15.86 grados
Promedio de temperaturas en CIUDAD 1-QUITO, Semana 3: 16.14 grados
Promedio de temperaturas en CIUDAD 1-QUITO, Semana 4: 16.00 grados

# Pormedio de temperatura Ciudad 2
Promedio de temperaturas en CIUDAD 2-CUENCA, Semana 1: 15.00 grados
Promedio de temperaturas en CIUDAD 2-CUENCA, Semana 2: 14.00 grados
Promedio de temperaturas en CIUDAD 2-CUENCA, Semana 3: 13.00 grados
Promedio de temperaturas en CIUDAD 2-CUENCA, Semana 4: 12.00 grados

# Pormedio de temperatura Ciudad 3
Promedio de temperaturas en CIUDAD 3-LAGO AGRIO, Semana 1: 31.00 grados
Promedio de temperaturas en CIUDAD 3-LAGO AGRIO, Semana 2: 30.00 grados
Promedio de temperaturas en CIUDAD 3-LAGO AGRIO, Semana 3: 29.00 grados
Promedio de temperaturas en CIUDAD 3-LAGO AGRIO, Semana 4: 28.00 grados

# Pormedio de temperatura Ciudad 4
Promedio de temperaturas en CIUDAD 4-EL COCA, Semana 1: 30.71 grados
Promedio de temperaturas en CIUDAD 4-EL COCA, Semana 2: 30.00 grados
Promedio de temperaturas en CIUDAD 4-EL COCA, Semana 3: 31.00 grados
Promedio de temperaturas en CIUDAD 4-EL COCA, Semana 4: 32.00 grados


