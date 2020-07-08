"""Для проверки приложения."""
import requests
import datetime


class Client:
    client_url = "http://localhost:5000/clients"

    def create_client(self, name: str, status: bool):
        data_client = {
            "name": name,
            "is_vip": status
        }
        response = requests.request("POST", self.client_url, json=data_client)
        print(response.text, response.status_code)

    def get_client(self, client_id: str):
        headers = {'clientId': client_id}
        response = requests.request("GET", self.client_url, headers=headers)
        print(response.text, response.status_code)

    def delete_client(self, client_id: str):
        headers = {'clientId': client_id}
        response = requests.request("DELETE", self.client_url, headers=headers)
        print(response.text, response.status_code)


class Driver:
    driver_url = "http://localhost:5000/drivers"

    def create_driver(self, name: str, car: str):
        data_driver = {
            "name": name,
            "car": car
        }
        response = requests.request("POST", self.driver_url, json=data_driver)
        print(response.text, response.status_code)

    def get_driver(self, driver_id: str):
        headers = {'driverId': driver_id}
        response = requests.request("GET", self.driver_url, headers=headers)
        print(response.text, response.status_code)

    def delete_driver(self, driver_id: str):
        headers = {'driverId': driver_id}
        response = requests.request("DELETE", self.driver_url, headers=headers)
        print(response.text, response.status_code)


class Orders:
    orders_url = "http://localhost:5000/orders"
    current_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    def create_order(self, driver_id: str, address_from: str, address_to: str, client_id: str,status: str):
        data_order = {
            'address_from': address_from,
            'address_to': address_to,
            'client_id': client_id,
            'driver_id': driver_id,
            'date_created': self.current_time,
            'status': status
        }
        response = requests.request("POST", self.orders_url, json=data_order)
        print(response.text, response.status_code)

    def get_order(self, order_id: str):
        headers = {'orderId': order_id}
        response = requests.request("GET", self.orders_url, headers=headers)
        print(response.text, response.status_code)

    def update_order(self, order_id:str, driver_id: str, address_from: str, address_to: str, client_id: str,
                     status: str):
        data_order = {
            'address_from': address_from,
            'address_to': address_to,
            'client_id': client_id,
            'driver_id': driver_id,
            'date_created': self.current_time,
            'status': status
        }
        headers = {'orderId': order_id}
        response = requests.request("PUT", self.orders_url, headers=headers, json=data_order)
        print(response.text, response.status_code)


driver = Driver()
client = Client()
order = Orders()

