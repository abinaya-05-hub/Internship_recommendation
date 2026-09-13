import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="internship_db",
        user="postgres",
        password="Abinaya_05",
        port="5432"
    )

    print("Connected to PostgreSQL successfully!")

    conn.close()

except Exception as e:
    print("Connection failed:")
    print(e)