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
        self.pages = pages  # Используем свойство для проверки

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для проверки

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration:.2f} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration:.2f})"


# Пример использования
if __name__ == "__main__":
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

    print(paper_book)  # Книга 1984. Автор Джордж Оруэлл. Количество страниц: 328
    print(repr(paper_book))  # PaperBook(name='1984', author='Джордж Оруэлл', pages=328)

    print(audio_book)  # Книга 1984. Автор Джордж Оруэлл. Продолжительность: 11.50 часов
    print(repr(audio_book))  # AudioBook(name='1984', author='Джордж Оруэлл', duration=11.50)
