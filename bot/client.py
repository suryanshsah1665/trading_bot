from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET"),
        testnet=True
    )
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    client.TIME_OFFSET = client.get_server_time()['serverTime'] - int(__import__('time').time() * 1000)

    return client