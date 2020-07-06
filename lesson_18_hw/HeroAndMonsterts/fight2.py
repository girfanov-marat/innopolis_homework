"""Реализация класса для боя."""
import random


class Fight2:
    """Класс бой."""

    def __init__(self, hero, enemy, bag):
        """Конструктор класса."""
        self.bag = bag
        self.hero = hero
        self.enemy = enemy
        self.weapon = None
        self.hero_damage = None
        self.chance = None

    def greeting(self) -> None:
        """Метод описывающий врага при встрече."""
        print(f'Перед вами появился противник - {self.enemy.monster_class}, '
              f'тип атаки - {self.enemy.attack_type}, '
              f'урон - {self.enemy.damage}, '
              f'количество жизней - {self.enemy.hp}')

    @staticmethod
    def choice() -> str:
        """Выбор - сражаться или убежать."""
        answers = ["1", "2"]
        decision = input("Введите 1, чтобы сражаться. "
                         "2 чтобы убежать и набраться сил: ")
        while decision not in answers:
            print("Вы ввели неверное значение")
            decision = (input("Введите 1, чтобы сражаться. "
                              "2 чтобы убежать и набраться сил: "))
        return decision

    @staticmethod
    def leave() -> None:
        """Просто сообщение о том, герой решил убежать."""
        print("Вы убежали")

    def choose_weapon(self) -> None:
        """
        Выбор оружия.

        На выбор предоставляется оружие, которое в данный момент находится в сумке.
        """
        number = 1
        weapons = ''
        answers = {}
        for key in self.bag:
            weapons += f"{str(number)} - {key}, "
            answers.update({number: key})
            number += 1
        decision = input(f"Выберите оружие, с помощью которого вы будете сражаться: {weapons}\n")
        while int(decision) not in answers:
            print("Вы ввели неверное значение")
            decision = input(f"Выберите оружие, с помощью которого вы будете сражаться: {weapons}\n")
        self.weapon = answers[int(decision)]

    def set_hero_damage(self, arrows: int) -> bool:
        """Устанавливает урон героя в зависимости от выбранного оружия."""
        weapon = self.weapon
        if weapon == 'меч':
            self.hero_damage = self.hero.sword_damage
        if weapon == 'лук':
            if arrows > 0:
                self.hero_damage = self.hero.bow_damage
            else:
                print("У вас нет стрел")
                return True
        if weapon == 'книга заклинаний':
            self.hero_damage = self.hero.spell_damage
        return False

    def hero_attack(self) -> int:
        """Атака героя."""
        self.enemy.hp = self.enemy.hp - self.hero_damage

        print(f"Вы нанесли монстру {self.hero_damage} урона. "
              f"У противника осталось {self.enemy.hp} жизней")
        return self.enemy.hp

    def monster_simple_attack(self) -> int:
        """Атака врага."""
        self.hero.hp = self.hero.hp - self.enemy.damage

        print(f"Противник нанес вам {self.enemy.damage} урона."
              f"У вас осталось {self.hero.hp} жизней\n")

        return self.hero.hp

    def end_of_fight(self, hero_hp: int, monster_hp: int) -> bool:
        """Метод, для того, чтобы узнать закончился ли бой."""
        if hero_hp <= 0:
            print("Вы проиграли\n")
            return False
        elif monster_hp <= 0:
            print("Вы одолели монстра\n")
            self.hero.kills += 1
            return False
        else:
            return True

    def kills_counter(self) -> int:
        """Счетчик убийств."""
        return self.hero.kills

    @staticmethod
    def fight_continue() -> None:
        """Выводит сообщение о продолжении боя, если герой не выбрал бежать после раунда."""
        print("Бой продолжается")

    def monster_attack_with_dodge(self, chance: int) -> int:
        """
        Атака монстра с учетом классов персонажей.

        Если классы персонажей совпадают, герой может уклониться от атаки.
        """
        if self.hero.attack_type == self.enemy.attack_type:
            if chance == 3:
                print("Вы уклонились от атаки врага")
                return self.hero.hp

        self.hero.hp = self.hero.hp - self.enemy.damage

        print(f"Противник нанес вам {self.enemy.damage} урона."
              f"У вас осталось {self.hero.hp} жизней\n")
        return self.hero.hp

    def randomizer(self) -> int:
        """Рандомайзер для высчитывания шанса уклонения от атаки."""
        self.chance = random.randint(1, 5)
        return self.chance
