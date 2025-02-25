class Car:
    """Базовый класс для автомобилей."""

    def __init__(self, make: str, model: str, year: int):
        """
        Конструктор класса Car.

        :param make: Произведённая компания автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self._make = make  # Защита свойства: не должно изменяться после инициализации
        self._model = model  # Защита свойства: не должно изменяться после инициализации
        self._year = year  # Защита свойства: не должно изменяться после инициализации

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    def start_engine(self) -> str:
        """Запуск двигателя автомобиля."""
        return "Двигатель запущен."

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление автомобиля."""
        return f"{self.__class__.__name__}(make={self.make!r}, " \
               f"model={self.model!r}, year={self.year})"


class PassengerCar(Car):
    """Класс для легковых автомобилей."""

    def __init__(self, make: str, model: str, year: int, seats: int):
        """
        Конструктор класса PassengerCar.

        :param make: Произведённая компания автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param seats: Количество мест в автомобиле.
        """
        super().__init__(make, model, year)  # Унаследовать атрибуты от родительского класса
        self._seats = seats  # Защита свойства: количество мест

    @property
    def seats(self) -> int:
        return self._seats

    def start_engine(self) -> str:
        """
        Запуск двигателя легкового автомобиля с сообщением о комфорте.

        Переопределение метода выполняется, чтобы добавить строку,
        описывающую комфорт легкового автомобиля при запуске.
        """
        base_message = super().start_engine()  # Вызов метода родительского класса
        return f"{base_message} Этот легковой автомобиль готов к поездке!"

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} (Seats: {self.seats})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление легкового автомобиля."""
        return f"{self.__class__.__name__}(make={self.make!r}, " \
               f"model={self.model!r}, year={self.year}, seats={self.seats})"


class Truck(Car):
    """Класс для грузовых автомобилей."""

    def __init__(self, make: str, model: str, year: int, load_capacity: float):
        """
        Конструктор класса Truck.

        :param make: Произведённая компания автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param load_capacity: Грузоподъёмность автомобиля в тоннах.
        """
        super().__init__(make, model, year)
        self._load_capacity = load_capacity  # Защита свойства: грузоподъемность

    @property
    def load_capacity(self) -> float:
        return self._load_capacity

    def start_engine(self) -> str:
        """
        Запуск двигателя грузовика с сообщением о мощности.

        Переопределение данного метода необходимо для предоставления
        дополнительной информации о мощности двигателя грузовика.
        """
        base_message = super().start_engine()
        return f"{base_message} Этот грузовик мощный и готов к работе!"

    def __str__(self) -> str:
        """Возвращает строковое представление грузовика."""
        return f"{super().__str__()} (Load Capacity: {self.load_capacity} tons)"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление грузовика."""
        return f"{self.__class__.__name__}(make={self.make!r}, " \
               f"model={self.model!r}, year={self.year}, " \
               f"load_capacity={self.load_capacity})"


# Пример использования:
if __name__ == "__main__":
    passenger_car = PassengerCar("Toyota", "Camry", 2020, 5)
    truck = Truck("Volvo", "FH", 2019, 20)

    print(passenger_car)  # 2020 Toyota Camry (Seats: 5)
    print(repr(passenger_car))  # PassengerCar(make='Toyota', model='Camry', year=2020, seats=5)
    print(passenger_car.start_engine())  # Двигатель запущен. Этот легковой автомобиль готов к поездке!

    print(truck)  # 2019 Volvo FH (Load Capacity: 20 tons)
    print(repr(truck))  # Truck(make='Volvo', model='FH', year=2019, load_capacity=20)
    print(truck.start_engine())  # Двигатель запущен. Этот грузовик мощный и готов к работе!
