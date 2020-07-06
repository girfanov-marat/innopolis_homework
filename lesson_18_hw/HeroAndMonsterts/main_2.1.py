"""Основной файл игры."""
import random

from lesson_18_hw.HeroAndMonsterts.controller import GameController


gc = GameController()

heal_points = 10000
sword = gc.items_dict['sword']()
bow = gc.items_dict['bow']()
spell_book = None
totem = None
kills = 0

stats = (heal_points, sword.current_damage, bow, spell_book, kills)

gc.set_character_class(stats)

while kills != 10:
    gc.main_message(kills)
    gc.create_item()
    current_action = random.randint(1, 2)
    if current_action == 1:
        if gc.item.item_name == 'меч':
            sword = gc.set_new_weapon()
            gc.update_sword()
        if gc.item.item_name == 'лук':
            bow = gc.set_new_weapon(bow)
            gc.update_bow()
        if gc.item.item_name == 'книга заклинаний':
            spell_book = gc.set_new_weapon()
            gc.update_spell()
        if gc.item.item_name == 'стрелы':
            bow = gc.arrows_setting(bow)
        if gc.item.item_name == 'яблочко':
            gc.eat_apple()
        if gc.item.item_name == 'тотем':
            totem = gc.get_totem()
    if current_action == 2:
        gc.create_enemy()
        gc.fight_message()
        combat = True
        while combat:
            choice = gc.fight_or_run()
            if choice == '1':
                hero_hp, monster_hp, bow = gc.fight_actions(bow)
                combat = gc.end_of_fight(hero_hp, monster_hp)
                if hero_hp <= 0:
                    break
            else:
                combat = False
                gc.leave_fight()
    if totem:
        break
    kills = gc.hero.kills

if kills == 10:
    print("Победа!")

input("Нажмите Enter для выхода")
