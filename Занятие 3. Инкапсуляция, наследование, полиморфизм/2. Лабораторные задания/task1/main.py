class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом - int")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Продолжительность должна быть числом с плавающей точкой - float")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self._duration = value

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    book1 = Book("1984", "Джордж Оруэлл")
    book2 = PaperBook("Час быка", "Иван Антонович Ефремов", 457)
    book3 = AudioBook("Машина останавливается", "Едвард Форстер", 88.72)



    print(book1)
    print(repr(book1), '\n')
    print(book1.author)
    # book1.author = ''
    print(book2)
    print(repr(book2), '\n')
    print(book3)
    print(repr(book3), '\n')
