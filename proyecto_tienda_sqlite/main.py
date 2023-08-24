from controller import ControladorProductos

def main():
    controlador = ControladorProductos()

    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            controlador.agregar_producto(codigo, nombre, precio, stock)
            print("Producto agregado con éxito.")
        elif opcion == "2":
            print("Lista de productos:")
            productos = controlador.listar_productos()
            for producto in productos:
                print(producto)
        elif opcion == "3":
            print("Cerrando la base de datos y saliendo del programa.")
            controlador.cerrar_base_datos()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
 main()
