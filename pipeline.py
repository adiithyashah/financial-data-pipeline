import os
import requests
import psycopg2
from dotenv import load_dotenv


load_dotenv()


def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    symbol = "bitcoin"
    price = data["bitcoin"]["usd"]
    currency = "usd"

    return symbol, price, currency


def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return conn


def insert_price(symbol, price, currency):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prices (symbol, price, currency)
        VALUES (%s, %s, %s)
        """,
        (symbol, price, currency)
    )

    conn.commit()
    cursor.close()
    conn.close()


def main():
    symbol, price, currency = fetch_bitcoin_price()
    insert_price(symbol, price, currency)
    print("Pipeline ran successfully!")
    print(f"Inserted: {symbol}, {price}, {currency}")


if __name__ == "__main__":
    main()