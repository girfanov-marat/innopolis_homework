"""Текстовая игра "Герой и Чудовища"."""
import random
import typing

heal_points = 10
current_damage = 10
kills = 0


def monster(hero_hp: int, hero_damage: int) -> typing.Tuple[int, int]:
    """
    В функции реализована встреча с монстром.

    Можно выбрать - сражаться или убежать
    """
    monster_hp = random.randint(20, 30)
    monster_damage = random.randint(10, 30)
    answers = ["1", "2"]
    flag = 0
    print(f"Вы встретили чудовище с {monster_hp} жизнями "
          f"и с силой удара {monster_damage}")
    choice = (input("Введите 1, чтобы сражаться. "
                    "2 чтобы убежать и набраться сил: "))
    while choice not in answers:
        print("Вы ввели неверное значение")
        choice = (input("Введите 1, чтобы сражаться. "
                        "2 чтобы убежать и набраться сил: "))
    if choice == "1":
        hero_hp = fight(hero_hp, hero_damage, monster_hp, monster_damage)
        flag = 1
    elif choice == "2":
        print("Вы убежали")
    return hero_hp, flag


def fight(hero_hp: int, hero_damage: int,
          monster_hp: int, monster_damage: int) -> int:
    """Функция боя с монстром."""
    if monster_hp // hero_damage < hero_hp // monster_damage:
        rounds = monster_hp // hero_damage + 1
    else:
        rounds = hero_hp // monster_damage + 1
    for i in range(rounds):
        monster_hp = monster_hp - hero_damage
        hero_hp = hero_hp - monster_damage
        print("Раунд: ", i+1)
        print(f"Вы нанесли монстру {hero_damage} урона. "
              f"У монстра осталось {monster_hp} жизней")
        print(f"Монстр нанес вам {monster_damage}. "
              f"У вас осталось {hero_hp} жизней")
        if hero_hp <= 0:
            print("Вы проиграли!")
            break
        if monster_hp <= 0:
            print("Вы убили монстра!")
            break
    return hero_hp


def apple(hp: int) -> int:
    """
    Функция прибавляет к здоровью героя рандомное значение.

    Значение задается в пределах 5-10.
    """
    healing = random.randint(5, 10)
    hp = hp + healing
    print(f"Вы нашли яблоко, которое восстановило вам {healing} здоровья")
    return hp


def sword(damage: int) -> int:
    """
    Функция предлагает установить новое рандомное значение урона героя.

    Можно выбрать новый меч или отказаться.
    """
    sword_power = random.randint(10, 25)
    answers = ["1", "2"]
    print(f"Вы обнаружили меч с уроном: {sword_power}")
    choice = (input("Введите 1, чтобы взять новый меч. 2 чтобы пройти мимо: "))
    while choice not in answers:
        print("Вы ввели неверное значение")
        choice = (input("Введите 1, чтобы взять новый меч. "
                        "2 чтобы пройти мимо: "))
    if choice == "1":
        print("Вы подобрали новый меч")
        damage = sword_power
    elif choice == "2":
        print("Вы оставили старый меч и пошли дальше")
    return damage


print("Текстовая игра \"Герой и Чудовища\" \n"
      "Вы - рыцарь в фантастической стране. \n"
      "Ваша задача - победить 10 чудовищ, чтобы спасти королевство "
      "от нападения и тем самым выиграть игру.\n")

while kills != 10:
    print(f"Здоровье: {heal_points}, Урон: {current_damage}, "
          f"Количество убитых монстров: {kills}")
    current_action = random.randint(1, 3)
    if current_action == 1:
        heal_points, win_flag = monster(heal_points, current_damage)
        if heal_points <= 0:
            break
        else:
            kills += win_flag
    elif current_action == 2:
        heal_points = apple(heal_points)
    elif current_action == 3:
        current_damage = sword(current_damage)
    print(" ")

if kills == 10:
    print("Победа!")

input("Нажмите любую клавишу для выхода")
