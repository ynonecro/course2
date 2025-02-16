if __name__ == "__main__":
    # Write your solution here
    class Vehicle:
        """
        Базовый класс для всех транспортных средств.

        Атрибуты:
            make (str): Производитель транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска.

        Методы:
            __str__: Возвращает строковое представление объекта класса.
            __repr__: Возвращает подробное представление объекта класса.
            start: Запускает двигатель транспортного средства.
        """

        def __init__(self, make: str, model: str, year: int) -> None:
            self.make = make
            self.model = model
            self.year = year
            self._is_running = False  # защита состояния двигателя от внешних изменений

        def __str__(self) -> str:
            return f"{self.year} {self.make} {self.model}"

        def __repr__(self) -> str:
            return f"Vehicle(make={self.make}, model={self.model}, year={self.year})"

        def start(self) -> None:
            """Запускает двигатель транспортного средства."""
            self._is_running = True
            print(f"{self} запущен.")

        def stop(self) -> None:
            """Останавливает двигатель транспортного средства."""
            self._is_running = False
            print(f"{self} остановлен.")


    class Car(Vehicle):
        """
        Класс для легковых автомобилей, наследующий Vehicle.

        Атрибуты:
            seating_capacity (int): Вместимость сидений легкового автомобиля.

        Методы:
            __str__: Возвращает строковое представление объекта класса, добавляя информацию о вместимости.
            play_music: Проигрывает музыку в автомобиле.
        """

        def __init__(self, make: str, model: str, year: int, seating_capacity: int) -> None:
            super().__init__(make, model, year)
            self.seating_capacity = seating_capacity

        def __str__(self) -> str:
            return super().__str__() + f", вместимость: {self.seating_capacity} человек"

        def play_music(self) -> None:
            """Проигрывает музыку в автомобиле."""
            if not self._is_running:
                print("Двигатель должен быть запущен для проигрывания музыки.")
            else:
                print(f"{self} играет музыку.")

        def start(self) -> None:
            """Перегруженный метод, который выводит дополнительное сообщение при запуске."""
            super().start()
            print("Теперь вы готовы к поездке!")


    pass
