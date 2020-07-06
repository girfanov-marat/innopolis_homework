"""Функции для работы с моделью водителей."""
from typing import Any

from models import Drivers, Session

session = Session()


def driver_data(values: dict) -> Drivers:
    """Создание объекта класса Drivers с полученным параметрами."""
    to_insert = Drivers(name=values["name"],
                        car=values["car"])
    return to_insert


def insert_driver(data: Drivers) -> None:
    """Добавление водителя в бд."""
    client = session.query(Drivers).filter_by(name=data.name).first()
    if client:
        session.delete(client)
    session.add(data)
    session.commit()
    session.close()


def find_driver(driver_id: str) -> Any:
    """Нахождение водителя в бд по имени."""
    try:
        driver = session.query(Drivers).filter_by(id=driver_id).first()
        res = {"id": driver.id,
               "name": driver.name,
               "car": driver.car}
        session.close()
        return res
    except AttributeError:
        session.close()
        return 'Объект в базе не найден'


def delete_driver(driver_id: str) -> Any:
    """Удаление водителя из бд."""
    try:
        driver = session.query(Drivers).filter_by(id=driver_id).first()
        res = {"id": driver.id,
               "name": driver.name,
               "car": driver.car}
        session.delete(driver)
        session.commit()
        session.close()
        return res
    except AttributeError:
        session.close()
        return 'Объект в базе не найден'
