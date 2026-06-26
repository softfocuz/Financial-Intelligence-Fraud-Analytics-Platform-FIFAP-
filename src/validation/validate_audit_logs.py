from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values

def validate_audit_logs(df):
    issues = []
    issues += check_nulls(df, "audit_logs", ["log_id", "table_name", "record_id", "action", "performed_by", "timestamp"])
    issues += check_duplicates(df, "audit_logs", "log_id")
    issues += check_values(df, "audit_logs", "action", ["INSERT", "UPDATE", "DELETE"])
    issues += check_values(df, "audit_logs", "performed_by", ["SYSTEM", "ADMIN"])
    issues += check_values(df, "audit_logs", "table_name", [
        "customers", "accounts", "cards", "devices", "transactions", "fraud_analysis"
    ])
    return issues