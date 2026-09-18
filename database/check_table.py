from db import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = 'internships'
    ORDER BY ordinal_position
""")

columns = cursor.fetchall()

print("================================")
print("INTERNSHIPS TABLE STRUCTURE")
print("================================")

for column in columns:
    print(column)

cursor.close()
conn.close()