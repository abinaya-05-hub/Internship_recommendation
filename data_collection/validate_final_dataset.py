import json
from collections import Counter


INPUT_FILE = "data/final_jobs_classified.json"


with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as file:

    jobs = json.load(file)


print("================================")
print("FINAL DATASET VALIDATION")
print("================================")


# --------------------------------
# Total records
# --------------------------------

print("\nTotal records:", len(jobs))


# --------------------------------
# Required fields
# --------------------------------

required_fields = [
    "title",
    "apply_url",
    "source",
    "source_job_id",
    "category"
]


print("\n===== MISSING REQUIRED FIELDS =====")


for field in required_fields:

    missing = sum(
        1
        for job in jobs
        if not job.get(field)
    )

    print(f"{field}: {missing}")


# --------------------------------
# Categories
# --------------------------------

categories = Counter(
    job.get("category")
    for job in jobs
)


print("\n===== CATEGORIES =====")

for category, count in categories.items():

    print(f"{category}: {count}")


# --------------------------------
# Duplicate source + source ID
# --------------------------------

seen = set()
duplicates = []


for job in jobs:

    source = str(
        job.get("source") or ""
    ).strip().lower()

    source_job_id = str(
        job.get("source_job_id") or ""
    ).strip()

    key = f"{source}|{source_job_id}"

    if key in seen:

        duplicates.append(key)

    else:

        seen.add(key)


print("\n===== DUPLICATES =====")

print(
    "Duplicate source + source_job_id:",
    len(duplicates)
)


# --------------------------------
# Invalid categories
# --------------------------------

valid_categories = {
    "Job",
    "Internship"
}


invalid_categories = [
    job.get("category")
    for job in jobs
    if job.get("category") not in valid_categories
]


print("\n===== INVALID CATEGORIES =====")

print(
    "Invalid category records:",
    len(invalid_categories)
)


# --------------------------------
# Final status
# --------------------------------

print("\n================================")

if (
    len(jobs) == 4087
    and all(
        job.get(field)
        for job in jobs
        for field in required_fields
    )
    and len(duplicates) == 0
    and len(invalid_categories) == 0
):

    print("FINAL DATASET STATUS: READY")

else:

    print("FINAL DATASET STATUS: NEEDS REVIEW")


print("================================")