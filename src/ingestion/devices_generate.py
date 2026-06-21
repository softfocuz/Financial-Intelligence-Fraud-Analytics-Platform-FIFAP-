from faker import Faker
import pandas as pd
import uuid
import random

generate = Faker()

customers = pd.read_csv("data/raw/customers.csv")
customer_ids = customers["customer_id"].tolist()

devices = []

for _ in range(900):
    device_type = random.choices(
        ["Mobile", "Laptop", "Tablet"],
        weights=[70, 25, 5],
        k=1
    )[0]

    if device_type == "Mobile":
        os = random.choices(
            ["Android", "iOS"],
            weights=[80, 20],
            k=1
        )[0]

    elif device_type == "Laptop":
        os = random.choices(
            ["Windows", "macOS"],
            weights=[85, 15],
            k=1
        )[0]

    else:
        os = random.choice([
            "Android",
            "iPadOS"
        ])

    browser = random.choices(
        ["Chrome", "Safari", "Edge", "Firefox"],
        weights=[65, 15, 15, 5],
        k=1
    )[0]

    devices.append({
        "device_id": str(uuid.uuid4()),
        "customer_id": random.choice(customer_ids),
        "device_type": device_type,
        "os": os,
        "browser": browser,
        "ip_first_seen": generate.ipv4(),
        "last_seen": generate.date_this_year(),
        "device_fingerprint": generate.sha256()
    })

df = pd.DataFrame(devices)
df.to_csv("data/raw/devices.csv", index=False)
