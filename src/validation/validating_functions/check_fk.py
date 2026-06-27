from validating_functions.config import CRITICAL
from validating_functions.flag import flag

def check_fk(df, table, fk_col, parent_df, pk_col, level=CRITICAL):
    orphans = ~df[fk_col].isin(parent_df[pk_col])
    if orphans.sum() > 0:
        return [flag(level, table, f'{orphans.sum()} {fk_col} values not found in parent table')]
    return []