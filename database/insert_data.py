import json
from db import get_connection


def insert_internships():
    # Read normalized internship data
    with open(
        "data/normalized_internships.json",
        "r",
        encoding="utf-8"
    ) as file:
        internships = json.load(file)

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

    for internship in internships:
        values = (
            internship.get("company_name"),
            internship.get("title"),
            internship.get("location"),
            internship.get("employment_type"),
            internship.get("description"),
            internship.get("apply_url"),
            internship.get("source"),
            internship.get("published_date"),
            internship.get("work_mode"),
            internship.get("category"),
            internship.get("department"),
            internship.get("source_job_id")
        )

        cursor.execute(query, values)

    conn.commit()

    print(f"{len(internships)} internship records processed successfully!")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    insert_internships()