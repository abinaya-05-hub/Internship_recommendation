import json
import re


INPUT_FILE = "data/final_jobs_classified.json"


def normalize_text(value):

    if not value:
        return ""

    return " ".join(value.lower().strip().split())


def title_has_internship_signal(title):

    title = normalize_text(title)

    patterns = [
        r"\bintern\b",
        r"\binternship\b",
        r"\bco[- ]op\b",
        r"\bapprentice\b",
        r"\bapprenticeship\b"
    ]

    return any(
        re.search(pattern, title)
        for pattern in patterns
    )


with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as file:

    jobs = json.load(file)


missed = []


for job in jobs:

    if (
        job.get("category") == "Job"
        and title_has_internship_signal(job.get("title"))
    ):

        missed.append(job)


print("================================")
print("CLASSIFICATION MISS CHECK")
print("================================")

print("\nPossible missed internships:", len(missed))


print("\n===== RECORDS TO REVIEW =====")


for job in missed:

    print("\n-------------------------")

    print("Title:", job.get("title"))
    print("Company:", job.get("company_name"))
    print("Employment type:", job.get("employment_type"))
    print("Category:", job.get("category"))
    print("Source:", job.get("source"))
    print("Location:", job.get("location"))


print("\n================================")
print("CHECK COMPLETE")
print("================================")