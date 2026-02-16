# main.py

from inventario import Inventario
from producto import Producto


def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:

            if opcion == "1":
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
                print("Producto añadido correctamente.")

            elif opcion == "2":
                id_producto = input("Ingrese el ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)
                print("Producto eliminado correctamente.")

            elif opcion == "3":
                id_producto = input("Ingrese el ID del producto a actualizar: ")

                cantidad = input("Nueva cantidad (dejar vacío si no desea modificar): ")
                precio = input("Nuevo precio (dejar vacío si no desea modificar): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
                print("Producto actualizado correctamente.")

            elif opcion == "4":
                nombre = input("Ingrese el nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)

                if resultados:
                    for producto in resultados:
                        print(producto)
                else:
                    print("No se encontraron productos.")

            elif opcion == "5":
                productos = inventario.obtener_todos()

                if productos:
                    for producto in productos:
                        print(producto)
                else:
                    print("El inventario está vacío.")

            elif opcion == "6":
                print("Finalizando el sistema.")
                break

            else:
                print("Opción inválida.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
