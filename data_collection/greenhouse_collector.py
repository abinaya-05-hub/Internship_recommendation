import requests


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

    company = "vercel"

    jobs = collect_greenhouse_jobs(
        company,
        company_name="Vercel"
    )

    print(f"Total jobs collected: {len(jobs)}")

    for job in jobs[:5]:
        print("\n-------------------------")
        print("Company:", job["company_name"])
        print("Title:", job["title"])
        print("Location:", job["location"])
        print("Department:", job["department"])
        print("URL:", job["apply_url"])
        print("Source:", job["source"])