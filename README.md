Trading Bot

Binance Futures Testnet





Submitted by - Suryansh

Role applying for - Python Developer Intern Candidate

 

Key Highlights

• Fully functional CLI-based trading bot using Binance Futures Testnet

• Supports both MARKET and LIMIT orders with BUY/SELL operations

• Robust error handling for API failures, invalid inputs, and trading constraints

• Structured modular codebase for scalability and maintainability

• Comprehensive logging of requests, responses, and errors

• Demonstrates real-world debugging (timestamp sync, notional limits, price filters)

Overview

This project is a Python-based command-line trading bot designed to interact with Binance Futures Testnet. It enables users to place MARKET and LIMIT orders while maintaining a clean architecture and production-oriented practices.

Project Structure

trading\_bot/

&#x20; bot/

&#x20;   client.py

&#x20;   orders.py

&#x20;   validators.py

&#x20;   logging\_config.py

&#x20; cli.py

&#x20; requirements.txt

&#x20; trading.log

&#x20; README.md

Setup Instructions

1\. Clone the repository

2\. Install dependencies using pip install -r requirements.txt

3\. Create a .env file with API\_KEY and API\_SECRET

4\. Ensure system time is synchronized

How to Run

Market Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002



Limit Order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000

Features

• MARKET and LIMIT order support

• BUY and SELL operations

• CLI input validation

• Logging and exception handling

• Modular architecture

Logging

All trading activities including requests, responses, and errors are recorded in trading.log for traceability and debugging.

Assumptions \& Notes

• Minimum order notional value is approximately 100 USDT

• Testnet environment may behave differently from real markets

• Some orders may remain pending due to simulated liquidity

Dependencies

python-binance==1.0.36

python-dotenv==1.0.1



# trading_bot
