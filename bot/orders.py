from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()
client = BinanceClient()

def place_market_order(symbol, side, quantity):
    try:
        response = client.place_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Market Order Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Market Order Error: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        response = client.place_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logger.info(f"Limit Order Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Limit Order Error: {str(e)}")
        raise
