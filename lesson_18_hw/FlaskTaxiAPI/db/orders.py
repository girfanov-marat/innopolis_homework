"""Функции для работы с моделю заказов."""
import datetime
from typing import Any

from models import Orders, Session

session = Session()


def order_data(values: dict) -> Orders:
    """Создание объекта класса Orders с полученным параметрами."""
    if isinstance(values["date_created"], str):
        values["date_created"] = datetime.datetime.strptime(values["date_created"], "%Y-%m-%dT%H:%M:%SZ")
    to_insert = Orders(address_from=values["address_from"],
                       address_to=values["address_to"],
                       client_id=values["client_id"],
                       driver_id=values["driver_id"],
                       date_created=values["date_created"],
                       status=values["status"])
    return to_insert


def insert_order(data: Orders) -> None:
    """Добавление клиента в бд."""
    session.add(data)
    session.commit()
    session.close()


def find_order(order_id: int) -> Any:
    """Нахождение клиента в бд по имени."""
    try:
        order = session.query(Orders).filter_by(id=order_id).first()
        res = {'id': order.id,
               'address_from': order.address_from,
               'address_to': order.address_to,
               'client_id': order.client_id,
               'driver_id': order.driver_id,
               'date_created': datetime.datetime.date(order.date_created).strftime("%Y-%m-%dT%H:%M:%SZ"),
               'status': order.status}
        session.close()
        return res
    except AttributeError:
        session.close()
        return 'Объект в базе не найден'


def get_order_status(order_id: int) -> Any:
    """Узнать статус заказа по id."""
    try:
        order = session.query(Orders).filter_by(id=order_id).first()
        res = {'status': order.status}
        session.close()
        return res
    except AttributeError:
        session.close()
        return 'Объект в базе не найден'


def update_order_status(order_id: int, status: str) -> Any:
    """Апдейт статуса заказа."""
    if status in ['not_accepted', 'in_progress', 'done', 'cancelled']:
        try:
            order = session.query(Orders).filter_by(id=order_id).first()
            res = {'id': order.id,
                   'address_from': order.address_from,
                   'address_to': order.address_to,
                   'client_id': order.client_id,
                   'driver_id': order.driver_id,
                   'date_created': order.date_created,
                   'status': status}
            data = order_data(res)
            session.query(Orders).filter_by(id=order_id).update({Orders.status: data.status})
            res.update({"date_created": datetime.datetime.date(order.date_created).strftime("%Y-%m-%dT%H:%M:%SZ")})
            session.commit()
            session.close()
            return res
        except AttributeError:
            session.close()
            return 'Объект в базе не найден'
    else:
        session.close()
        return 'Некорретный запрос'


def update_order_params(order_id: int, data) -> Any:
    """Апдейт данных заказа."""
    try:
        order = session.query(Orders).filter_by(id=order_id).first()
        if order.status == "not_accepted":
            session.query(Orders).filter_by(id=order_id).update({Orders.driver_id: data.driver_id,
                                                                 Orders.client_id: data.client_id,
                                                                 Orders.date_created: data.date_created,
                                                                 Orders.address_from: data.address_from,
                                                                 Orders.address_to: data.address_to,
                                                                 Orders.status: data.status})
        else:
            session.query(Orders).filter_by(id=order_id).update({Orders.address_from: data.address_from,
                                                                 Orders.address_to: data.address_to,
                                                                 Orders.status: data.status})
        res = {'id': order.id,
               'address_from': order.address_from,
               'address_to': order.address_to,
               'client_id': order.client_id,
               'driver_id': order.driver_id,
               'date_created': order.date_created,
               'status': order.status}
        res.update({"date_created": datetime.datetime.date(order.date_created).strftime("%Y-%m-%dT%H:%M:%SZ")})
        session.commit()
        session.close()
        return res
    except AttributeError:
        session.close()
        return 'Объект в базе не найден'
