from faker import Faker
import pandas as pd
import uuid
import random

generate = Faker()

customers = []

for _ in range(500):
    customers.append({
        "customer_id": str(uuid.uuid4()),
        "first_name": generate.first_name(),
        "last_name": generate.last_name(),
        "email": generate.email(),
        "phone": generate.phone_number(),
        "birth_date": generate.date_of_birth(minimum_age = 18, maximum_age = 70),
        "address": generate.address(),
        "risk_tier": random.choices(
            ["LOW", "MEDIUM", "HIGH"],
            weights=[70, 25, 5],
            k=1
        )[0],
        "created_at": generate.date_between(start_date = "-7y", end_date = "today"),
        "updated_at": generate.date_this_year()
    })

df = pd.DataFrame(customers)
df.to_csv("data/raw/customers.csv", index=False)
