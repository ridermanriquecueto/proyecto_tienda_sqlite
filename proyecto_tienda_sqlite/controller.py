from model import BaseDatosProductos

class ControladorProductos:
    def ___init___(self):
        self.base_datos = BaseDatosProductos()

    def agregar_producto(self, codigo, nombre, precio, stock):
        self.base_datos.agregar_producto(codigo, nombre, precio, stock)

    def listar_productos(self):
        return self.base_datos.listar_productos()

    def cerrar_base_datos(self):
        self.base_datos.cerrar()
