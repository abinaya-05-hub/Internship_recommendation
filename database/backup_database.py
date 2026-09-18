from db import get_connection


def backup_database():

    conn = get_connection()
    cursor = conn.cursor()

    print("================================")
    print("DATABASE BACKUP")
    print("================================")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS internships_backup
        AS TABLE internships
    """)

    conn.commit()

    cursor.execute("""
        SELECT COUNT(*)
        FROM internships_backup
    """)

    count = cursor.fetchone()[0]

    print(f"\nBackup records: {count}")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    backup_database()