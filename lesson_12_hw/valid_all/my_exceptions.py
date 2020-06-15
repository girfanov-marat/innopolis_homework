"""Файл с исключениями."""
from typing import Any


class InputParameterVerificationError(Exception):
    """Исключения вызываемое при провале валидации входных параметров."""

    def __init__(self, text: str, arguments: Any) -> None:
        """Конструктор класса."""
        self.arguments = arguments
        self.text = text

    def __str__(self) -> str:
        """Изменение формата вывода."""
        return self.text + str(self.arguments)


class ResultVerificationError(Exception):
    """Исключения вызываемое при провале валидации результата выполнения функции."""

    pass


class RepeatTimesZero(Exception):
    """Исключение вызываемое при случае, когда параметр on_fail_repeat_times == 0."""

    pass





