"""Классы описывающие врагов."""
import random
from abc import ABC, abstractmethod
from typing import Tuple


class Enemy:
    """Базовый класс для врага."""

    def __init__(self):
        """Конструктор класса врага."""
        self.damage = random.randint(10, 25)
        self.hp = random.randint(10, 50)
        self.attack_type = None
        self.monster_class = None

    def attack(self) -> int:
        """Метод атаки, возвращающий урон."""
        return self.damage

    def monster_stats(self) -> Tuple[int, int, str, str]:
        """Метод, возрвщающий характеристики врага."""
        return self.hp, self.damage, self.attack_type, self.monster_class


class Rogue(Enemy):
    """Класс Разбойник."""

    def __init__(self):
        """Конструктор класса Разбойник."""
        super().__init__()
        self.attack_type = 'Ближний бой'
        self.monster_class = 'Разбойник'


class Warlock(Enemy):
    """Класс Чернокнижник."""

    def __init__(self):
        """Конструктор класса Чернокнижник."""
        super().__init__()
        self.attack_type = 'Магический'
        self.monster_class = 'Чернокнижник'


class Hunter(Enemy):
    """Класс Охотник."""

    def __init__(self):
        """Конструктор класса Охотник."""
        super().__init__()
        self.attack_type = 'Дальний бой'
        self.monster_class = 'Охотник'


class EnemyFactory(ABC):
    """Абстрактная фабрика для создания врагов."""

    @abstractmethod
    def create_enemy(self):
        """Создание абстрактного продукта."""
        pass


class RogueFactory(EnemyFactory):
    """Фабрика создания Разбойников."""

    def create_enemy(self):
        """Создание врага класса Разбойник."""
        return Rogue()


class WarlockFactory(EnemyFactory):
    """Фабрика создания Чернокнижников."""

    def create_enemy(self):
        """Создание врага класса Чернокнижник."""
        return Warlock()


class HunterFactory(EnemyFactory):
    """Фабрика создания Охотников."""

    def create_enemy(self):
        """Создание врага класса Охотник."""
        return Hunter()
