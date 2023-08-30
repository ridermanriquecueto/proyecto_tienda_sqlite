from controller import ControladorProductos
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpiar_consola()
    print("Menú:")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Salir")

def main():
    controlador = ControladorProductos()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar_consola()
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            controlador.agregar_producto(codigo, nombre, precio, stock)
            print(f"Producto '{nombre}' agregado exitosamente.")

        elif opcion == "2":
            limpiar_consola()
            productos = controlador.listar_productos()
            print("Lista de productos:")
            for producto in productos:
                print(producto)

        elif opcion == "3":
            controlador.cerrar_conexion()
            limpiar_consola()
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
