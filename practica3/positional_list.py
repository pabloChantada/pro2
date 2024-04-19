'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

class SortedPositionalList:
    '''
    Clase que genera una Lista Posicional Ordenada.

    Methods
    -------
    is_empty(self):
    add(self, e):
    replace(self, p, e):
    
    '''
    def __init__(self):
        self._data = []

    def is_empty(self):
        '''
        Comprueba si la lista está vacía.
        '''
        return len(self._data) == 0

    def add(self, e):
        '''
        Inserta el elemento e en la lista manteniéndola ordenada.
        Parameters
        ----------
        e: elemento a añaidr
        '''
        # Si esta vacia o e es mas grande que el ultimo elemento se
        # añade directamente
        if self.is_empty() or e > self._data[-1]:
            self._data.append(e)
            # Reducimos en 1 el tamaño
            return len(self._data) - 1
        else:
            # Recorremos la lista hasta encontrar la posicion para colocar el 
            # elemento
            for i in range(len(self._data)):
                if e <= self._data[i]:
                    # movemos los elementos de la poscion i en adelante a la derecha
                    # de esta forma creamoes espacio para el elemento e y se mantiene el
                    # orden
                    self._data.insert(i, e)
                    # devolvemos la posicion donde se inserto el elemento
                    return i

    def replace(self, p, e):
        '''
        Reemplaza el elemento en la posición p con e manteniendo la lista ordenada.
        
        Parameters
        ----------
        p: posicion del elemento al reemplazar
        e: elmento a añadir
        '''
        
        if 0 <= p < len(self._data):
            self._data.pop(p)  # Eliminamos el elemento antiguo
            self.add(e)  # Añadimos el nuevo elemento de forma ordenada
        else:
            raise IndexError("Posición inválida")

    def __len__(self):
        '''
        Devuelve el número de elementos en la lista.
        '''
        return len(self._data)

    def __iter__(self):
        '''
        Devuelve un iterador sobre los elementos de la lista.
        '''        
        for item in self._data:
            yield item

class Peliculas:
    '''
    Clase para reprensentar las Peliculas.

    Parameters
    ----------
    - director(str): nombre del director
    - title(str): nombre de la pelicula
    - year(int): año de estreno
    - rating(float): calificación de la Pelicula
    
    Methods
    ------- 
    print(): imprime un string con los datos de la Pelicula
    '''
    
    def __init__(self, director: str, title: str, year: int, rating: float):
        self.director = director
        self.title = title
        self.year = year
        self.rating = rating
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string")
    
    @property
    def director(self):
        return self._director
    @director.setter
    def director(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._director = value
        else:
            raise ValueError("Director must be a non-empty string")
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and value > 0:
            self._year = value
        else:
            raise ValueError("Year must be a positive integer")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, float) and value > 0:
            self._rating = value
        else:
            raise ValueError("Rating must be a positive float")
    
    # Metodos magicos para utilizar las peliclas dentro de la lista posicional ordenada
    def __lt__(self, other):
        if not isinstance(other, Peliculas):
            return NotImplemented
        return (self.director, self.title, self.year) < (other.director, other.title, other.year)
    
    def __le__(self, other):
        if not isinstance(other, Peliculas):
            return NotImplemented
        return (self.director, self.title, self.year) <= (other.director, other.title, other.year)
    
    def __gt__(self, other):
        if not isinstance(other, Peliculas):
            return NotImplemented
        return (self.director, self.title, self.year) > (other.director, other.title, other.year)
    
    def __eq__(self, other):
        if not isinstance(other, Peliculas):
            return NotImplemented
        return (self.director, self.title, self.year) == (other.director, other.title, other.year)
    
    def __getitem__(self, key):
        return getattr(self,key)

    def print(self):
        return f"Title: {self.title} | Director: {self.director} | Year: {self.year} | Rating: {self.rating}"