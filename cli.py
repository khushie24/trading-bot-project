import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import *

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        print("\n--- Order Summary ---")
        print(vars(args))

        if args.type == "MARKET":
            response = place_market_order(args.symbol, args.side, args.quantity)

        elif args.type == "LIMIT":
            if not args.price:
                raise ValueError("Price required for LIMIT order")
            response = place_limit_order(args.symbol, args.side, args.quantity, args.price)

        print("\n--- Order Response ---")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
