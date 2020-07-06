"""Функции для работы с моделью клиентов."""
from typing import Any

from models import Client, Session

session = Session()


def client_data(values: dict) -> Client:
    """Создание объекта класса Client с полученным параметрами."""
    to_insert = Client(name=values["name"],
                       is_vip=values["is_vip"])
    return to_insert


def insert_client(data: Client) -> None:
    """Добавление клиента в бд."""
    client = session.query(Client).filter_by(name=data.name).first()
    if client:
        session.delete(client)
    session.add(data)
    session.commit()
    session.close()


def find_client(client_id: int) -> Any:
    """Нахождение клиента в бд по имени."""
    try:
        client = session.query(Client).filter_by(id=client_id).first()
        res = {"id": client.id,
               "name": client.name,
               "is_vip": client.is_vip}
        session.close()
        return res
    except AttributeError:
        session.close()
        return 'Объект в базе не найден'


def delete_client(client_id: int) -> Any:
    """Удаление клиента из бд."""
    try:
        client = session.query(Client).filter_by(id=client_id).first()
        res = {"id": client.id,
               "name": client.name,
               "is_vip": client.is_vip}
        session.delete(client)
        session.commit()
        session.close()
        return res
    except AttributeError:
        session.close()
        return 'Объект в базе не найден'
