import json
import re
from collections import Counter


INPUT_FILE = "data/all_jobs_combined.json"
OUTPUT_FILE = "data/final_jobs_classified.json"


def normalize_text(value):
    if not value:
        return ""

    return " ".join(value.lower().strip().split())


def is_internship_by_employment_type(employment_type):
    """
    Check structured employment information first.
    """

    if not employment_type:
        return False

    value = normalize_text(employment_type)

    internship_types = {
        "intern",
        "internship"
    }

    return value in internship_types


def is_internship_by_title(title):
    """
    Check the title using word boundaries.

    This prevents words such as:
    internal
    international

    from being classified as internships.
    """

    title = normalize_text(title)

    if not title:
        return False

    patterns = [
        r"\bintern\b",
        r"\binternship\b",
        r"\bco[- ]op\b",
        r"\bapprentice\b",
        r"\bapprenticeship\b"
    ]

    for pattern in patterns:

        if re.search(pattern, title):
            return True

    return False


def classify_job(job):

    employment_type = job.get("employment_type")
    title = job.get("title")

    # --------------------------------
    # Rule 1: Structured employment type
    # --------------------------------

    if is_internship_by_employment_type(employment_type):

        return "Internship"


    # --------------------------------
    # Rule 2: Explicit internship title
    # --------------------------------

    if is_internship_by_title(title):

        return "Internship"


    # --------------------------------
    # Default
    # --------------------------------

    return "Job"


def main():

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        jobs = json.load(file)


    print("================================")
    print("JOB CLASSIFICATION")
    print("================================")

    print("\nTotal records:", len(jobs))


    classification_counts = Counter()


    for job in jobs:

        category = classify_job(job)

        # Keep original fields.
        # Only update the normalized category.
        job["category"] = category

        classification_counts[category] += 1


    print("\n===== CLASSIFICATION RESULT =====")

    for category, count in classification_counts.items():

        print(f"{category}: {count}")


    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            jobs,
            file,
            indent=4,
            ensure_ascii=False
        )


    print("\nSaved to:")
    print(OUTPUT_FILE)

    print("\n================================")
    print("CLASSIFICATION COMPLETE")
    print("================================")


if __name__ == "__main__":
    main()