import random
import pandas as pd
from datetime import datetime, timedelta

users = [
    {
        "user_id": "EMP001", "name": "Alice", "work_hours": (9, 17), "location": "office"
    },
    {
        "user_id": "EMP002", "name": "Bob", "work_hours": (10, 18), "location": "remote"
    },
    {
        "user_id": "EMP003", "name": "Carol", "work_hours": (8, 17), "location": "office"
    }
]


machines = ["PC-FINANCE-01", "PC-ENG-02", "PC-HR-03"]

file_paths = ["/documents/reports/financial_report.xlsx",
    "/documents/contracts/client_agreement.pdf",
    "/projects/source_code/main.py",
    "/hr/employee_records/salary_data.csv",
    "/shared/presentations/quarterly_review.pptx",
    "/temp/cache/temp_file.tmp",
    "/backup/database_backup.sql",
    "/config/system_settings.json"]

actions = ["read", "write", "delete", "copy", "move", "rename"]

file_types = ["xlsx", "pdf", "py", "csv", "pptx", "tmp", "sql", "json", "docx", "txt"]

sensitivity_levels = ["public", "internal", "confidential", "restricted"]


def generate_file_access_logs(days=7):
    logs = []
    base_data = datetime(2024, 1, 1)

    for day in range(days):
        date = base_data + timedelta(days=day)
        for user in users:
            num_access = random.randint(3, 8)
            for _ in range(num_access):
                hour = random.randint(user['work_hours'][0], user['work_hours'][1])
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                timestamp = datetime(date.year, date.month, date.day, hour, minute, second)

                logs.append({
                    "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": user['user_id'],
                    "machine_id": random.choice(machines),
                    "file_path": random.choice(file_paths),
                    "action" : random.choice(actions),
                    "file_types" : random.choice(file_types),
                    "file_size_kb" : random.randint(1, 10000),
                    "is_encrypted" : random.choices([True, False]),
                    "sensitivity_level" : random.choice(sensitivity_levels)
                    
                })

    return pd.DataFrame(logs)

df = generate_file_access_logs()
df.to_csv("synthetic_file_logs.csv, index = False")
print("Generated synthetic_file_logs.csv")

