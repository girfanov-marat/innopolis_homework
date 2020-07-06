"""Реализация ендпоинтов приложения."""
import json

from flask import request, Response

from app import app
from db.clients import find_client, insert_client, client_data, delete_client
from db.drivers import insert_driver, driver_data, delete_driver, find_driver
from db.orders import insert_order, order_data, find_order, update_order_params, get_order_status
from schemes import CLIENTS_SCHEMA, DRIVERS_SCHEMA, ORDERS_SCHEMA
from utilities import json_validate


@app.route('/clients', methods=["GET", "POST", "DELETE"])
def clients() -> Response:
    """Обработка запросов для клиента."""
    if request.method == "POST":
        data = request.get_json()
        if json_validate(data, CLIENTS_SCHEMA):
            insert_client(client_data(data))
            return Response(status=201, response='created!')
    client_id = request.headers.get('clientId')
    if client_id is not None:
        if request.method == "DELETE":
            res = delete_client(client_id)
            status = 200
            message = 'deleted'
        else:
            res = find_client(client_id)
            status = 200
            message = 'successful operation'
        if res == "Объект в базе не найден":
            return Response(status=404, response=res)
        response_dict = dict(message=message, client=res)
        response = json.dumps(response_dict, ensure_ascii=False)
        return Response(status=status, response=response, mimetype='application/json')
    return Response(status=400, response='Неправильный запрос')


@app.route('/drivers', methods=["GET", "POST", "DELETE"])
def drivers() -> Response:
    """Обработка запросов для водителей."""
    if request.method == "POST":
        data = request.get_json()
        if json_validate(data, DRIVERS_SCHEMA):
            insert_driver(driver_data(data))
            return Response(status=201, response='created!')
    driver_id = request.headers.get('driverId')
    if driver_id is not None:
        if request.method == "DELETE":
            res = delete_driver(driver_id)
            status = 200
            message = 'Удалено'
        else:
            res = find_driver(driver_id)
            status = 200
            message = 'successful operation'
        if res == "Объект в базе не найден":
            return Response(status=404, response=res)
        response_dict = dict(message=message, driver=res)
        response = json.dumps(response_dict, ensure_ascii=False)
        return Response(status=status, response=response, mimetype='application/json')
    return Response(status=400, response='Неправильный запрос')


@app.route('/orders', methods=["GET", "POST", "PUT"])
def orders() -> Response:
    """Обработка запросов для заказов."""
    bad_status = False
    if request.method == "POST":
        data = request.get_json()
        if json_validate(data, ORDERS_SCHEMA):
            insert_order(order_data(data))
            return Response(status=201, response='created!')
    order_id = request.headers.get('orderId')
    if order_id is not None:
        if request.method == "PUT":
            update_info = request.get_json()
            new_data = order_data(update_info)
            current_status = get_order_status(order_id)["status"]
            if current_status == "not_accepted":
                if update_info["status"] not in ["not_accepted", "in_progress", "cancelled"]:
                    bad_status = True
            if current_status == "in_progress":
                if update_info["status"] not in ["in_progress", "done", "cancelled"]:
                    bad_status = True
            if current_status == "cancelled":
                bad_status = True
            if current_status == "done":
                bad_status = True
            if bad_status:
                return Response(status=400, response='Неправильный запрос')
            res = update_order_params(order_id, new_data)
            status = 200
            message = 'Изменено!'
            if res == "Объект в базе не найден":
                return Response(status=404, response=res)
        else:
            res = find_order(order_id)
            status = 200
            message = 'successful operation'
            if res == "Объект в базе не найден":
                return Response(status=404, response=res)
        response_dict = dict(message=message, order=res)
        response = json.dumps(response_dict, ensure_ascii=False)
        return Response(status=status, response=response, mimetype='application/json')
    return Response(status=400, response='Неправильный запрос')
