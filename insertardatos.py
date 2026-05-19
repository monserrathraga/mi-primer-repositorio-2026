import pymysql

conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="escuela"
)

cursor = conexion.cursor()

# Insertar usuarios
usuarios = [
    ("Juan Pérez", "juan@example.com"),
    ("María Gómez", "maria@example.com")
]
cursor.executemany("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", usuarios)

# Insertar pedidos
pedidos = [
    ("Laptop", 1, 1),   # usuario_id = 1 (Juan)
    ("Teléfono", 2, 2)  # usuario_id = 2 (María)
]
cursor.executemany("INSERT INTO pedidos (producto, cantidad, usuario_id) VALUES (%s, %s, %s)", pedidos)

conexion.commit()
cursor.close()
conexion.close()
print("Datos insertados correctamente.")
