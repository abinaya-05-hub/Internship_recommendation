import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="internship_db",
    user="postgres",
    password="Abinaya_05",
    port="5432"
)

cursor = conn.cursor()

query = """
INSERT INTO internships
(company, title, location, employment_type, description, url, source, posted_date)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

data = (
    "Test Company",
    "Python Developer Intern",
    "Remote - India",
    "Internship",
    "Python development internship",
    "https://example.com/test",
    "Test",
    None
)

cursor.execute(query, data)

conn.commit()

print("Internship inserted successfully!")

cursor.close()
conn.close()