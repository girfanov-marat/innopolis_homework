"""Файл для доп функций."""
import jsonschema


def json_validate(json: dict, schema: dict) -> bool:
    """Валидация JSON."""
    try:
        jsonschema.validate(json, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False
