from faker import Faker
import pandas as pd
import uuid
import random

generate = Faker()

customers = pd.read_csv("data/raw/customers.csv")

customer_ids = customers["customer_id"].tolist()

accounts = []

for _ in range(750):

    status = random.choices(
        ["ACTIVE", "DORMANT", "CLOSED"],
        weights=[85, 10, 5],
        k=1
    )[0]

    created = generate.date_between(start_date="-7y", end_date="today")

    updated = generate.date_between(start_date=created, end_date="today")
    accounts.append({
        "account_id": str(uuid.uuid4()),
        "customer_id": random.choice(customer_ids),
        "account_number": generate.unique.bban(),
        "account_type":random.choices(
            ["Savings", "Checking"],
            weights=[70, 30],
            k=1
        )[0],
        "currency": "PHP",
        "balance": round(random.uniform(1000, 500000), 2),
        "status": status,
        "created_at": created,
        "updated_at": updated
    })

df = pd.DataFrame(accounts)
df.to_csv("data/raw/accounts.csv", index=False)