# producto.py

class Producto:
    """
    Clase que representa un producto dentro del sistema de inventario.
    Aplica el principio de encapsulamiento mediante atributos privados.
    """

    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.

        :param id_producto: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en inventario.
        :param precio: Precio unitario del producto.
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters

    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio(self) -> float:
        return self._precio

    # Setters

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_cantidad(self, cantidad: int):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa.")

    def set_precio(self, precio: float):
        if precio >= 0:
            self._precio = precio
        else:
            raise ValueError("El precio no puede ser negativo.")

    def __str__(self):
        """
        Representación textual del producto.
        """
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
