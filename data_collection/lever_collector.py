import requests
import json
import os
from config import LEVER_COMPANIES


def collect_lever_jobs(company, company_name=None):

    url = f"https://api.lever.co/v0/postings/{company}"

    params = {
        "mode": "json"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    jobs = response.json()

    normalized_jobs = []

    for job in jobs:

        categories = job.get("categories", {})

        location = categories.get("location")
        department = categories.get("department")
        employment_type = categories.get("commitment")

        workplace_type = job.get("workplaceType")

        if workplace_type:
            work_mode = workplace_type.capitalize()
        else:
            work_mode = None

        normalized_job = {
            "company_name": company_name or job.get("company"),
            "title": job.get("text"),
            "description": job.get("description"),
            "location": location,
            "work_mode": work_mode,
            "employment_type": employment_type,
            "category": "Job",
            "department": department,
            "published_date": None,
            "apply_url": job.get("applyUrl"),
            "source": "Lever",
            "source_job_id": str(job.get("id"))
        }

        normalized_jobs.append(normalized_job)

    return normalized_jobs


if __name__ == "__main__":

    all_jobs = []

    for company, company_name in LEVER_COMPANIES.items():

        print(f"\nCollecting jobs from {company_name}...")

        try:

            jobs = collect_lever_jobs(
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
    print(f"TOTAL LEVER JOBS COLLECTED: {len(all_jobs)}")
    print("================================")
    os.makedirs("data", exist_ok=True)

    output_file = "data/lever_jobs.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(all_jobs, file, indent=4, ensure_ascii=False)

    print(f"\nSaved jobs to: {output_file}")