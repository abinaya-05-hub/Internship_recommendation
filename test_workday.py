import requests

url = "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs"

response = requests.post(
    url,
    json={
        "appliedFacets": {},
        "limit": 20,
        "offset": 0,
        "searchText": ""
    },
    timeout=30
)

print("Status:", response.status_code)

data = response.json()

print("Keys:", data.keys())

print("Total jobs:", data.get("total"))

for job in data.get("jobPostings", [])[:5]:
    print("\n-------------------------")
    print("Title:", job.get("title"))
    print("Location:", job.get("locationsText"))
    print("URL:", job.get("externalPath"))