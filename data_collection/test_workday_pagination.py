import requests

url = "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs"

all_ids = []

for offset in [0, 20, 40, 60]:

    response = requests.post(
        url,
        json={
            "appliedFacets": {},
            "limit": 20,
            "offset": offset,
            "searchText": ""
        },
        timeout=30
    )

    response.raise_for_status()

    data = response.json()
    jobs = data.get("jobPostings", [])

    ids = [job.get("externalPath") for job in jobs]

    all_ids.extend(ids)

    print("\n==============================")
    print("OFFSET:", offset)
    print("JOBS:", len(jobs))
    print("API TOTAL:", data.get("total"))

    if ids:
        print("FIRST:", ids[0])
        print("LAST :", ids[-1])

print("\n==============================")
print("PAGINATION CHECK")
print("==============================")

print("Total IDs collected:", len(all_ids))
print("Unique IDs:", len(set(all_ids)))

if len(all_ids) == len(set(all_ids)):
    print("RESULT: Pages contain different jobs.")
else:
    print("RESULT: DUPLICATE jobs found between pages.")