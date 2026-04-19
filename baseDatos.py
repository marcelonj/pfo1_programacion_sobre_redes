import sqlite3
from datetime import datetime

class baseDatos ():
    def __init__(self):
        self.conexion = sqlite3.connect("mensajes_pfo1.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS mensajes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT,
                fecha_envio DATETIME,
                ip_cliente TEXT
            )
            '''
        )

    def __del__(self):
        self.conexion.close()

    def insertarRegistro(self, contenido, ip_cliente):
        fecha = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        ultima_fila = self.cursor.lastrowid
        self.cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?,?,?)",(contenido, fecha, ip_cliente))
        self.conexion.commit()

        exito = True if self.cursor.lastrowid > ultima_fila else False
        return (exito, fecha)