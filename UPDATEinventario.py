# inventario.py

import os
from producto import Producto


class Inventario:
    """
    Clase que gestiona una coleccion de productos.
    Permite operaciones CRUD y persistencia en archivo.
    """

    def __init__(self, archivo="inventario.txt"):
        self._productos = []
        self._archivo = archivo
        self._cargar_desde_archivo()

    # ==================================================
    # MÉTODOS PRIVADOS DE ARCHIVO
    # ==================================================

    def _cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo al iniciar el sistema.
        Si el archivo no existe, lo crea automaticamente.
        """
        try:
            if not os.path.exists(self._archivo):
                open(self._archivo, "w").close()
                print("Archivo de inventario creado automaticamente.")
                return

            with open(self._archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()

                    if linea:
                        try:
                            id_producto, nombre, cantidad, precio = linea.split(",")
                            producto = Producto(
                                id_producto,
                                nombre,
                                int(cantidad),
                                float(precio)
                            )
                            self._productos.append(producto)
                        except ValueError:
                            print(f"Línea corrupta ignorada: {linea}")

            print("Inventario cargado correctamente.")

        except FileNotFoundError:
            print("Error: No se encontro el archivo de inventario.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    def _guardar_en_archivo(self):
        """
        Guarda todos los productos en el archivo.
        """
        try:
            with open(self._archivo, "w", encoding="utf-8") as f:
                for producto in self._productos:
                    linea = f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n"
                    f.write(linea)

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")

    # ==================================================
    # METODOS CRUD
    # ==================================================

    def añadir_producto(self, producto: Producto):
        if any(p.get_id() == producto.get_id() for p in self._productos):
            raise ValueError("Ya existe un producto con ese ID.")

        self._productos.append(producto)
        self._guardar_en_archivo()

    def eliminar_producto(self, id_producto: str):
        for producto in self._productos:
            if producto.get_id() == id_producto:
                self._productos.remove(producto)
                self._guardar_en_archivo()
                return

        raise ValueError("Producto no encontrado.")

    def actualizar_producto(self, id_producto: str, nueva_cantidad=None, nuevo_precio=None):
        for producto in self._productos:
            if producto.get_id() == id_producto:

                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)

                self._guardar_en_archivo()
                return

        raise ValueError("Producto no encontrado.")

    def buscar_por_nombre(self, nombre: str):
        return [
            producto for producto in self._productos
            if nombre.lower() in producto.get_nombre().lower()
        ]

    def obtener_todos(self):
        return self._productos