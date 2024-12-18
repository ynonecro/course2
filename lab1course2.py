# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Apple:
    def __init__(self, space_in_basket: int, quantity: int):
        self.space_in_basket = space_in_basket
        self.quantity = quantity
        """
                Создание и подготовка к работе объекта "Яблоко"

                :param space_in_basket: Количество места в корзине
                :param quantity: Количество яблок

                Примеры:
                >>> apple = Apple(10, 2)  # инициализация экземпляра класса
                """

        if not isinstance(space_in_basket, int):
            raise TypeError("Количество мест в корзине должно быть типа int")
        if space_in_basket < 0:
            raise ValueError("Количество мест в корзине не может быть отрицательным числом")

        if not isinstance(quantity, int):
            raise TypeError("Количество яблок должно быть int")
        if quantity < 0:
            raise ValueError("Количество яблок не может быть отрицательным числом")

    def is_empty_basket(self) -> bool:
        """
               Функция которая проверяет, является ли корзина пустой

               :return: Является ли корзина пустой

               Примеры:
               >>> apple = Apple(10, 0)
               >>> apple.is_empty_basket()
               """
        ...

    def add_apple(self, added_apple: int) -> None:
        """
        Добавление яблок.
        :param added_apple: Количество добавляемых яблок

        :raise ValueError: Если количество добавляемых яблок превышает свободное место в корзине, то вызываем ошибку

        Примеры:
        >>> apple = Apple(10, 0)
        >>> apple.add_apple(2)
        """
        if not isinstance(added_apple, int):
            raise TypeError("Добавляемое количество яблок должно быть типа int")
        if added_apple < 0:
            raise ValueError("Добавляемое количество яблок должно быть положительным числом")
        ...

class Exam:
    def __init__(self, scored_points: int, passing_score: int):
        self.scored_points = scored_points
        self.passing_score = passing_score
        """
                Создание и подготовка к работе объекта "Экзамен"

                :param scored_points: Набранные баллы
                :param passing_score: Проходной балл

                Примеры:
                >>> exam = Exam(100, 50)  # инициализация экземпляра класса
                """
        if not isinstance(scored_points, int):
            raise TypeError("Набранные баллы должны быть типа int")
        if scored_points < 0:
            raise ValueError("Количество набарнных баллов не может быть отрицательным числом")

        if not isinstance(passing_score, int):
            raise TypeError("Проходной балл должен быть int")
        if passing_score < 0:
            raise ValueError("Проходной балл не может быть отрицательным числом")


    def add_points(self, added_points: int) -> None:
        """
        Добавление баллов.
        :param added_points: Количество добавляемых баллов

        :raise ValueError: Если количество добавляемых баллов превышает проходной балл, то вызываем ошибку

        Примеры:
        >>> exam = Exam(20, 21)
        >>> exam.add_points(2)
        """
        if not isinstance(added_points, int):
            raise TypeError("Добавляемое количество баллов должно быть типа int")
        if added_points < 0:
            raise ValueError("Добавляемое количество баллов должно быть положительным числом")
        ...

    def remove_points(self, estimate_points: float) -> None:
        """
        Изъятие баллов.

        :param estimate_points: Количество изъятых баллов
        :raise ValueError: Если количество изъятых баллов превышает количество набранных баллов,
        то возвращается ошибка.

        :return: Количество реально изъятых баллов

        Примеры:
        >>> exam = Exam(60, 50)
        >>> exam.remove_points(20)
        """
        ...

class BlackCat:
    def __init__(self, black: int, quantity: int):
        self.black = black
        self.quantity = quantity
        """
                Создание и подготовка к работе объекта "Черный Кот"

                :param black: Количество черных котов
                :param quantity: Общее количество котов

                Примеры:
                >>> cat = BlackCat(1, 2)  # инициализация экземпляра класса
                """

        if not isinstance(black, int):
            raise TypeError("Количество черных котов должно быть типа int")
        if black < 0:
            raise ValueError("Количество черных котов не может быть отрицательным числом")


        if not isinstance(quantity, int):
            raise TypeError("Количество котов должно быть int")
        if quantity < 0:
            raise ValueError("Количество котов не может быть отрицательным числом")

    def add_black_cat(self, black_cats: int) -> None:
        """
        Добавление котов.
        :param black_cats: Количество добавляемых черных котов

        :raise ValueError: Если количество добавляемых черных котов превышает общее количество котов, то вызываем ошибку

        Примеры:
        >>> cat = BlackCat(10, 10)
        >>> cat.add_black_cat(2)
        """
        if not isinstance(black_cats, int):
            raise TypeError("Добавляемое количество черных котов должно быть типа int")
        if black_cats < 0:
            raise ValueError("Добавляемое количество черных котов должно быть положительным числом")
        ...

    def meow(self, cat_meow: str, quantity: int):
        self.cat_meow = cat_meow

        """
        Функция, которая вызывает мяуканье кота.

        :param cat_meow: Мяуканье

        :param quantity: Количество котов
        :raise ValueError: Если количество котов меньше единицы, то мяукать некому, поэтому вызываем ошибку

        :return: Кот мяукает

        Примеры:
        >>> cat = BlackCat("Мяу!", 1)
        >>> cat.meow()
        """

        if quantity < 1:
            raise ValueError("Количество котов не может быть меньше единицы")
        if quantity >= 1:
            cat_meow = "Мяу!"

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod() # тестирование примеров, которые находятся в документации
