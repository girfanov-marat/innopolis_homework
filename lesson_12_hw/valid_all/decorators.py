"""Файл с декоратором."""
from typing import Callable, Any

from lesson_12_hw.valid_all.my_exceptions import InputParameterVerificationError, ResultVerificationError, \
    RepeatTimesZero


def valid_all_decorator(input_validation: Callable,
                        result_validation: Callable,
                        on_fail_repeat_times: int = 1,
                        default_behavior: Callable = None) -> Callable:
    """Декоратор для валидации функции."""
    def my_decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if input_validation(*args, **kwargs):
                res = func(*args, **kwargs)
                if on_fail_repeat_times == 0:
                    raise RepeatTimesZero
                if result_validation(res):
                    return res
                else:
                    if not default_behavior:
                        raise ResultVerificationError("Ошибка работы функции, результаты не совпадают")
                    else:
                        if on_fail_repeat_times == -1:
                            while not result_validation(res):
                                res = func(*args, **kwargs)
                            return res
                        else:
                            for i in range(on_fail_repeat_times):
                                res = func(*args, **kwargs)
                                if result_validation(res):
                                    return res
                                else:
                                    print(f"Результат {res} не прошёл валидацию")
                            default_behavior()
            else:
                raise InputParameterVerificationError('Ошибка валидации входных параметров: ', *args, **kwargs)
        return wrapper
    return my_decorator
