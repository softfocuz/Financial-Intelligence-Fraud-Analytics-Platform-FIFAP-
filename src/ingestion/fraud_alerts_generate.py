import pandas as pd
import uuid
import random

analysis = pd.read_csv("data/raw/fraud_analysis.csv")

frauds = analysis[analysis["fraud_flag"] == True]
frauds = frauds.sample(n=min(1000, len(frauds)), random_state=42)

alerts = []

for _, row in frauds.iterrows():
    alerts.append({
        "alert_id": str(uuid.uuid4()),
        "transaction_id": row["transaction_id"],
        "analysis_id": row["analysis_id"],
        "alert_type": "Fraud Detection",
        "severity": random.choice([
            "HIGH",
            "CRITICAL"
        ]),
        "status": random.choice([
            "OPEN",
            "INVESTIGATING",
            "RESOLVED"
        ]),
        "created_at": pd.Timestamp.now(),
        "resolved_at": None
    })

df = pd.DataFrame(alerts)
df.to_csv("data/raw/fraud_alerts.csv", index=False)