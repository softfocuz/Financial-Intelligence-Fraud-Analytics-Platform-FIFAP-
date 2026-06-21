import pandas as pd
import uuid
import random

transactions = pd.read_csv("data/raw/transactions.csv")
accounts = pd.read_csv("data/raw/accounts.csv")

account_ids = accounts["account_id"].tolist()

legs = []

for _, row in transactions.iterrows():
    if row["transaction_type"] != "TRANSFER":
        continue

    credit_account = row["account_id"]

    while credit_account == row["account_id"]:
        credit_account = random.choice(
            account_ids
        )

    # money leaves source account
    legs.append({
        "leg_id": str(uuid.uuid4()),
        "transaction_id": row["transaction_id"],
        "account_id": row["account_id"],
        "direction": "DEBIT",
        "amount": row["amount"],
        "currency": row["currency"]
    })

    # money enters destination account
    legs.append({
        "leg_id": str(uuid.uuid4()),
        "transaction_id": row["transaction_id"],
        "account_id": credit_account,
        "direction": "CREDIT",
        "amount": row["amount"],
        "currency": row["currency"]
    })

df = pd.DataFrame(legs)
df.to_csv("data/raw/transaction_legs.csv", index=False)
