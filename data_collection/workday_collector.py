import requests
import json
import os


def collect_workday_jobs():

    url = "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs"

    limit = 20
    offset = 0

    all_jobs = []
    seen_ids = set()

    first_request = True
    expected_total = None

    while True:

        response = requests.post(
            url,
            json={
                "appliedFacets": {},
                "limit": limit,
                "offset": offset,
                "searchText": ""
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        job_postings = data.get("jobPostings", [])

        # Get total only from the first request
        if first_request:
            expected_total = data.get("total", 0)
            first_request = False

            print(f"\nAPI reports {expected_total} total jobs")

        print(
            f"Offset: {offset} | "
            f"Jobs returned: {len(job_postings)} | "
            f"Collected: {len(all_jobs)}"
        )

        if not job_postings:
            print("No more jobs returned. Stopping.")
            break

        for job in job_postings:

            source_job_id = job.get("externalPath")

            # Prevent duplicate jobs
            if source_job_id in seen_ids:
                continue

            seen_ids.add(source_job_id)

            normalized_job = {
                "company_name": "NVIDIA",
                "title": job.get("title"),
                "description": None,
                "location": job.get("locationsText"),
                "work_mode": None,
                "employment_type": None,
                "category": "Job",
                "department": None,
                "published_date": None,
                "apply_url": (
                    "https://nvidia.wd5.myworkdayjobs.com"
                    + job.get("externalPath", "")
                ),
                "source": "Workday",
                "source_job_id": source_job_id
            }

            all_jobs.append(normalized_job)

        # Stop when we have reached the total reported
        if len(all_jobs) >= expected_total:
            print("\nReached the expected total.")
            break

        offset += limit

    return all_jobs


if __name__ == "__main__":

    jobs = collect_workday_jobs()

    print("\n================================")
    print(f"TOTAL UNIQUE WORKDAY JOBS: {len(jobs)}")
    print("================================")

    os.makedirs("data", exist_ok=True)

    output_file = "data/workday_jobs.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            jobs,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"\nSaved to: {output_file}")