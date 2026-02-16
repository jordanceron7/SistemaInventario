
# inventario.py

from producto import Producto


class Inventario:
    """
    Clase que gestiona una colección de productos.
    Permite operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
    """

    def __init__(self):
        self._productos = []

    def añadir_producto(self, producto: Producto):
        """
        Añade un producto asegurando que el ID sea único.
        """
        if any(p.get_id() == producto.get_id() for p in self._productos):
            raise ValueError("Ya existe un producto con ese ID.")

        self._productos.append(producto)

    def eliminar_producto(self, id_producto: str):
        """
        Elimina un producto por su ID.
        """
        for producto in self._productos:
            if producto.get_id() == id_producto:
                self._productos.remove(producto)
                return

        raise ValueError("Producto no encontrado.")

    def actualizar_producto(self, id_producto: str, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto.
        """
        for producto in self._productos:
            if producto.get_id() == id_producto:

                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)

                return

        raise ValueError("Producto no encontrado.")

    def buscar_por_nombre(self, nombre: str):
        """
        Busca productos por coincidencia parcial en el nombre.
        """
        return [
            producto for producto in self._productos
            if nombre.lower() in producto.get_nombre().lower()
        ]

    def obtener_todos(self):
        """
        Devuelve la lista completa de productos.
        """
        return self._productos
