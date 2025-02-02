class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self.pages = value
        else:
            raise ValueError("Количество страниц должно быть положительным числом")

    def __str__(self):
        return f"{super().__str__()}, {self.pages} страниц"

    def __repr__(self):
        return f"Бумажная книга(name={self.name}, author={self.author}, pages={self.pages})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.name = name
        self.author = author
        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, (float, int)) and value > 0:
            self.duration = value
        else:
            raise ValueError("Продолжительность должна быть положительным числом")

    def __str__(self):
        return f"{super().__str__()}, продолжительность {self.duration} минут"

    def __repr__(self):
        return f"Аудиокнига(name={self.name}, author={self.author}, duration={self.duration})"
