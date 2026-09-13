import json
from db import get_connection


def insert_jobs():
    with open(
        "data/normalized_jobs.json",
        "r",
        encoding="utf-8"
    ) as file:
        jobs = json.load(file)

    conn = get_connection()
    cursor = conn.cursor()

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
        ON CONFLICT (url) DO NOTHING
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

        if cursor.rowcount == 1:
            inserted += 1

    conn.commit()

    print(f"{inserted} new job records inserted.")
    print(f"{len(jobs)} job records processed.")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    insert_jobs()