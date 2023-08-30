from model import ModeloProductos

class ControladorProductos:
    def __init__(self):
        self.modelo = ModeloProductos()

    def agregar_producto(self, codigo, nombre, precio, stock):
        self.modelo.agregar_producto(codigo, nombre, precio, stock)

    def listar_productos(self):
        return self.modelo.listar_productos()

    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()
