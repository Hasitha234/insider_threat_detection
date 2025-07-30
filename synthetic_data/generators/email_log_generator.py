import random
import pandas as pd
from datetime import datetime, timedelta

users = [
    {
        "user_id": "EMP001", "name": "Alice", "department" : "finance", "email_frequency": "high"
    },
    {
        "user_id": "EMP002", "name": "Bob", "department" : "engineering", "email_frequency": "medium"
    },
    {
        "user_id": "EMP003", "name": "Carol", "department" : "hr", "email_frequency": "low"
    }
]


external_domains = ["gmail.com", "yahoo.com", "client-company.com", "vendor.org"]

attatchment_types = ["pdf", "docx", "xlsx", "pptx", "jpg", "zip"]


def generate_mail_logs(days=7):
    logs = []
    base_data = datetime(2024, 1, 1)

    for day in range(days):
        date = base_data + timedelta(days=day)
        for user in users:
            num_email = random.randint(1, 3)
            for _ in range(num_email):
                hour = random.randint(user['work_hours'][0], user['work_hours'][1])
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                timestamp = datetime(date.year, date.month, date.day, hour, minute, second)

                logs.append({
                    "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": user['user_id'],
                    "machine_id": random.choice(machines),
                    "device_id" : random.choice(device_id),
                    "device_type" : random.choice(device_type),
                    "action" : random.choice(action),
                    "file_transfer_size_mb" : round(random.uniform(0.1, 25.0),2 ),
                    "file_count" : random.randint(1, 5),
                    "transfer_direction" : random.choice(transfer_direction)
                })

    return pd.DataFrame(logs)

df = generate_mail_logs()
df.to_csv("synthetic_mail_logs.csv, index = False")
print("Generated synthetic_mail_logs.csv")

