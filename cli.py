import argparse
import logging

from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        # ✅ Validate inputs
        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # 📌 Request Summary
        print("\n================ ORDER REQUEST ================")
        print(f"Symbol     : {args.symbol.upper()}")
        print(f"Side       : {args.side.upper()}")
        print(f"Type       : {args.type.upper()}")
        print(f"Quantity   : {args.quantity}")
        print(f"Price      : {args.price if args.price else 'N/A'}")
        print("===============================================")

        logging.info(f"Request: {vars(args)}")

        # 🚀 Place Order
        order = place_order(
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        # ❌ Error Handling
        if "error" in order:
            print("\n❌ ORDER FAILED")
            print(f"Reason: {order['error']}")
            logging.error(order["error"])
            return

        # 📊 Response Output
        print("\n================ ORDER RESPONSE ===============")
        print(f"Order ID   : {order.get('orderId')}")
        print(f"Status     : {order.get('status')}")
        print(f"ExecutedQty: {order.get('executedQty')}")
        print(f"Avg Price  : {order.get('avgPrice', 'N/A')}")
        print("===============================================")

        logging.info(f"Response: {order}")

        # ✅ Final Status Message
        if order.get("status") == "FILLED":
            print("\n✅ SUCCESS: Order fully executed")
        else:
            print("\n⚠️ NOTE: Order placed but not fully executed yet")

    except Exception as e:
        print("\n❌ ERROR")
        print(str(e))
        logging.error(str(e))


if __name__ == "__main__":
    main()