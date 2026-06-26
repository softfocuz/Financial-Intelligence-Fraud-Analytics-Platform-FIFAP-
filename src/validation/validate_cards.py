import pandas as pd
from validating_functions.config import CRITICAL, WARNING
from validating_functions.flag import flag

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values
from validating_functions.check_fk import check_fk

def validate_cards(df, accounts_df):
    issues = []
    issues += check_nulls(df, "cards", ["card_id", "account_id", "card_number", "card_type", "status", "expiry_date"])
    issues += check_duplicates(df, "cards", "card_id")
    issues += check_duplicates(df, "cards", "card_number")
    issues += check_values(df, "cards", "card_type", ["DEBIT", "CREDIT"])
    issues += check_values(df, "cards", "status", ["ACTIVE", "BLOCKED", "EXPIRED"])
    issues += check_fk(df, "cards", "account_id", accounts_df, "account_id")
    expired = df[df["status"] == "EXPIRED"]
    future_expiry = (pd.to_datetime(expired["expiry_date"]) > pd.Timestamp.today()).sum()
    if future_expiry > 0:
        issues.append(flag(CRITICAL, "cards", f"{future_expiry} EXPIRED cards with a future expiry date"))
    active = df[df["status"].isin(["ACTIVE", "BLOCKED"])]
    past_expiry = (pd.to_datetime(active["expiry_date"]) < pd.Timestamp.today()).sum()
    if past_expiry > 0:
        issues.append(flag(WARNING, "cards", f"{past_expiry} ACTIVE/BLOCKED cards with a past expiry date"))