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


machines = ["PC-FINANCE-01", "PC-ENG-02", "PC-HR-03", "LAPTOP-001", "LAPTOP-002"]

connection_types = ["ethernet", "wifi", "mobile", "vpn"]

location_types = ["office", "home", "public", "remote"]

cities = ["New York", "London", "Tokyo", "Sydney", "Toronto"]

countries = ["USA", "UK", "Japan", "Australia", "Canada"]

ip_ranges = {
    "office": "192.168.1.",
    "home": "10.0.0.",
    "public": "203.45.",
    "remote": "172.16."
}

def generate_ip_address(location_type):
    """Generate IP address based on location type"""
    base = ip_ranges[location_type]
    last_octet = random.randint(1, 254)
    return f"{base}{last_octet}"

def determine_vpn_usage(location_type, connection_type):

    if location_type in ["public", "remote"]:
        return random.choices([True, False], weights=[0.8, 0.2])[0]
    elif connection_type == "vpn":
        return True
    else:
        return random.choices([True, False], weights=[0.1, 0.9])[0]

def generate_network_logs(days=7):
    logs = []
    base_data = datetime(2024, 1, 1)

    for day in range(days):
        date = base_data + timedelta(days=day)
        for user in users:
            num_connection = random.randint(2, 5)
            for _ in range(num_connection):
                hour = random.randint(user['work_hours'][0], user['work_hours'][1])
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                timestamp = datetime(date.year, date.month, date.day, hour, minute, second)

                location_type = random.choices(
                    location_types,
                    weights=[0.4, 0.3, 0.2, 0.1]
                    )[0]
                
                connection_type = random.choice(connection_types)
                vpn_used = determine_vpn_usage(location_type, connection_type)

                logs.append({
                    "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": user['user_id'],
                    "machine_id": random.choice(machines),
                    "ip_address" : generate_ip_address(location_type),
                    "location_type" : location_type,
                    "city" : random.choice(cities),
                    "country" : random.choice(countries),
                    "connection_type" : connection_type,
                    "vpn_used" : vpn_used
                })

    return pd.DataFrame(logs)

df = generate_network_logs()
df.to_csv("synthetic_network_logs.csv, index = False")
print("Generated synthetic_network_logs.csv")

