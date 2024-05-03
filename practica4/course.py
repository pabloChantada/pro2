'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''


class Curso:
    '''
    Clase que representa un curso.

    Parameters
    ----------
    - name (str) = nombre del curso
    - duration (int) = duracion en horas del curso
    - students (int) = numero de estudiantes
    - level (str) = nivel del curso
    - language (str) = lenguaje en el que se imparte el curso
    - price (float) = precio del curso
    - company (str) = nombre de la compañia a la que pertence el curso, 
    vacio si no hay dos con el mismo nombre
    '''

    def __init__(self, name: str, duration: int, students: int, level: str, language: str, price: float) -> None:
        self.name = name
        self.duration = duration
        self.students = students
        self.level = level
        self.language = language
        self.price = price
        self.company = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: int):
        if isinstance(value, int) and value > 0:
            self._duration = value
        else:
            raise ValueError("Duration must be a positive integer")

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, value: int):
        if isinstance(value, int) and value > 0:
            self._students = value
        else:
            raise ValueError("Students must be a positive integer")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._level = value
        else:
            raise ValueError("Level must be a non-empty string")

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._language = value
        else:
            raise ValueError("Language must be a non-empty string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if isinstance(value, float) and value > 0:
            self._price = value
        else:
            raise ValueError("Price must be a positive integer")

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value: str):
        if value is None or isinstance(value, str) and len(value) >= 0:
            self._company = value
        else:
            raise ValueError("Company must be a non-empty string")

    def __str__(self):
        '''
        Devuelve las caracteristicas del Curso en forma de cadena de texto.

        Returns
        -------
        str: Cadena que representa al objeto Curso.
        '''
        base_info = (
            f"Name: {self.name} | "
            f"Duration: {self.duration} | "
            f"Nº Students: {self.students} | "
            f"Level: {self.level} | "
            f"Language: {self.language} | "
            f"Price: {self.price}"
        )
        # Si solo su nombre esta duplicado añadimos la compañia
        if self.company:
            return f"{base_info} | Company: {self.company}"
        return base_info
