import json
from db import get_connection


INPUT_FILE = "data/final_jobs_classified.json"


def insert_final_dataset():

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        jobs = json.load(file)


    print("================================")
    print("FINAL DATASET → POSTGRESQL")
    print("================================")

    print(f"\nRecords to insert: {len(jobs)}")


    conn = get_connection()
    cursor = conn.cursor()


    # --------------------------------
    # Clear current main table
    # --------------------------------

    print("\nClearing existing internships table...")

    cursor.execute("""
        DELETE FROM internships
    """)

    print(
        f"Deleted existing records: {cursor.rowcount}"
    )


    # --------------------------------
    # Insert final dataset
    # --------------------------------

    query = """
        INSERT INTO internships (
            company,
            title,
            location,
            employment_type,
            description,
            url,
            source,
            posted_date,
            work_mode,
            category,
            department,
            source_job_id
        )
        VALUES (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
    """


    inserted = 0


    for job in jobs:

        values = (
            job.get("company_name"),
            job.get("title"),
            job.get("location"),
            job.get("employment_type"),
            job.get("description"),
            job.get("apply_url"),
            job.get("source"),
            job.get("published_date"),
            job.get("work_mode"),
            job.get("category"),
            job.get("department"),
            job.get("source_job_id")
        )

        cursor.execute(query, values)

        inserted += 1


    conn.commit()


    print("\n================================")
    print("INSERTION COMPLETE")
    print("================================")

    print(f"Records inserted: {inserted}")


    # --------------------------------
    # Verify database count
    # --------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM internships
    """)

    total = cursor.fetchone()[0]

    print(f"Database total: {total}")


    cursor.execute("""
        SELECT category, COUNT(*)
        FROM internships
        GROUP BY category
        ORDER BY category
    """)

    print("\n===== DATABASE CATEGORIES =====")

    for category, count in cursor.fetchall():

        print(
            f"{category}: {count}"
        )


    cursor.close()
    conn.close()


if __name__ == "__main__":
    insert_final_dataset()