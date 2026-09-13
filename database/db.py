import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="internship_db",
        user="postgres",
        password="Abinaya_05",
        port="5432"
    )