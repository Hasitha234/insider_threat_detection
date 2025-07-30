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
login_types = ["domain", "local", "remote"]
locations = ["office", "remote", "vpn"]


def generate_login_logs(days=7):
    logs = []
    base_data = datetime(2024, 1, 1)

    for day in range(days):
        date = base_data + timedelta(days=day)
        for user in users:
            num_logins = random.randint(1, 3)
            for _ in range(num_logins):
                hour = random.randint(user['work_hours'][0], user['work_hours'][1])
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                timestamp = datetime(date.year, date.month, date.day, hour, minute, second)

                logs.append({
                    "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": user['user_id'],
                    "machine_id": random.choice(machines),
                    "login_type": random.choice(login_types),
                    "location": user["location"],
                    "success": random.choices([True, False], weights=[0.95, 0.05])[0],
                    "session_duration": random.randint(30, 480)
                })

    return pd.DataFrame(logs)

df = generate_login_logs()
df.to_csv("synthetic_login_logs.csv, index = False")
print("Generated synthetic_login_logs.csv")

