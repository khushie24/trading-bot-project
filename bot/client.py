from binance.client import Client
import os

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(self.api_key, self.api_secret, testnet=True)

    def place_order(self, **params):
        return self.client.futures_create_order(**params)
