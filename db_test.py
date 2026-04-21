import psycopg2

conn = psycopg2.connect(
    dbname="financial_data",
    user="postgres",
    password="Adithya@2002",
    host="localhost",
    port="5432"
)

print("Database connection successful!")

conn.close()