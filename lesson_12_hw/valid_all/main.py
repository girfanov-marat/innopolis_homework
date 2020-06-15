"""Основной файл, в котором находятся необходимые функции для проверок."""
import re

import jsonschema
from lesson_12_hw.valid_all.decorators import valid_all_decorator
from lesson_12_hw.valid_all.my_exceptions import InputParameterVerificationError

regex_to_check = "[0-9]{2}-[0-9]{2}-[0-9]{4}"

SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "date": {
      "type": "string"
    }
  },
  "required": [
    "date"
  ]
}


def regex_func(result: str) -> bool:
    """Валидация даты."""
    regex = re.compile(regex_to_check)
    return bool(regex.match(result))


def validate_json(json: dict) -> bool:
    """Валидация JSON."""
    try:
        return not bool(jsonschema.validate(json, SCHEMA))
    except jsonschema.ValidationError:
        return False


def default_function() -> None:
    """Поведение программы если не прошли валидации."""
    print("Формат даты не валиден")


@valid_all_decorator(input_validation=validate_json,
                     result_validation=regex_func,
                     default_behavior=default_function,
                     on_fail_repeat_times=5)
def target_function(json: dict) -> str:
    """Функция, принимаемое и возвращаемое значение которой нужно провалидировать."""
    return json["date"]


positive_case = {"date": "29-05-2020"}

negative_case_result_validation = {"date": "29.05.2020"}

negative_case_input_validation = {"dataaa": "29-05-2020"}


if __name__ == "__main__":
    print(target_function(positive_case))

    try:
        print(target_function(negative_case_result_validation))
    except InputParameterVerificationError as ex:
        print(type(ex), str(ex))

    print(target_function(negative_case_input_validation))
