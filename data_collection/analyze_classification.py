import json
from collections import Counter


INPUT_FILE = "data/all_jobs_combined.json"


with open(INPUT_FILE, "r", encoding="utf-8") as file:
    jobs = json.load(file)


print("================================")
print("CLASSIFICATION DATA ANALYSIS")
print("================================")

print("\nTotal records:", len(jobs))


# --------------------------------
# Employment Type
# --------------------------------

employment_types = Counter()

for job in jobs:

    employment_type = job.get("employment_type")

    if employment_type:
        employment_types[employment_type.strip()] += 1
    else:
        employment_types["<Missing>"] += 1


print("\n===== EMPLOYMENT TYPES =====")

for employment_type, count in employment_types.most_common():

    print(f"{employment_type}: {count}")


# --------------------------------
# Current Category
# --------------------------------

categories = Counter()

for job in jobs:

    category = job.get("category")

    if category:
        categories[category.strip()] += 1
    else:
        categories["<Missing>"] += 1


print("\n===== CURRENT CATEGORIES =====")

for category, count in categories.most_common():

    print(f"{category}: {count}")


# --------------------------------
# Internship-related titles
# --------------------------------

internship_keywords = [
    "intern",
    "internship",
    "co-op",
    "co op",
    "apprentice",
    "apprenticeship"
]


internship_title_matches = []

for job in jobs:

    title = (job.get("title") or "").lower()

    if any(keyword in title for keyword in internship_keywords):

        internship_title_matches.append(job)


print("\n===== INTERNSHIP-RELATED TITLES =====")

print(
    "Records with internship-related title:",
    len(internship_title_matches)
)


# --------------------------------
# Show examples
# --------------------------------

print("\n===== SAMPLE INTERNSHIP-RELATED TITLES =====")

for job in internship_title_matches[:30]:

    print(
        f"Title: {job.get('title')} | "
        f"Employment: {job.get('employment_type')} | "
        f"Category: {job.get('category')} | "
        f"Source: {job.get('source')}"
    )


print("\n================================")
print("ANALYSIS COMPLETE")
print("================================")