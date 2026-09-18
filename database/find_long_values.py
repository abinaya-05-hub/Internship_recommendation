import json


FILE = "data/final_jobs_classified.json"

LIMITS = {
    "company_name": 255,
    "title": 255,
    "location": 255,
    "employment_type": 100,
    "source": 100,
    "work_mode": 50,
    "category": 100,
    "department": 100,
    "source_job_id": 255,
}


with open(FILE, "r", encoding="utf-8") as f:
    records = json.load(f)


print("================================")
print("CHECKING LONG VALUES")
print("================================")

found = False

for index, record in enumerate(records, start=1):

    for field, limit in LIMITS.items():

        value = record.get(field)

        if value is not None:
            value_length = len(str(value))

            if value_length > limit:
                found = True

                print(f"\nRecord: {index}")
                print(f"Company: {record.get('company_name')}")
                print(f"Title: {record.get('title')}")
                print(f"Field: {field}")
                print(f"Length: {value_length}")
                print(f"Allowed: {limit}")
                print(f"Value: {value}")


if not found:
    print("\nNo values exceed the database limits.")
else:
    print("\n================================")
    print("LONG VALUES FOUND")
    print("================================")