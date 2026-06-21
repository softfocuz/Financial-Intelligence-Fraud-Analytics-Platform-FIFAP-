from faker import Faker
import pandas as pd
import uuid
import random

generate = Faker()

HIGH_RISK_CATEGORIES = [
    "Gambling",
    "Crypto",
    "Wire Transfer"
]

merchants = []

for _ in range(100):
    category = random.choices([
        "Retail",
        "Food",
        "Travel",
        "Electronics",
        "Healthcare",
        "Gambling",
        "Crypto",
        "Wire Transfer"
    ],
        weights=[
            25,
            25,
            15,
            15,
            10,
            4,
            3,
            3
        ],
        k=1
    )[0]

    risk_level = (
        "HIGH"
        if category in HIGH_RISK_CATEGORIES
        else "LOW"
    )

    merchants.append({
        "merchant_id": str(uuid.uuid4()),
        "name": generate.company(),
        "category": category,
        "risk_level": risk_level,
        "country": "Philippines",
        "location": generate.city(),
        "created_at": generate.date_this_year()
    })

df = pd.DataFrame(merchants)
df.to_csv("data/raw/merchants.csv", index=False)

