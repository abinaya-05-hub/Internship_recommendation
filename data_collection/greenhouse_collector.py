import json
import os
import requests
from config import GREENHOUSE_COMPANIES


def collect_greenhouse_jobs(company, company_name=None):

    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

    params = {
        "content": "true"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    jobs = data.get("jobs", [])

    normalized_jobs = []

    for job in jobs:

        location = job.get("location", {}).get("name")

        departments = job.get("departments", [])
        department = departments[0].get("name") if departments else None

        published_date = job.get("first_published")

        normalized_job = {
            "company_name": company_name or job.get("company_name"),
            "title": job.get("title"),
            "description": job.get("content"),
            "location": location,
            "work_mode": None,
            "employment_type": None,
            "category": "Job",
            "department": department,
            "published_date": published_date,
            "apply_url": job.get("absolute_url"),
            "source": "Greenhouse",
            "source_job_id": str(job.get("id"))
        }

        normalized_jobs.append(normalized_job)

    return normalized_jobs


if __name__ == "__main__":

    all_jobs = []

    for company, company_name in GREENHOUSE_COMPANIES.items():

        print(f"\nCollecting jobs from {company_name}...")

        try:
            jobs = collect_greenhouse_jobs(
                company,
                company_name
            )

            print(f"Collected {len(jobs)} jobs")

            all_jobs.extend(jobs)

        except requests.exceptions.HTTPError as e:

            print(f"Failed to collect {company_name}: {e}")

        except Exception as e:

            print(f"Error collecting {company_name}: {e}")


    print("\n================================")
    print(f"TOTAL JOBS COLLECTED: {len(all_jobs)}")
    print("================================")
    os.makedirs("data", exist_ok=True)

    output_file = "data/greenhouse_jobs.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(all_jobs, file, indent=4, ensure_ascii=False)

    print(f"\nSaved jobs to: {output_file}")