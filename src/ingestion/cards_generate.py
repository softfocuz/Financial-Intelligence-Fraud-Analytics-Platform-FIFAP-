from faker import Faker
import pandas as pd
import uuid
import random

generate = Faker()

accounts = pd.read_csv("data/raw/accounts.csv")
account_ids = accounts["account_id"].tolist()

cards = []

for _ in range(580):

    status = random.choices(
        ["ACTIVE", "BLOCKED", "EXPIRED"],
        weights=[80, 12, 8],
        k=1
    )[0]

    if status == "EXPIRED":
        expiry_date = generate.date_between(start_date="-3y", end_date="-1d")
    else:
        expiry_date = generate.date_between(start_date="today", end_date="+5y")

    cards.append({
        "card_id": str(uuid.uuid4()),
        "account_id": random.choice(account_ids),
        "card_number": generate.credit_card_number(),
        "card_type": random.choice([
            "DEBIT",
            "CREDIT"
        ]),
        "status": status,
        "expiry_date": expiry_date,
        "created_at": generate.date_between(start_date="-5y", end_date="today")
    })

df = pd.DataFrame(cards)
df.to_csv("data/raw/cards.csv", index=False)