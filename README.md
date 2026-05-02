# Binance Futures Testnet Trading Bot

## Setup

1. Install Python 3.x
2. Install dependencies:
   pip install -r requirements.txt

3. Set environment variables:

Windows:
set BINANCE_API_KEY=your_key
set BINANCE_API_SECRET=your_secret

Mac/Linux:
export BINANCE_API_KEY=your_key
export BINANCE_API_SECRET=your_secret

## Run Examples

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Features
- Market & Limit orders
- CLI input validation
- Logging
- Error handling
