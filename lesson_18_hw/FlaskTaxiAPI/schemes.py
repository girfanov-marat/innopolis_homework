"""Схемы json."""
DRIVERS_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "car": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "car"
  ]
}

CLIENTS_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "is_vip": {
      "type": "boolean"
    }
  },
  "required": [
    "name",
    "is_vip"
  ]
}


ORDERS_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "driver_id": {
      "type": "string"
    },
    "date_created": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "address_from": {
      "type": "string"
    },
    "address_to": {
      "type": "string"
    }
  },
  "required": [
    "client_id",
    "driver_id",
    "date_created",
    "status",
    "address_from",
    "address_to"
  ]
}