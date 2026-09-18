import json
from collections import defaultdict


INPUT_FILE = "data/all_jobs_combined.json"


def normalize_text(value):
    if not value:
        return ""

    return " ".join(value.lower().strip().split())


def create_content_key(job):

    company = normalize_text(job.get("company_name"))
    title = normalize_text(job.get("title"))
    location = normalize_text(job.get("location"))

    return f"{company}|{title}|{location}"


with open(INPUT_FILE, "r", encoding="utf-8") as file:
    jobs = json.load(file)


print("================================")
print("GLOBAL DUPLICATE CHECK")
print("================================")

print("\nTotal combined jobs:", len(jobs))


# --------------------------------------------------
# 1. Exact duplicate check
# --------------------------------------------------

source_id_groups = defaultdict(list)

for job in jobs:

    source = normalize_text(job.get("source"))
    source_job_id = normalize_text(job.get("source_job_id"))

    if source_job_id:

        key = f"{source}|{source_job_id}"

        source_id_groups[key].append(job)


exact_duplicates = {
    key: records
    for key, records in source_id_groups.items()
    if len(records) > 1
}


print("\n===== EXACT DUPLICATES =====")

print(
    "Duplicate source + source_job_id groups:",
    len(exact_duplicates)
)


# --------------------------------------------------
# 2. Company + title + location groups
# --------------------------------------------------

content_groups = defaultdict(list)

for job in jobs:

    key = create_content_key(job)

    if key != "||":

        content_groups[key].append(job)


same_source_duplicates = []
cross_source_duplicates = []


for key, records in content_groups.items():

    if len(records) <= 1:
        continue

    sources = set(
        normalize_text(job.get("source"))
        for job in records
    )

    if len(sources) == 1:

        same_source_duplicates.append(
            (key, records)
        )

    else:

        cross_source_duplicates.append(
            (key, records)
        )


# --------------------------------------------------
# 3. Print results
# --------------------------------------------------

print("\n===== SAME-SOURCE DUPLICATE GROUPS =====")

print(
    "Groups:",
    len(same_source_duplicates)
)


print("\n===== CROSS-SOURCE DUPLICATE GROUPS =====")

print(
    "Groups:",
    len(cross_source_duplicates)
)


# --------------------------------------------------
# 4. Show cross-source duplicates
# --------------------------------------------------

print("\n================================")
print("CROSS-SOURCE EXAMPLES")
print("================================")


shown = 0

for key, records in cross_source_duplicates:

    print("\n-------------------------")

    print("Company | Title | Location")
    print(key)

    for job in records:

        print(
            f"Source: {job.get('source')} | "
            f"ID: {job.get('source_job_id')}"
        )

    shown += 1

    if shown >= 20:
        break


print("\n================================")
print("CHECK COMPLETE")
print("================================")

print(
    "\nCross-source groups displayed:",
    min(shown, 20)
)