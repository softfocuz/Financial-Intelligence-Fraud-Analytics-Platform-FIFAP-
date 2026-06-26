import pandas as pd

from validating_functions.config import WARNING
from validating_functions.flag import flag

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values
from validating_functions.check_fk import check_fk

def validate_login_history(df, customers_df, devices_df):
    issues = []
    issues += check_nulls(df, "login_history", ["login_id", "customer_id", "device_id", "login_timestamp", "login_status"])
    issues += check_duplicates(df, "login_history", "login_id")
    issues += check_values(df, "login_history", "login_status", ["SUCCESS", "FAILED"])
    issues += check_fk(df, "login_history", "customer_id", customers_df, "customer_id")
    issues += check_fk(df, "login_history", "device_id", devices_df, "device_id")
    future_ts = (pd.to_datetime(df["login_timestamp"]) > pd.Timestamp.today()).sum()
    if future_ts > 0:
        issues.append(flag(WARNING, "login_history", f"{future_ts} login events with a future timestamp"))
    return issues