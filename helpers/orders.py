import requests
import allure

from helpers.urls import BASE_URL


@allure.step('Create order')
def create_order(payload):
    return requests.post(
        f'{BASE_URL}/api/v1/orders',
        json=payload
    )


@allure.step('Cancel order')
def cancel_order(track):
    return requests.put(
        f'{BASE_URL}/api/v1/orders/cancel',
        json={'track': track}
    )


@allure.step('Get orders list')
def get_orders_list(params=None):
    return requests.get(
        f'{BASE_URL}/api/v1/orders',
        params=params
    )