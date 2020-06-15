"""All utilities."""
import random
import re
import jsonschema
import requests

regex = "[a-z0-9]{2,5}"
all_stats = ["Обрабатывается", "Выполняется", "Доставлено"]

schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "identifier": {
      "type": "string"
    },
    "status": {
      "type": "string"
    }
  },
  "required": [
    "identifier",
    "status"
  ]
}


def validate_input(d_id: str, d_status: str) -> bool:
    """Validate input data."""
    if 2 <= len(d_id) <= 5:
        if not re.match(regex, d_id):
            return False
        else:
            if d_status in all_stats:
                return True
            else:
                return False
    else:
        return False


def validate_json(input_json: dict) -> bool:
    """JSON validator."""
    try:
        jsonschema.validate(input_json, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False


def unique_code():
    """Generate unique identifier."""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    code = ""
    for i in range(random.randint(2, 5)):
        code += chars[random.randint(0, len(chars)) - 1]
    return code


def json_generator():
    """Generate JSON for performance testing."""
    json = {
        "identifier": unique_code(),
        "status": all_stats[random.randint(0, 2)]
    }
    return json


if __name__ == "__main__":
    url = "http://localhost:8080/add"

    data = {
        "identifier": "aweg4",
        "status": "Обрабатывается",
    }

    response = requests.request("POST", url, json=data)
    print(response.text)
