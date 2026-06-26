import pandas as pd

from validating_functions.flag import flag
from validating_functions.config import CRITICAL

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values
from validating_functions.check_fk import check_fk

def validate_fraud_alerts(df, transactions_df, analysis_df):
    issues = []
    issues += check_nulls(df, "fraud_alerts", ["alert_id", "transaction_id", "analysis_id", "severity", "status"])
    issues += check_duplicates(df, "fraud_alerts", "alert_id")
    issues += check_values(df, "fraud_alerts", "severity", ["HIGH", "CRITICAL"])
    issues += check_values(df, "fraud_alerts", "status", ["OPEN", "INVESTIGATING", "RESOLVED"])
    issues += check_fk(df, "fraud_alerts", "transaction_id", transactions_df, "transaction_id")
    issues += check_fk(df, "fraud_alerts", "analysis_id", analysis_df, "analysis_id")
    resolved = df[df["status"] == "RESOLVED"].copy()
    if len(resolved) > 0 and resolved["resolved_at"].notnull().any():
        resolved["resolved_at"] = pd.to_datetime(resolved["resolved_at"])
        resolved["created_at"]  = pd.to_datetime(resolved["created_at"])
        bad = (resolved["resolved_at"] < resolved["created_at"]).sum()
        if bad > 0:
            issues.append(flag(CRITICAL, "fraud_alerts", f"{bad} RESOLVED alerts where resolved_at is before created_at"))
    return issues