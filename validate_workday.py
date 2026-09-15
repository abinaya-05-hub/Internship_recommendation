import json


file_path = "data/workday_jobs.json"

with open(file_path, "r", encoding="utf-8") as file:
    jobs = json.load(file)


print("================================")
print("WORKDAY DATA VALIDATION")
print("================================")

# 1. Total records
print("\nTotal jobs:", len(jobs))


# 2. Check duplicate source IDs
source_ids = [
    job.get("source_job_id")
    for job in jobs
    if job.get("source_job_id")
]

unique_ids = set(source_ids)

print("Unique source IDs:", len(unique_ids))
print("Duplicate source IDs:", len(source_ids) - len(unique_ids))


# 3. Check missing important fields
missing_title = 0
missing_location = 0
missing_url = 0
missing_source_id = 0

for job in jobs:

    if not job.get("title"):
        missing_title += 1

    if not job.get("location"):
        missing_location += 1

    if not job.get("apply_url"):
        missing_url += 1

    if not job.get("source_job_id"):
        missing_source_id += 1


print("\nMissing fields:")
print("Missing title:", missing_title)
print("Missing location:", missing_location)
print("Missing apply URL:", missing_url)
print("Missing source ID:", missing_source_id)


# 4. Show first 5 jobs
print("\n================================")
print("SAMPLE JOBS")
print("================================")

for job in jobs[:5]:

    print("\n-------------------------")
    print("Company:", job.get("company_name"))
    print("Title:", job.get("title"))
    print("Location:", job.get("location"))
    print("URL:", job.get("apply_url"))
    print("Source:", job.get("source"))
    print("Source ID:", job.get("source_job_id"))