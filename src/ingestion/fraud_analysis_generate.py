import pandas as pd
import uuid
import random

transactions = pd.read_csv("data/raw/transactions.csv")

analysis = []

for _, row in transactions.iterrows():
    score = round(random.betavariate(2, 5), 2)
    fraud_flag = score >= 0.65

    if score >= 0.65:
        risk_level = "HIGH"
    elif score >= 0.40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    analysis.append({
        "analysis_id": str(uuid.uuid4()),
        "transaction_id": row["transaction_id"],
        "model_name": "RuleBasedEngine",
        "model_version": "1.0",
        "fraud_score": score,
        "risk_level": risk_level,
        "fraud_flag": fraud_flag,
        "analyzed_at": row["transaction_timestamp"],

        "reason": random.choice([
            "Normal transaction",
            "High amount",
            "New device",
            "Unusual location",
            "Rapid transactions",
            "Multiple failed logins"
        ])
    })

df = pd.DataFrame(analysis)
df.to_csv("data/raw/fraud_analysis.csv", index=False)