"""Скрипт для сканирования "Луны" и нахождения в ней кратеров."""
from typing import Generator

import numpy as np

my_file = "moon.txt"


def read_file(filename: str) -> Generator:
    """Генератор для чтения файла."""
    with open(filename) as file:
        for line in file:
            if "\n" in line:
                line = line.replace("\n", "")
            if line != "":
                res = line.split(" ")
                yield res


def list_builder(line: Generator) -> list:
    """Формирование списка из генератора."""
    new_list = list()
    new_list += list(line)
    return new_list


def is_input_array(array: list) -> bool:
    """Проверка является ли содержимое файла массивом."""
    lines = len(array)
    for i in range(lines):
        if len(array[i-1]) == len(array[i]):
            continue
        else:
            return False
    return True


def is_array_correct(array: list) -> bool:
    """Проверка содержит ли массив 1 или 0."""
    lines = len(array)
    for i in range(lines):
        lines_len = len(array[i])
        for j in range(lines_len):
            if array[i][j] == '0' or array[i][j] == '1':
                continue
            else:
                return False
    return True


def find_crater(array: np.ndarray, i: int, j: int) -> bool:
    """Нахождение кратера через рекурсию."""
    if i < 0 or i >= len(array):
        return False
    if j < 0 or j >= len(array):
        return False
    crater = array[i][j] == "1"
    array[i][j] = "0"
    if crater:
        find_crater(array, i, j + 1)
        find_crater(array, i, j - 1)
        find_crater(array, i + 1, j)
        find_crater(array, i - 1, j)
    return crater


def calculate(array: np.ndarray) -> int:
    """Счетчик найденных кратеров."""
    craters = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if find_crater(array, i, j):
                craters += 1
    return craters


def create_array_square(array: np.ndarray) -> np.ndarray:
    """Добавление к прямоугольной матрице недостающих строк или столбцов."""
    new_line = []
    lenght = max(len(array), len(array[0]))
    for i in range(lenght):
        new_line.append("0")
    new_line = np.array(new_line)
    if len(array) != len(array[0]):
        if len(array) > len(array[0]):
            while len(array) != len(array[0]):
                array = np.column_stack((my_array, new_line))
        else:
            while len(array) != len(array[0]):
                array = np.row_stack((array, new_line))
        return array
    return array


if __name__ == "__main__":
    my_array = []
    my_list = list_builder(read_file(my_file))
    if is_input_array(my_list) and is_array_correct(my_list):
        my_array = np.array(my_list)
        my_array = create_array_square(my_array)
        result = calculate(my_array)
        print(result)
    else:
        print(my_list)
        print("Не корректный массив")
