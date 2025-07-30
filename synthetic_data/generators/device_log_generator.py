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

devices = ["USB-001", "USB-002", "EXT-HDD-001", "SD-CARD-001", "DVD-RW-001"]

device_types = ["USB", "External HDD", "SD Card", "DVD", "Network Drive"]

actions = ["connect", "disconnect", "file_transfer", "scan"]

transfer_direction = ["upload", "download", "bidirectional"]


def generate_device_logs(days=7):
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

                action = random.choice(actions)
                logs.append({
                    "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": user['user_id'],
                    "machine_id": random.choice(machines),
                    "device_id" : random.choice(devices),
                    "device_type" : random.choice(device_types),
                    "action" : action,
                    "file_transfer_size_mb" : random.randint(1, 1000) if action == "file_transfer" else 0,
                    "file_count" : random.randint(1, 50) if action == "file_transfer" else 0,
                    "transfer_direction" : random.choice(transfer_direction) if action == "file_transfer" else ""
                })

    return pd.DataFrame(logs)

df = generate_device_logs()
df.to_csv("synthetic_device_logs.csv, index = False")
print("Generated synthetic_device_logs.csv")

