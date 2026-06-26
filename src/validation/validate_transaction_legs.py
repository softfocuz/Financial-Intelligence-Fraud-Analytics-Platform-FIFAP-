from validating_functions.config import CRITICAL
from validating_functions.flag import flag

from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values
from validating_functions.check_fk import check_fk

def validate_transaction_legs(df, transactions_df, accounts_df):
    issues = []
    issues += check_nulls(df, "transaction_legs", ["leg_id", "transaction_id", "account_id", "direction", "amount"])
    issues += check_duplicates(df, "transaction_legs", "leg_id")
    issues += check_values(df, "transaction_legs", "direction", ["DEBIT", "CREDIT"])
    issues += check_fk(df, "transaction_legs", "transaction_id", transactions_df, "transaction_id")
    issues += check_fk(df, "transaction_legs", "account_id", accounts_df, "account_id")
    non_positive = (df["amount"] <= 0).sum()
    if non_positive > 0:
        issues.append(flag(CRITICAL, "transaction_legs", f"{non_positive} legs with amount <= 0"))
    leg_counts = df.groupby("transaction_id").size()
    not_two = (leg_counts != 2).sum()
    if not_two > 0:
        issues.append(flag(CRITICAL, "transaction_legs", f"{not_two} transactions without exactly 2 legs"))
    same_account = df.groupby("transaction_id")["account_id"].nunique()
    same = (same_account == 1).sum()
    if same > 0:
        issues.append(flag(CRITICAL, "transaction_legs", f"{same} transfers where DEBIT and CREDIT use the same account"))
    return issues