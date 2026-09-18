from db import get_connection


conn = get_connection()
cursor = conn.cursor()

print("================================")
print("CHECKING DATABASE COLUMN LENGTHS")
print("================================")

cursor.execute("""
    SELECT
        column_name,
        data_type,
        character_maximum_length
    FROM information_schema.columns
    WHERE table_name = 'internships'
    ORDER BY ordinal_position
""")

columns = cursor.fetchall()

for column in columns:
    print(column)

cursor.close()
conn.close()