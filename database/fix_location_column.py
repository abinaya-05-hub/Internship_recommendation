from db import get_connection


conn = get_connection()
cursor = conn.cursor()

print("================================")
print("FIXING LOCATION COLUMN")
print("================================")

cursor.execute("""
    ALTER TABLE internships
    ALTER COLUMN location TYPE TEXT
""")

conn.commit()

print("\nLocation column changed to TEXT successfully.")

cursor.close()
conn.close()