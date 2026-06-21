from faker import Faker
import pandas as pd
import uuid
import random

generate = Faker()

tables = [
    "customers",
    "accounts",
    "cards",
    "devices",
    "transactions",
    "fraud_analysis"
]

logs = []
for _ in range(2000):

    logs.append({
        "log_id": str(uuid.uuid4()),
        "table_name": random.choice(tables),
        "record_id": str(uuid.uuid4()),
        "action": random.choice([
            "INSERT",
            "UPDATE",
            "DELETE"
        ]),
        "performed_by": random.choice([
            "SYSTEM",
            "ADMIN"
        ]),
        "timestamp": generate.date_time_this_year()
    })

df = pd.DataFrame(logs)
df.to_csv("data/raw/audit_logs.csv", index=False)
