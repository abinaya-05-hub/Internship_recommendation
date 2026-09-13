from database.db import get_connection


def rows_to_dicts(cursor, rows):
    columns = [column[0] for column in cursor.description]

    return [
        dict(zip(columns, row))
        for row in rows
    ]


def get_all_internships():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM internships
        WHERE category = 'Internship'
        ORDER BY id;
    """)

    rows = cursor.fetchall()
    records = rows_to_dicts(cursor, rows)

    cursor.close()
    conn.close()

    return records


def get_all_jobs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM internships
        WHERE category = 'Job'
        ORDER BY id;
    """)

    rows = cursor.fetchall()
    records = rows_to_dicts(cursor, rows)

    cursor.close()
    conn.close()

    return records


def get_remote_jobs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM internships
        WHERE category = 'Job'
        AND work_mode = 'Remote'
        ORDER BY id;
    """)

    rows = cursor.fetchall()
    records = rows_to_dicts(cursor, rows)

    cursor.close()
    conn.close()

    return records


def get_jobs_by_location(location):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM internships
        WHERE category = 'Job'
        AND location ILIKE %s
        ORDER BY id;
    """, (f"%{location}%",))

    rows = cursor.fetchall()
    records = rows_to_dicts(cursor, rows)

    cursor.close()
    conn.close()

    return records