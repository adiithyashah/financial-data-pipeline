import requests
import psycopg2

# step 1: Fetch the current price of Bitcoin in USD from CoinGecko API
url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)
data = response.json()

symbol = "bitcoin"
price = data["bitcoin"]["usd"]
currency = "usd"

# Step 2: Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="financial_data",
    user="postgres",
    password="Adithya@2002",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Step 3: Insert data into table
cursor.execute(
    """
    INSERT INTO prices (symbol, price, currency)
    VALUES (%s, %s, %s)
    """,
    (symbol, price, currency)
)

conn.commit()

print("Inserted price successfully!")
print(f"Symbol: {symbol}, Price: {price}, Currency: {currency}")

# Step 4: Close connection
cursor.close()
conn.close()