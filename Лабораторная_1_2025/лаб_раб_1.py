# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


class Furniture:
    """
    Класс, представляющий мебель.
    """

    def __init__(self, material: str, weight: float, height: float):
        """
        Инициализация мебели.

        :param material: Материал, из которого сделана мебель. Должен быть строкой.
        :param weight: Вес мебели в килограммах. Должен быть положительным числом.
        :param height: Высота мебели в сантиметрах. Должен быть положительным числом.
        :raises ValueError: Если weight или height отрицательные.

        >>> chair = Furniture("Wood", 10.0, 90.0)
        >>> chair.material
        'Wood'
        >>> chair.weight
        10.0
        >>> chair.height
        90.0
        """
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")

        self.material = material
        self.weight = weight
        self.height = height

    def assemble(self) -> None:
        """Сборка мебели."""
        pass

    def disassemble(self) -> None:
        """Разборка мебели."""
        pass


class Animal:
    """
    Класс, представляющий животное.
    """

    def __init__(self, species: str, age: int, health_status: str):
        """
        Инициализация животного.

        :param species: Вид животного. Должен быть строкой.
        :param age: Возраст животного в годах. Должен быть неотрицательным числом.
        :param health_status: Статус здоровья животного. Должен быть строкой.
        :raises ValueError: Если age отрицательный.

        >>> dog = Animal("Dog", 5, "Healthy")
        >>> dog.species
        'Dog'
        >>> dog.age
        5
        >>> dog.health_status
        'Healthy'
        """
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")

        self.species = species
        self.age = age
        self.health_status = health_status

    def eat(self, food_type: str) -> None:
        """Питание животного."""
        pass

    def sleep(self, hours: int) -> None:
        """
        Сон животного.

        :param hours: Количество часов сна. Должно быть положительным числом.
        :raises ValueError: Если hours отрицательный.
        """
        pass


class DigitalProduct:
    """
    Класс, представляющий цифровой продукт.
    """

    def __init__(self, title: str, file_size: float, license_type: str):
        """
        Инициализация цифрового продукта.

        :param title: Название продукта. Должно быть строкой.
        :param file_size: Размер файла в мегабайтах. Должен быть положительным числом.
        :param license_type: Тип лицензии. Должен быть строкой.
        :raises ValueError: Если file_size отрицательный.

        >>> ebook = DigitalProduct("Python Programming", 2.5, "Unlimited")
        >>> ebook.title
        'Python Programming'
        >>> ebook.file_size
        2.5
        >>> ebook.license_type
        'Unlimited'
        """
        if file_size <= 0:
            raise ValueError("Размер файла должен быть положительным числом.")

        self.title = title
        self.file_size = file_size
        self.license_type = license_type

    def download(self) -> None:
        """Скачивание цифрового продукта."""
        pass

    def update_license(self, new_license: str) -> None:
        """
        Обновление лицензии.

        :param new_license: Новый тип лицензии.
        """
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
