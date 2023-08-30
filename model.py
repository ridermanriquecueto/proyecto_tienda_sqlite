import sqlite3

class ModeloProductos:
    def __init__(self):
        self.conexion = sqlite3.connect("productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS productos (codigo TEXT, nombre TEXT, precio REAL, stock INTEGER)")
        self.conexion.commit()

    def agregar_producto(self, codigo, nombre, precio, stock):
        self.cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (codigo, nombre, precio, stock))
        self.conexion.commit()

    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conexion.close()

