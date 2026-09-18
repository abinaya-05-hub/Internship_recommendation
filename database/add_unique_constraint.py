from db import get_connection


conn = get_connection()
cursor = conn.cursor()


print("================================")
print("ADDING DATABASE DUPLICATE PROTECTION")
print("================================")


cursor.execute("""
    ALTER TABLE internships
    ADD CONSTRAINT unique_source_job
    UNIQUE (source, source_job_id)
""")


conn.commit()


print("\nUnique constraint added successfully.")

cursor.close()
conn.close()