from validating_functions.config import CRITICAL, WARNING
from validating_functions.flag import flag

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values
from validating_functions.check_fk import check_fk

def validate_fraud_analysis(df, transactions_df):
    issues = []
    issues += check_nulls(df, "fraud_analysis", ["analysis_id", "transaction_id", "fraud_score", "risk_level", "fraud_flag"])
    issues += check_duplicates(df, "fraud_analysis", "analysis_id")
    issues += check_duplicates(df, "fraud_analysis", "transaction_id")
    issues += check_values(df, "fraud_analysis", "risk_level", ["LOW", "MEDIUM", "HIGH", "CRITICAL"])
    issues += check_fk(df, "fraud_analysis", "transaction_id", transactions_df, "transaction_id")
    out_of_range = ((df["fraud_score"] < 0) | (df["fraud_score"] > 1)).sum()
    if out_of_range > 0:
        issues.append(flag(CRITICAL, "fraud_analysis", f"{out_of_range} fraud_score values outside 0.0–1.0"))
    if len(df) != len(transactions_df):
        issues.append(flag(WARNING, "fraud_analysis", f"{len(df)} analysis records vs {len(transactions_df)} transactions"))
    return issues