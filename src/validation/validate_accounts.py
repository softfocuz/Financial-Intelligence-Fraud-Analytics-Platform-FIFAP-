import pandas as pd

from validating_functions.config import CRITICAL
from validating_functions.flag import flag

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values
from validating_functions.check_fk import check_fk

def validate_accounts(df, customers_df):
    issues = []
    issues += check_nulls(df, "accounts", ["account_id", "customer_id", "account_number", "account_type", "balance", "status"])
    issues += check_duplicates(df, "accounts", "account_id")
    issues += check_duplicates(df, "accounts", "account_number")
    issues += check_values(df, "accounts", "account_type", ["Savings", "Checking"])
    issues += check_values(df, "accounts", "status", ["ACTIVE", "DORMANT", "CLOSED"])
    issues += check_values(df, "accounts", "currency", ["PHP"])
    issues += check_fk(df, "accounts", "customer_id", customers_df, "customer_id")
    negative = (df["balance"] < 0).sum()
    if negative > 0:
        issues.append(flag(CRITICAL, "accounts", f"{negative} negative balance values"))
    bad_dates = (pd.to_datetime(df["updated_at"]) < pd.to_datetime(df["created_at"])).sum()
    if bad_dates > 0:
        issues.append(flag(CRITICAL, "accounts", f"{bad_dates} rows where updated_at is before created_at"))
    return issues