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


if __name__ == "__main__":

    input_file = "data/greenhouse_jobs.json"
    output_file = "data/greenhouse_jobs_deduplicated.json"

    with open(input_file, "r", encoding="utf-8") as file:
        jobs = json.load(file)

    print(f"Jobs before deduplication: {len(jobs)}")

    unique_jobs = deduplicate_jobs(jobs)

    print(f"Jobs after deduplication: {len(unique_jobs)}")
    print(f"Duplicates removed: {len(jobs) - len(unique_jobs)}")

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(unique_jobs, file, indent=4, ensure_ascii=False)

    print(f"\nSaved deduplicated jobs to: {output_file}")