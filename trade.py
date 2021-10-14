"""
This module should contain all the post functions to be used with the Alpaca API.
In the future, this will only be used for that purpose. Getters, constant variables,
and other unrelated functions and variables will be located in another module.

Idea: I will have an object (module) just to continuously scan stock(s). Once the
module finds a pattern, or is reasonably confident that a trade will work, then it
initialize a new trade object.
"""
import json
import requests
from config import *


class Trade(object):

    def __init__(self, symbol, qty, side, type, time_in_force):
        self.symbol = symbol
        self.qty = qty
        self.side = side
        self.type = type
        self.time_in_force = time_in_force

    BASE_URL = "https://paper-api.alpaca.markets"
    ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
    ORDERS_URL = "{}/v2/orders".format(BASE_URL)
    HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}

    # def main():
    #     """
    #     All function calls will go here. Use this when you want to execute code.
    #     """
    #     # Ex: print(create_order("AAPL", 1, "buy", "market", "gtc"))

    def create_order(self, symbol, qty, side, type, time_in_force):
        """
        :var data: Dictionary of parameters
        :returns: Dictionary of order parameters from Alpaca
        """
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": type,
            "time_in_force": time_in_force
        }
        r = requests.post(Trade.ORDERS_URL, json=data, headers=Trade.HEADERS)
        return json.loads(r.content)

    @staticmethod
    def get_account():
        r = requests.get(Trade.ACCOUNT_URL, headers=Trade.HEADERS)
        return json.loads(r.content)

    @staticmethod
    def get_orders():
        r = requests.get(Trade.ORDERS_URL, headers=Trade.HEADERS)
        return json.loads(r.content)

    # if __name__ == "__main__":
    #     main()
