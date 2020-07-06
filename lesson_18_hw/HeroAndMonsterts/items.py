"""Классы описывающие игровые предметы."""
import random
from abc import ABC, abstractmethod


class Items(ABC):
    """Абстрактный класс для всех предметов."""

    item_name = ''

    @abstractmethod
    def greeting(self) -> None:
        """Абстрактный метод для вывода сообщения, при обнаружении предмета."""
        pass


class Weapons(Items):
    """Класс для всех видов оружий."""

    def __init__(self):
        """Конструктор класса оружий."""
        self.current_damage = 10
        self.new_damage = None

    @abstractmethod
    def choice(self) -> str:
        """Метод для выбора, подобрать или пройти мимо."""
        pass

    @abstractmethod
    def item_info(self) -> str:
        """Метод возвращающий информацию об оружии."""
        pass

    @abstractmethod
    def set_damage(self) -> int:
        """Метод возвращающий новый урон от оружия."""
        pass


class Sword(Weapons):
    """Класс оружия - меч."""

    item_name = 'меч'

    def greeting(self):
        """Метод для вывода сообщения, при обнаружении предмета."""
        self.new_damage = random.randint(10, 25)
        print(f"Вы обнаружили новый меч с уроном {self.new_damage}")

    def choice(self) -> str:
        """Метод для выбора, подобрать или пройти мимо."""
        answers = ["1", "2"]
        decision = input("Введите 1, чтобы взять новый меч. "
                         "2 чтобы пройти мимо: ")
        while decision not in answers:
            print("Вы ввели неверное значение")
            decision = (input("Введите 1, чтобы взять новый меч. "
                              "2 чтобы пройти мимо: "))
        if decision == "1":
            print("Вы подобрали новый меч")
            self.current_damage = self.new_damage
        elif decision == "2":
            print("Вы не подобрали новый предмет и пошли дальше")
        return decision

    def set_damage(self):
        """Метод возвращающий новый урон от оружия."""
        return self.current_damage

    def item_info(self):
        """Метод возвращающий информацию об оружии."""
        return f"{self.current_damage} единиц урона"


class Bow(Weapons):
    """Класс оружия - лук."""

    item_name = 'лук'
    arrows = 0

    def greeting(self):
        """Метод для вывода сообщения, при обнаружении предмета."""
        self.new_damage = random.randint(10, 25)
        print(f"Вы обнаружили новый лук с уроном {self.new_damage}")

    def choice(self) -> str:
        """Метод для выбора, подобрать или пройти мимо."""
        answers = ["1", "2"]
        decision = input("Введите 1, чтобы взять новый лук. "
                         "2 чтобы пройти мимо: ")
        while decision not in answers:
            print("Вы ввели неверное значение")
            decision = (input("Введите 1, чтобы взять новый лук. "
                              "2 чтобы пройти мимо: "))
        if decision == "1":
            print("Вы подобрали новый лук")
            self.current_damage = self.new_damage
        elif decision == "2":
            print("Вы не подобрали новый предмет и пошли дальше")
        return decision

    def set_damage(self):
        """Метод возвращающий новый урон от оружия."""
        return self.current_damage

    def arrow_shot(self) -> None:
        """Уменьшает количество стрел при использовании лука."""
        self.arrows -= 1
        if self.arrows <= 0:
            print("У вас кончились стрелы, выберите другое оружие")

    def item_info(self):
        """Метод возвращающий информацию об оружии."""
        return f"{self.current_damage} единиц урона, количество стрел {self.arrows}"


class SpellBook(Weapons):
    """Класс оружия - книга заклинаний."""

    item_name = 'книга заклинаний'

    def greeting(self):
        """Метод для вывода сообщения, при обнаружении предмета."""
        self.new_damage = random.randint(10, 25)
        print(f"Вы обнаружили новую книгу заклинаний с уроном {self.new_damage}")

    def choice(self) -> str:
        """Метод для выбора, подобрать или пройти мимо."""
        answers = ["1", "2"]
        decision = input("Введите 1, чтобы взять новую книгу заклинаний. "
                         "2 чтобы пройти мимо: ")
        while decision not in answers:
            print("Вы ввели неверное значение")
            decision = (input("Введите 1, чтобы взять новую книгу заклинаний. "
                              "2 чтобы пройти мимо: "))
        if decision == "1":
            print("Вы подобрали новую книгу заклинаний")
            self.current_damage = self.new_damage
        elif decision == "2":
            print("Вы не подобрали новый предмет и пошли дальше")
        return decision

    def set_damage(self):
        """Метод возвращающий новый урон от оружия."""
        return self.current_damage

    def item_info(self):
        """Метод возвращающий информацию об оружии."""
        return f"{self.current_damage} единиц урона"


class Arrows(Items):
    """Класс стрелы для лука."""

    item_name = 'стрелы'
    arrows = 0

    def greeting(self):
        """Метод для вывода сообщения, при обнаружении предмета."""
        self.arrows = random.randint(1, 5)
        print(f"Вы нашли стрелы - {self.arrows} шт")


class Apple(Items):
    """Класс яблоко, восстанавливает жизни героя."""

    item_name = 'яблочко'

    def greeting(self):
        """Метод для вывода сообщения, при обнаружении предмета."""
        healing = random.randint(10, 20)
        print(f"Вы нашли яблоко, которое восстановило вам {healing} здоровья")
        return healing


class Totem(Items):
    """Класс тотем, сохраняет текущее состояние игры. Действует только 1 раз после смерти."""

    item_name = 'тотем'

    def __init__(self, hero, bag):
        """Конструктор класса Тотем. Принимает экземпляр класса героя и сумку."""
        self.hero = hero
        self.bag = bag

    def greeting(self):
        """Метод для вывода сообщения, при обнаружении предмета."""
        print("Вы встретили на своем пути тотем, который позволяет вам сохраниться")

    @staticmethod
    def choice() -> str:
        """Метод для выбора, подобрать или пройти мимо."""
        answers = ["1", "2"]
        decision = input("Введите 1, чтобы подобрать тотем. "
                         "2 чтобы пройти мимо: ")
        while decision not in answers:
            print("Вы ввели неверное значение")
            decision = input("Введите 1, чтобы подобрать тотем. "
                             "2 чтобы пройти мимо: ")
        if decision == "1":
            print("Вы сохранились")

        elif decision == "2":
            print("Вы не подобрали новый предмет и пошли дальше")
        return decision

    @staticmethod
    def save_point():
        """Выводит сообщение о том, что герой вернулся к точке сохранения."""
        print('Вы вернулись к точке сохранения')
