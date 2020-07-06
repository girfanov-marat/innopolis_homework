"""Контроллер - класс Фасад для управления элементами игры."""
import random
from typing import Any, Tuple

from lesson_18_hw.HeroAndMonsterts.fight2 import Fight2
from lesson_18_hw.HeroAndMonsterts.hero import Warrior, Archer, Mage
from lesson_18_hw.HeroAndMonsterts.monsters import RogueFactory, WarlockFactory, HunterFactory
from lesson_18_hw.HeroAndMonsterts.items import Sword, Bow, SpellBook, Arrows, Apple, Totem


class GameController:
    """Контроллер - класс Фасад для управления элементами игры."""

    def __init__(self):
        """Конструктор класса."""
        self.hero = None
        self.enemy = None
        self.item = None
        self.bag = None
        self.current_fight = None
        self.totem = Totem
        self.fight = Fight2  # type: ignore
        self.hero_classes = {
            "warrior": Warrior,
            "archer": Archer,
            "mage": Mage
        }
        self.enemy_factory_dict = {
            "rogue": RogueFactory,
            "warlock": WarlockFactory,
            "hunter": HunterFactory
        }
        self.items_dict = {'sword': Sword,
                           'bow': Bow,
                           'spell_book': SpellBook,
                           'arrow': Arrows,
                           'apple': Apple}

    def set_character_class(self, h_stats: tuple) -> None:
        """Выбор класса персонажа."""
        hero_class = input("Выберите класс персонажа: 1 - Воин, 2 - Лучник, 3 - Маг: ")
        classes = ["1", "2", "3"]

        while hero_class not in classes:
            print("Вы ввели неверное значение")
            hero_class = input("Выберите класс персонажа: 1 - Воин, 2 - Лучник, 3 - Маг: ")

        if hero_class == "1":
            hero = self.hero_classes["warrior"](*h_stats)
        elif hero_class == "2":
            hero = self.hero_classes["archer"](*h_stats)
        else:
            hero = self.hero_classes["mage"](*h_stats)
        self.hero = hero
        sword = self.items_dict['sword']()
        self.bag = {sword.item_name: sword.item_info()}

    def create_enemy(self) -> None:
        """Создание врага при помощи фабрики."""
        enemy_type_list = ["rogue", "warlock", "hunter"]
        spawn_type = random.choice(enemy_type_list)
        spawn = self.enemy_factory_dict[spawn_type]()
        self.enemy = spawn.create_enemy()

    def create_item(self) -> None:
        """Создание игрового предмета."""
        items_list = ['sword', 'bow', 'spell_book', 'arrow', 'apple']
        item_type = random.choice(items_list)
        item = self.items_dict[item_type]()
        self.item = item

    def main_message(self, kills: int) -> None:
        """Основное сообщение в игре. Показывает текущее состояние."""
        hero = self.hero
        bag = self.bag
        print(f"\nВаш класс - {hero.hero_class()} Здоровье: {hero.hp}, "
              f"Количество убитых монстров: {kills}")
        hero.hero_class_bonus()
        bag_items = ''
        for key, value in bag.items():
            bag_items += f'{key} - {value}, '
        print(f"Доступные оружия для атаки: {bag_items}\n")

    def set_new_weapon(self, bow: Bow = None) -> Any:
        """Обновляет сумку в зависимости от значения item.choice."""
        item = self.item
        bag = self.bag
        item.greeting()
        if item.choice() == '1':
            if bow is not None:
                if item.item_name == 'лук':
                    item.arrows = bow.arrows
            bag.update({item.item_name: item.item_info()})
        return self.item

    def update_sword(self) -> None:
        """Устанавливает урон от меча в атрибут класса hero.sword_damage."""
        self.hero.update_sword_damage(self.item.set_damage())

    def update_bow(self) -> None:
        """Устанавливает урон от лука в атрибут класса hero.bow_damage."""
        self.hero.update_bow_damage(self.item.set_damage())

    def update_spell(self) -> None:
        """Устанавливает урон от книги заклинаний в атрибут класса hero.spell_damage."""
        self.hero.update_spell_damage(self.item.set_damage())

    def arrows_setting(self, bow) -> Any:
        """Добавляет стрелы в сумку при наличии лука."""
        bag = self.bag
        arrow = self.item
        arrow.greeting()
        if 'лук' in bag:
            bow.arrows += arrow.arrows
            bag.update({bow.item_name: bow.item_info()})
            return bow
        else:
            print("У вас нет лука, вам некуда положить стрелы")

    def eat_apple(self) -> None:
        """Восстанавливает жизни."""
        apple = self.item.greeting()
        self.hero.hp += apple

    def fight_message(self) -> None:
        """Создает экземпляр класса fight и выводит сообщение об обнаруженном враге."""
        fight = self.fight(self.hero, self.enemy, self.bag)
        self.current_fight = fight
        fight.greeting()

    def fight_or_run(self) -> str:
        """Выбор - сражаться или убежать."""
        return self.fight.choice()

    def fight_actions(self, bow) -> Tuple[int, int, dict]:
        """Раунд боя с врагом."""
        f = self.current_fight
        f.choose_weapon()
        f.set_hero_damage(bow.arrows)
        while f.set_hero_damage(bow.arrows):
            f.choose_weapon()
        m_hp = f.hero_attack()
        if f.weapon == 'лук':
            bow.arrow_shot()
            self.bag.update({bow.item_name: bow.item_info()})
        h_hp = f.monster_attack_with_dodge(f.randomizer())
        self.hero.hp = h_hp
        self.hero.kills = f.kills_counter()
        return h_hp, m_hp, bow

    def end_of_fight(self, h_hp: int, m_hp: int) -> bool:
        """Метод, для того, чтобы узнать закончился ли бой."""
        return self.current_fight.end_of_fight(h_hp, m_hp)

    def leave_fight(self) -> None:
        """Вывод сообщения, о том, что герой бежал."""
        self.current_fight.leave()

    def get_totem(self) -> Any:
        """Подобрать тотем или нет. При подборе в атрибут класса hero.totem устанавливается значение True."""
        totem = self.totem(self.hero, self.bag)
        if totem.choice() == '1':
            self.hero.totem = True
            return totem
        return None

    def totem(self, totem) -> bool:
        """Возврат состояния игры при наличии тотема."""
        if self.hero.hp < 0:
            if self.hero.totem:
                totem.save_point()
                self.hero = totem.hero
                self.bag = totem.bag
                return False
        return True
