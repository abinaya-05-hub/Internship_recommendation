from database.queries import (
    get_all_internships,
    get_all_jobs,
    get_remote_jobs,
    get_jobs_by_location
)


print("===== INTERNSHIPS =====")

internships = get_all_internships()

for internship in internships:
    print(internship["id"], "-", internship["title"])


print("\n===== JOBS =====")

jobs = get_all_jobs()

for job in jobs:
    print(job["id"], "-", job["title"])


print("\n===== REMOTE JOBS =====")

remote_jobs = get_remote_jobs()

for job in remote_jobs:
    print(job["id"], "-", job["title"])


print("\n===== INDIA JOBS =====")

india_jobs = get_jobs_by_location("India")

for job in india_jobs:
    print(job["id"], "-", job["title"])