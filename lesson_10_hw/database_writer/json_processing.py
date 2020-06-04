"""Файл для работы с JSON."""

import jsonschema
import json

my_file = 'example.json'

schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "id": 123,
            "name": "Телевизор",
            "package_params": {
                "width": 5,
                "height": 10
            },
            "location_and_quantity": [
                {
                    "location": "Магазин на Ленина",
                    "amount": 7
                },
                {
                    "location": "Магазин в центре",
                    "amount": 3
                }
            ]
        }
    ],
    "required": [
        "id",
        "name",
        "package_params",
        "location_and_quantity"
    ],
    "additionalProperties": False,
    "properties": {
        "id": {
            "$id": "#/properties/id",
            "type": "integer",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                123
            ]
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Телевизор"
            ]
        },
        "package_params": {
            "$id": "#/properties/package_params",
            "type": "object",
            "title": "The package_params schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "width": 5,
                    "height": 10
                }
            ],
            "required": [
                "width",
                "height"
            ],
            "additionalProperties": True,
            "properties": {
                "width": {
                    "$id": "#/properties/package_params/properties/width",
                    "type": "integer",
                    "title": "The width schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        5
                    ]
                },
                "height": {
                    "$id": "#/properties/package_params/properties/height",
                    "type": "integer",
                    "title": "The height schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        10
                    ]
                }
            }
        },
        "location_and_quantity": {
            "$id": "#/properties/location_and_quantity",
            "type": "array",
            "title": "The location_and_quantity schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "location": "Магазин на Ленина",
                        "amount": 7
                    },
                    {
                        "location": "Магазин в центре",
                        "amount": 3
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/location_and_quantity/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "location": "Магазин на Ленина",
                                "amount": 7
                            }
                        ],
                        "required": [
                            "location",
                            "amount"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "location": {
                                "$id": "#/properties/location_and_quantity/items/anyOf/0/properties/location",
                                "type": "string",
                                "title": "The location schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "Магазин на Ленина"
                                ]
                            },
                            "amount": {
                                "$id": "#/properties/location_and_quantity/items/anyOf/0/properties/amount",
                                "type": "integer",
                                "title": "The amount schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    7
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/location_and_quantity/items"
            }
        }
    }
}

with open(my_file, encoding="utf-8") as f:
    json_content = json.load(f)


def validate_json(input_json: dict) -> bool:
    """Валидация JSON."""
    try:
        jsonschema.validate(input_json, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False


intermediate_dict = dict()
dicts = list()


def dict_parser(my_dict: dict) -> list:
    """Парсинг JSON."""
    id_goods = 0
    for k, v in my_dict.items():
        if k == "id":
            id_goods = v
        if isinstance(v, dict):
            dict_parser(v)
        if isinstance(v, list):
            for i in range(len(v)):
                if k == "location_and_quantity":
                    v[i].update({"id_good": id_goods})
                    dicts.append(v[i])
        if isinstance(v, str) or isinstance(v, int):
            intermediate_dict.update({k: v})
    if intermediate_dict not in dicts:
        dicts.append(intermediate_dict)
    return dicts
