from faker import Faker
import pandas as pd
import uuid
import random
import numpy as np

generate = Faker()

accounts = pd.read_csv("data/raw/accounts.csv")
cards = pd.read_csv("data/raw/cards.csv")
devices = pd.read_csv("data/raw/devices.csv")
merchants = pd.read_csv("data/raw/merchants.csv")

account_ids = accounts["account_id"].tolist()
card_ids = cards["card_id"].tolist()
device_ids = devices["device_id"].tolist()
merchant_ids = merchants["merchant_id"].tolist()

transactions = []

for _ in range(50000):
    amount = round(np.random.exponential(scale=3000), 2)
    amount = max(50.0, min(amount, 150000.0))

    transactions.append({
        "transaction_id": str(uuid.uuid4()),
        "account_id": random.choice(account_ids),
        "card_id": random.choice(card_ids),
        "merchant_id": random.choice(merchant_ids),
        "device_id": random.choice(device_ids),
        "transaction_type": random.choice([
            "PURCHASE",
            "TRANSFER",
            "WITHDRAWAL",
            "PAYMENT"
        ]),
        "transaction_status": random.choice([
            "SUCCESS",
            "FAILED"
        ]),
        "amount": amount,
        "currency": "PHP",
        "transaction_timestamp": generate.date_time_this_year(),
        "channel": random.choice([
            "ATM",
            "ONLINE",
            "POS",
            "MOBILE"
        ]),
        "ip_address": generate.ipv4(),
        "location": generate.city(),
        "reference_number": generate.unique.bothify("REF########"),
        "created_at": generate.date_this_year(),
        "updated_at": generate.date_this_year()
    })
df = pd.DataFrame(transactions)
df.to_csv("data/raw/transactions.csv",index=False)
