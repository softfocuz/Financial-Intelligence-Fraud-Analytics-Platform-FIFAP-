from faker import Faker
import pandas as pd
import uuid
import random

generate = Faker()

customers = pd.read_csv("data/raw/customers.csv")
devices = pd.read_csv("data/raw/devices.csv")

customer_ids = customers["customer_id"].tolist()
device_ids = devices["device_id"].tolist()

logins = []

for _ in range(8000):
    login_status = random.choices(
        ["SUCCESS", "FAILED"],
        weights=[92, 8],
        k=1
    )[0]

    logins.append({
        "login_id": str(uuid.uuid4()),
        "customer_id": random.choice(customer_ids),
        "device_id": random.choice(device_ids),
        "ip_address": generate.ipv4(),
        "location": generate.city(),
        "login_timestamp": generate.date_time_this_year(),
        "login_status": login_status
    })

df = pd.DataFrame(logins)
df.to_csv("data/raw/login_history.csv",index=False)
