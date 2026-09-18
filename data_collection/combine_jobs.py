import json
import os


INPUT_FILES = [
    "data/normalized_jobs.json",
    "data/greenhouse_jobs_deduplicated.json",
    "data/lever_jobs_deduplicated.json",
    "data/workday_jobs_deduplicated.json"
]

OUTPUT_FILE = "data/all_jobs_combined.json"


def load_jobs(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def combine_jobs():

    all_jobs = []

    print("================================")
    print("COMBINING JOB DATA")
    print("================================")

    for file_path in INPUT_FILES:

        if not os.path.exists(file_path):
            print(f"\nFile not found: {file_path}")
            continue

        jobs = load_jobs(file_path)

        print(f"\n{file_path}")
        print(f"Jobs: {len(jobs)}")

        all_jobs.extend(jobs)

    print("\n================================")
    print(f"TOTAL COMBINED JOBS: {len(all_jobs)}")
    print("================================")

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_jobs,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"\nSaved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    combine_jobs()