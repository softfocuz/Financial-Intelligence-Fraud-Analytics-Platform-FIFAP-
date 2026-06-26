from validating_functions.config import CRITICAL
from validating_functions.flag import flag

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates

def validate_alert_rules(df):
    issues = []
    issues += check_nulls(df, "alert_rules", ["rule_id", "rule_name", "score", "threshold_value", "threshold_unit"])
    issues += check_duplicates(df, "alert_rules", "rule_id")
    issues += check_duplicates(df, "alert_rules", "rule_name")
    if len(df) != 8:
        issues.append(flag(CRITICAL, "alert_rules", f"expected 8 rules, found {len(df)}"))
    if (df["score"] <= 0).sum() > 0:
        issues.append(flag(CRITICAL, "alert_rules", f"{(df['score'] <= 0).sum()} rules with score <= 0"))
    if (df["threshold_value"] <= 0).sum() > 0:
        issues.append(
            flag(CRITICAL, "alert_rules", f"{(df['threshold_value'] <= 0).sum()} rules with threshold_value <= 0"))
    return issues