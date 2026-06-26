import pandas as pd

from validating_functions.config import WARNING
from validating_functions.flag import flag

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values

def validate_customers(df):
    issues = []
    issues += check_nulls(df, "customers", ["customer_id", "first_name", "last_name", "email", "risk_tier"])
    issues += check_duplicates(df, "customers", "customer_id")
    issues += check_duplicates(df, "customers", "email", level=WARNING)
    issues += check_values(df, "customers", "risk_tier", ["LOW"], "MEDIUM", "HIGH")
    future_dob = (pd.to_datetime(df["birth_date"]) > pd.Timestamp.today()).sum()
    if future_dob > 0:
        issues.append(flag(WARNING, "customers", f"{future_dob} birth_date values in the future"))
    return issues