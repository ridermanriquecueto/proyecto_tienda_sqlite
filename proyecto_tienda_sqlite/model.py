import sqlite3

class BaseDatosProductos:
    def ___init___(self):
        self.conexion = sqlite3.connect("productos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS productos (codigo TEXT PRIMARY KEY, nombre TEXT, precio REAL, stock INTEGER)")
        self.conexion.commit()

    def agregar_producto(self, codigo, nombre, precio, stock):
        self.cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (codigo, nombre, precio, stock))
        self.conexion.commit()

    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        return rows

    def cerrar(self):
        self.conexion.close()
