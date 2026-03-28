from bot.client import get_client
import logging
import time

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing {order_type} order: {symbol} {side} {quantity} price={price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=float(quantity)
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=float(quantity),
                price=str(price),
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        # Wait and fetch updated status
        time.sleep(2)

        updated_order = client.futures_get_order(
            symbol=symbol,
            orderId=order["orderId"]
        )

        logging.info(f"Order Response: {updated_order}")

        return updated_order

    except Exception as e:
        logging.error(str(e))
        return {"error": str(e)}