import logging

# Set up logging
logging.basicConfig(
    filename='pepeai.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Starting PepeAI bot...")

# Try to import ccxt
try:
    import ccxt
    logging.info("ccxt module loaded successfully.")
except ImportError:
    ccxt = None
    logging.warning("ccxt module not found. Running in limited mode.")

# Function to fetch token data
def fetch_token_data():
    if ccxt is None:
        logging.warning("Skipping token fetch due to missing ccxt.")
        return None
    try:
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker('BTC/USDT')
        logging.info(f"Fetched BTC/USDT price: {ticker['last']}")
        return ticker
    except Exception as e:
        logging.error(f"Error fetching token data: {e}")
        return None

# Main execution
if __name__ == '__main__':
    logging.info("PepeAI bot is running.")
    data = fetch_token_data()
    if data:
        print(f"BTC/USDT Price: {data['last']}")
    else:
        print("Running in limited mode. Token data not available.")
