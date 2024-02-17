import mysql.connector


# Datos de conexión
def date():
    host = "b2jvfbwwzwgru1w4egfx-mysql.services.clever-cloud.com"
    database = "b2jvfbwwzwgru1w4egfx"
    user = "umpbhpsayjpkxxrn"
    password = "MPQecUPZwyGfZ922o8wV"
    port = 3306


def connect():
    # Crear conexión
    try:
        connection = mysql.connector.connect(
            host=host, database=database, user=user, password=password, port=port
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
