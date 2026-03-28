#  Trading Bot – Binance Futures Testnet

## Author
**Suryansh**  
Python Developer Intern Candidate  

---

##  Key Highlights

- Fully functional CLI-based trading bot using Binance Futures Testnet  
- Supports both **MARKET** and **LIMIT** orders with BUY/SELL operations  
- Clean modular architecture (client, orders, validators, CLI)  
- Robust error handling for API failures and invalid inputs  
- Comprehensive logging of requests, responses, and errors  
- Handles real-world trading constraints:
  - Timestamp synchronization issues  
  - Minimum notional value (~100 USDT)  
  - Binance price band restrictions  

---

##  Problem Statement

The objective of this project is to build a Python application that interacts with the Binance Futures Testnet to:

- Place MARKET and LIMIT orders  
- Accept user inputs via CLI  
- Provide structured output and logging  
- Handle real-world API constraints and failures  

---

##  Approach & Design

The application follows a **layered architecture**:

### 1. Client Layer (`client.py`)
- Handles API authentication  
- Connects to Binance Futures Testnet  
- Manages timestamp synchronization  

### 2. Order Layer (`orders.py`)
- Implements order placement logic  
- Supports MARKET and LIMIT orders  
- Fetches updated order status  

### 3. Validation Layer (`validators.py`)
- Validates:
  - Order type  
  - Side (BUY/SELL)  
  - Quantity  
  - Price (for LIMIT orders)  

### 4. CLI Layer (`cli.py`)
- Parses user input using argparse  
- Displays structured request & response  
- Handles user-facing errors  

### 5. Logging Layer (`logging_config.py`)
- Logs:
  - API requests  
  - Responses  
  - Errors  

---

##  Project Structure
```  trading_bot/
│
├── bot/
│ ├── __init__.py
│ ├── client.py # Binance client setup
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ ├── logging_config.py # Logging configuration
│
├── cli.py # CLI entry point
├── requirements.txt
├── trading.log # Generated log file
└── README.md
```
The project follows a modular architecture separating API interaction, business logic, validation, and CLI handling.
## How to Run
##  Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/suryanshsah1665/trading_bot.git
cd trading_bot
```

2 Install dependencies: 
```bash 
pip install -r requirements.txt
```
3. Create a .env file:
```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key
```
4. Ensure system time is synchronized

MARKET Order
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
``` 
LIMIT Order
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000
```
## Sample Output

### Market Order
```
================ ORDER REQUEST ================
Symbol : BTCUSDT
Side : BUY
Type : MARKET
Quantity : 0.002
Price : N/A
================ ORDER RESPONSE ===============
Order ID : 13002230029
Status : FILLED
ExecutedQty: 0.002
Avg Price : 66650.00000

SUCCESS: Order fully executed
```
### Limit Order
```
================ ORDER REQUEST ================
Symbol : BTCUSDT
Side : SELL
Type : LIMIT
Quantity : 0.002
Price : 65000
================ ORDER RESPONSE ===============
Order ID : 13002239363
Status : FILLED
ExecutedQty: 0.002
Avg Price : 66924.90000

SUCCESS: Order fully executed
```
