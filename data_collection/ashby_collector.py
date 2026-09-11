import requests
import json

JOB_BOARD_NAME = "interview-kickstart"

url = f"https://api.ashbyhq.com/posting-api/job-board/{JOB_BOARD_NAME}"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

jobs = data["jobs"]

internships = []
full_time_jobs = []

for job in jobs:

    employment_type = job.get("employmentType")

    if employment_type == "Intern":
        internships.append(job)

    elif employment_type == "FullTime":
        full_time_jobs.append(job)

with open("data/internships.json", "w", encoding="utf-8") as file:
    json.dump(internships, file, indent=4)

with open("data/jobs.json", "w", encoding="utf-8") as file:
    json.dump(full_time_jobs, file, indent=4)

print("\nData saved successfully!")


print("\n========== SUMMARY ==========")
print("Total postings:", len(jobs))
print("Total internships:", len(internships))
print("Total full-time jobs:", len(full_time_jobs))

with open("data/internships.json", "w", encoding="utf-8") as file:
    json.dump(internships, file, indent=4)

with open("data/jobs.json", "w", encoding="utf-8") as file:
    json.dump(full_time_jobs, file, indent=4)

print("\nData saved successfully!")


print("\n========== INTERNSHIPS ==========")

for job in internships:
    print("-----------------------------")
    print("Title:", job.get("title"))
    print("Location:", job.get("location"))
    print("Department:", job.get("department"))
    print("Employment Type:", job.get("employmentType"))
    print("Workplace:", job.get("workplaceType"))
    print("Published:", job.get("publishedAt"))
    print("Apply URL:", job.get("applyUrl"))


print("\n========== FULL-TIME JOBS ==========")

for job in full_time_jobs:
    print("-----------------------------")
    print("Title:", job.get("title"))
    print("Location:", job.get("location"))
    print("Department:", job.get("department"))
    print("Employment Type:", job.get("employmentType"))
    print("Workplace:", job.get("workplaceType"))
    print("Published:", job.get("publishedAt"))
    print("Apply URL:", job.get("applyUrl"))