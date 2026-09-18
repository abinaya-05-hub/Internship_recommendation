from database.db import get_connection


conn = get_connection()
cursor = conn.cursor()


print("================================")
print("DATABASE VERIFICATION")
print("================================")


# 1. Total records
cursor.execute("""
    SELECT COUNT(*)
    FROM internships
""")

total = cursor.fetchone()[0]

print("\nTotal records:", total)


# 2. Records by source
cursor.execute("""
    SELECT source, COUNT(*)
    FROM internships
    GROUP BY source
    ORDER BY source
""")

print("\n===== RECORDS BY SOURCE =====")

for source, count in cursor.fetchall():
    print(f"{source}: {count}")


# 3. Workday records
cursor.execute("""
    SELECT COUNT(*)
    FROM internships
    WHERE source = 'Workday'
""")

workday_count = cursor.fetchone()[0]

print("\nWorkday records:", workday_count)


# 4. Sample Workday records
cursor.execute("""
    SELECT
        id,
        company,
        title,
        location,
        source,
        source_job_id
    FROM internships
    WHERE source = 'Workday'
    LIMIT 5
""")

print("\n===== SAMPLE WORKDAY JOBS =====")

for job in cursor.fetchall():

    print("\n-------------------------")
    print("ID:", job[0])
    print("Company:", job[1])
    print("Title:", job[2])
    print("Location:", job[3])
    print("Source:", job[4])
    print("Source Job ID:", job[5])


cursor.close()
conn.close()