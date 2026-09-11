import json


COMPANY_NAME = "Interview Kickstart"
SOURCE = "Ashby"


def normalize_job(job):
    job_url = job.get("jobUrl", "")

    source_job_id = job_url.rstrip("/").split("/")[-1]

    if job.get("employmentType") == "Intern":
        category = "Internship"
    elif job.get("employmentType") == "FullTime":
        category = "Job"
    else:
        category = "Other"

    normalized = {
        "company_name": COMPANY_NAME,
        "title": job.get("title"),
        "description": job.get("descriptionPlain"),
        "location": job.get("location"),
        "work_mode": job.get("workplaceType"),
        "employment_type": job.get("employmentType"),
        "category": category,
        "department": job.get("department"),
        "published_date": job.get("publishedAt"),
        "apply_url": job.get("applyUrl"),
        "source": SOURCE,
        "source_job_id": source_job_id
    }

    return normalized


# Read internships
with open("data/internships.json", "r", encoding="utf-8") as file:
    internships = json.load(file)


# Read jobs
with open("data/jobs.json", "r", encoding="utf-8") as file:
    jobs = json.load(file)


# Normalize
normalized_internships = []

for internship in internships:
    normalized_internships.append(normalize_job(internship))


normalized_jobs = []

for job in jobs:
    normalized_jobs.append(normalize_job(job))


# Save normalized internships
with open("data/normalized_internships.json", "w", encoding="utf-8") as file:
    json.dump(normalized_internships, file, indent=4)


# Save normalized jobs
with open("data/normalized_jobs.json", "w", encoding="utf-8") as file:
    json.dump(normalized_jobs, file, indent=4)


print("Normalization completed!")
print("Internships normalized:", len(normalized_internships))
print("Jobs normalized:", len(normalized_jobs))