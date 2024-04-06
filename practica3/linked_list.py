class SortedPositionalList:
    def __init__(self):
        self._data = []

    def is_empty(self):
        """Comprueba si la lista está vacía."""
        return len(self._data) == 0

    def add(self, e):
        """Inserta el elemento e en la lista manteniéndola ordenada."""
        if self.is_empty() or e > self._data[-1]:
            self._data.append(e)
            return len(self._data) - 1
        else:
            for i in range(len(self._data)):
                if e <= self._data[i]:
                    # movemos los elementos de la poscion i en adelante a la derecha
                    # de esta forma creamoes espacio para el elemento e y se mantiene el
                    # orden
                    self._data.insert(i, e)
                    # devolvemos la posicion donde se inserto el elemento
                    return i

    def replace(self, p, e):
        """Reemplaza el elemento en la posición p con e manteniendo la lista ordenada."""
        if 0 <= p < len(self._data):
            self._data.pop(p)  # Eliminamos el elemento antiguo
            self.add(e)  # Añadimos el nuevo elemento de forma ordenada
        else:
            raise IndexError("Posición inválida")

    def __len__(self):
        """Devuelve el número de elementos en la lista."""
        return len(self._data)

    def __iter__(self):
        """Devuelve un iterador sobre los elementos de la lista."""
        for item in self._data:
            yield item

