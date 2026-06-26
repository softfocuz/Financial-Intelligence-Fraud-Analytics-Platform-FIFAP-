import pandas as pd

from validating_functions.config import CRITICAL, WARNING
from validating_functions.flag import flag

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values
from validating_functions.check_fk import check_fk

def validate_transactions(df, accounts_df, cards_df, merchants_df, devices_df):
    issues = []
    issues += check_nulls(df, "transactions", [
        "transaction_id", "account_id", "merchant_id", "device_id",
        "transaction_type", "transaction_status", "amount",
        "currency", "transaction_timestamp", "channel"
    ])
    issues += check_duplicates(df, "transactions", "transaction_id")
    issues += check_duplicates(df, "transactions", "reference_number")
    issues += check_values(df, "transactions", "transaction_type", ["PURCHASE", "TRANSFER", "WITHDRAWAL", "PAYMENT"])
    issues += check_values(df, "transactions", "transaction_status", ["SUCCESS", "FAILED"])
    issues += check_values(df, "transactions", "channel", ["ATM", "ONLINE", "POS", "MOBILE"])
    issues += check_values(df, "transactions", "currency", ["PHP"])
    issues += check_fk(df, "transactions", "account_id", accounts_df, "account_id")
    issues += check_fk(df, "transactions", "card_id", cards_df, "card_id")
    issues += check_fk(df, "transactions", "merchant_id", merchants_df, "merchant_id")
    issues += check_fk(df, "transactions", "device_id", devices_df, "device_id")
    non_positive = (df["amount"] <= 0).sum()
    if non_positive > 0:
        issues.append(flag(CRITICAL, "transactions", f"{non_positive} transactions with amount <= 0"))
    future_ts = (pd.to_datetime(df["transaction_timestamp"]) > pd.Timestamp.today()).sum()
    if future_ts > 0:
        issues.append(flag(WARNING, "transactions", f"{future_ts} transactions with a future timestamp"))
    return issues