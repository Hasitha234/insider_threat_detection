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

websites = [
 {"url": "https://www.google.com/search", "domain": "google.com", "category": "search", "is_personal": False},
    {"url": "https://github.com/company/repo", "domain": "github.com", "category": "development", "is_personal": False},
    {"url": "https://stackoverflow.com/questions", "domain": "stackoverflow.com", "category": "development", "is_personal": False},
    {"url": "https://www.youtube.com/watch", "domain": "youtube.com", "category": "entertainment", "is_personal": True},
    {"url": "https://www.facebook.com/feed", "domain": "facebook.com", "category": "social", "is_personal": True},
    {"url": "https://company-intranet.com/dashboard", "domain": "company-intranet.com", "category": "work", "is_personal": False},
    {"url": "https://mail.company.com/inbox", "domain": "mail.company.com", "category": "email", "is_personal": False},
    {"url": "https://www.amazon.com/shop", "domain": "amazon.com", "category": "shopping", "is_personal": True},
    {"url": "https://docs.google.com/document", "domain": "docs.google.com", "category": "productivity", "is_personal": False},
    {"url": "https://www.linkedin.com/feed", "domain": "linkedin.com", "category": "professional", "is_personal": False}
]


def generate_http_logs(days=7):
    logs = []
    base_data = datetime(2024, 1, 1)

    for day in range(days):
        date = base_data + timedelta(days=day)
        for user in users:
            num_requests = random.randint(1, 3)
            for _ in range(num_requests):
                hour = random.randint(user['work_hours'][0], user['work_hours'][1])
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                timestamp = datetime(date.year, date.month, date.day, hour, minute, second)

                website = random.choice(websites)
                logs.append({
                    "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": user['user_id'],
                    "machine_id": random.choice(machines),
                    "url" : website["url"],
                    "domain" : website["domain"],
                    "category" : website["category"],
                    "duration_seconds" : random.randint(5, 300),
                    "data_downloaded_kb": random.randint(10, 5000),
                    "is_personal": website["is_personal"]
                })

    return pd.DataFrame(logs)

df = generate_http_logs()
df.to_csv("synthetic_http_logs.csv, index = False")
print("Generated synthetic_http_logs.csv")

