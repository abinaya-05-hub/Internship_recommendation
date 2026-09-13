import json


def create_job_key(job):
    """
    Creates a unique key using company, title and location.
    """

    company = (job.get("company_name") or "").strip().lower()
    title = (job.get("title") or "").strip().lower()
    location = (job.get("location") or "").strip().lower()

    return f"{company}|{title}|{location}"


def deduplicate_jobs(jobs):

    unique_jobs = []
    seen = set()

    for job in jobs:

        key = create_job_key(job)

        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    return unique_jobs


def process_file(input_file, output_file):

    with open(input_file, "r", encoding="utf-8") as file:
        jobs = json.load(file)

    print(f"\nProcessing: {input_file}")
    print(f"Jobs before deduplication: {len(jobs)}")

    unique_jobs = deduplicate_jobs(jobs)

    print(f"Jobs after deduplication: {len(unique_jobs)}")
    print(f"Duplicates removed: {len(jobs) - len(unique_jobs)}")

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(unique_jobs, file, indent=4, ensure_ascii=False)

    print(f"Saved to: {output_file}")


if __name__ == "__main__":

    process_file(
        "data/greenhouse_jobs.json",
        "data/greenhouse_jobs_deduplicated.json"
    )

    process_file(
        "data/lever_jobs.json",
        "data/lever_jobs_deduplicated.json"
    )