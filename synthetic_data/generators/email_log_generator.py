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

priorities = ["low", "normal", "high", "urgent"]


def generate_email_logs(days=7):
    logs = []
    base_data = datetime(2024, 1, 1)

    for day in range(days):
        date = base_data + timedelta(days=day)
        for user in users:
            if user['email_frequency'] == 'high':
                num_email = random.randint(5, 15)
            elif user["email_frequency"] == 'medium':
                num_email = random.randint(2, 8)
            else:
                num_email = random.randint(1, 4)

            for _ in range(num_email):
                hour = random.randint(7, 19)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                timestamp = datetime(date.year, date.month, date.day, hour, minute, second)

                has_attachment = random.choices([True, False], weights=[0.3, 0.7])[0]
                attachment_count = random.randint(1, 4) if has_attachment else 0
                is_external = random.choices([True, False], weights=[0.2, 0.8])[0]

                logs.append({
                    "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "sender_id": user['user_id'],
                    "receiver_id": random.choice([u['user_id'] for u in users if u['user_id'] != user['user_id']]),
                    "external_recipients": f"external@{random.choice(external_domains)}" if is_external else "",
                    "subject_length" : random.randint(10, 80),
                    "body_length" : random.randint(50, 2000),
                    "has_attachment" : has_attachment,
                    "attachment_count" : attachment_count,
                    "attachment_size_mb" : round(random.uniform(0.1, 50.0), 2) if has_attachment else 0,
                    "attachment_types" : ",".join(random.sample(attatchment_types, min(attachment_count, len(attatchment_types)))) if has_attachment else "",
                    "is_reply" : random.choices([True, False], weights=[0.4, 0.6])[0],
                    "prioritie" :random.choice(priorities)
                })

    return pd.DataFrame(logs)

df = generate_email_logs()
df.to_csv("synthetic_email_logs.csv, index = False")
print("Generated synthetic_mail_logs.csv")

