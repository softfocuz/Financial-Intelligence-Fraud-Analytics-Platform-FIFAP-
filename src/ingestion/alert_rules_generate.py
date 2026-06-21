import pandas as pd
import uuid
from faker import Faker

generate = Faker()

rules = [
    ("Rapid transaction burst", "More than 5 transactions in 60 minutes", 40, 5, "count"),
    ("Abnormally high amount", "Purchase is more than 3 times what the customer normally spends", 35, 3, "multiplier"),
    ("Rapid consecutive transfers", "More than 3 transfers in 10 minutes", 30, 3, "count"),
    ("Unrecognized device", "Customer pays using a device they have never used before", 30, 1, "device"),
    ("Multiple failed logins", "More than 3 failed logins in 30 minutes", 25, 3, "count"),
    ("Unusual transaction location", "More than 500km from last known location", 25, 500, "km"),
    ("Middle-of-the-night transaction", "Transaction happens between 12AM and 5AM with no history of night spending", 20, 5, "hours"),
    ("High-risk merchant", "Merchant is in a high-risk category", 20, 1, "category")
]

alert_rules = []

for (
    rule_name,
    description,
    score,
    threshold_value,
    threshold_unit
) in rules:

    alert_rules.append({
        "rule_id": str(uuid.uuid4()),
        "rule_name": rule_name,
        "description": description,
        "score": score,
        "threshold_value": threshold_value,
        "threshold_unit": threshold_unit,
        "is_active": True,
        "created_at": generate.date_this_year(),
        "updated_at": generate.date_this_year()
    })

df = pd.DataFrame(alert_rules)
df.to_csv("data/raw/alert_rules.csv", index=False)
