"""Реализация классов главного героя."""

from abc import ABC, abstractmethod
from typing import Tuple


class Hero(ABC):
    """Абстрактный класс героя."""

    attack_type: str = ''

    def __init__(self, heal_points, sword_damage, bow_damage, spell_damage, kills):
        """Конструктор класса героя."""
        self.sword_damage = sword_damage
        self.bow_damage = bow_damage
        self.spell_damage = spell_damage
        self.hp = heal_points
        self.kills = kills
        self.class_bonus = 10
        self.totem = False

    @abstractmethod
    def update_sword_damage(self, new_sword_damage: int) -> None:
        """Метод обновления урона от меча."""
        pass

    @abstractmethod
    def update_bow_damage(self, new_bow_damage: int) -> None:
        """Метод обновления урона от лука."""
        pass

    @abstractmethod
    def update_spell_damage(self, new_spell_damage: int) -> None:
        """Метод обновления урона от заклинаний."""
        pass

    @abstractmethod
    def hero_class(self) -> str:
        """Метод возвращающий класс персонажа."""
        pass

    def hero_stats(self) -> Tuple[int, int, int, int, int]:
        """Метод возвращающий статы персонажа."""
        return self.hp, self.sword_damage, self.bow_damage, self.spell_damage, self.kills

    def hero_class_bonus(self):
        """ВОзвращает информацию о бонусе героя."""
        if self.attack_type == 'Ближний бой':
            print(f"Бонус от удара мечом + {self.class_bonus} ед. урона")
        if self.attack_type == 'Дальний бой':
            print(f"Бонус от выстрела луком + {self.class_bonus} ед. урона")
        if self.attack_type == 'Магический':
            print(f"Бонус от заклинаний + {self.class_bonus} ед. урона")


class Warrior(Hero):
    """Класс Воин."""

    attack_type = 'Ближний бой'

    def update_sword_damage(self, new_sword_damage):
        """Метод обновления урона от меча."""
        self.sword_damage = new_sword_damage + self.class_bonus

    def update_bow_damage(self, new_bow_damage):
        """Метод обновления урона от лука."""
        self.bow_damage = new_bow_damage

    def update_spell_damage(self, new_spell_damage):
        """Метод обновления урона от заклинаний."""
        self.spell_damage = new_spell_damage

    def hero_class(self):
        """Метод возвращающий класс персонажа."""
        return 'Воин'


class Archer(Hero):
    """Класс Лучник."""

    attack_type = 'Дальний бой'

    def update_sword_damage(self, new_sword_damage):
        """Метод обновления урона от меча."""
        self.sword_damage = new_sword_damage

    def update_bow_damage(self, new_bow_damage):
        """Метод обновления урона от лука."""
        self.bow_damage = new_bow_damage + self.class_bonus

    def update_spell_damage(self, new_spell_damage):
        """Метод обновления урона от заклинаний."""
        self.spell_damage = new_spell_damage

    def hero_class(self) -> str:
        """Метод возвращающий класс персонажа."""
        return 'Лучник'


class Mage(Hero):
    """Класс Маг."""

    attack_type = 'Магический'

    def update_sword_damage(self, new_sword_damage):
        """Метод обновления урона от меча."""
        self.sword_damage = new_sword_damage

    def update_bow_damage(self, new_bow_damage):
        """Метод обновления урона от лука."""
        self.bow_damage = new_bow_damage

    def update_spell_damage(self, new_spell_damage):
        """Метод обновления урона от заклинаний."""
        self.spell_damage = new_spell_damage + self.class_bonus

    def hero_class(self):
        """Метод возвращающий класс персонажа."""
        return 'Маг'
