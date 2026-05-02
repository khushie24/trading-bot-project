# 📈 Trading Bot – Binance Futures Testnet

## 🚀 Overview

This project is a **Python-based trading bot** that interacts with the **Binance Futures Testnet (USDT-M)**.
It allows users to place **Market and Limit orders** via a command-line interface (CLI) with proper validation, logging, and error handling.

---

## 🎯 Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL** sides
* CLI-based input using arguments
* Input validation (symbol, quantity, price, etc.)
* Structured and modular code
* Detailed logging of:

  * API requests
  * API responses
  * Errors and exceptions
* Clear console output for order execution

---

## 🛠️ Tech Stack

* Python 3.x
* `requests` / `python-binance` (depending on implementation)
* `argparse` (for CLI)
* Logging module

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
├── logs/
│   ├── market_order.log
│   ├── limit_order.log
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/khushie24/trading-bot-project.git
cd trading-bot-project
```

### 2️⃣ Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 🔐 API Configuration

1. Go to Binance Futures Testnet
2. Generate API Key and Secret
3. Add them in your project:

Example:

```
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
BASE_URL = "https://testnet.binancefuture.com"
```

---

## ▶️ How to Run

### 🔹 Market Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### 🔹 Limit Order Example

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
```

---

## 📤 Sample Output

```
Order Request:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

Order Response:
Order ID: 12345678
Status: FILLED
Executed Quantity: 0.01
Average Price: 59000

✅ Order executed successfully
```

---

## 📜 Logging

* Logs are stored in the `/logs` directory
* Includes:

  * API request details
  * API responses
  * Errors and exceptions

---

## ⚠️ Error Handling

The application handles:

* Invalid input (wrong symbol, missing price, etc.)
* API errors (invalid credentials, insufficient balance)
* Network failures

---

## 📌 Assumptions

* User has a valid Binance Futures Testnet account
* API keys are correctly configured
* Internet connection is stable

---

## 🧪 Test Cases Included

* ✅ One successful MARKET order
* ✅ One successful LIMIT order
* Logs attached for both

---

## 🌟 Bonus Features (if implemented)

* Enhanced CLI validation messages
* Additional order type (optional)
* Improved user experience

---

## 🙌 Conclusion

This project demonstrates:

* API integration
* Clean architecture
* Error handling & logging
* CLI-based interaction

---

## 📬 Submission

* GitHub Repository (Public)
* Includes:

  * Source code
  * README
  * requirements.txt
  * Log files

---
