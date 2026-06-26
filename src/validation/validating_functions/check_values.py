from config import CRITICAL
from flag import flag

def check_values(df, table, column, allowed, level=CRITICAL):
    invalid = ~df[column].isin(allowed)
    if invalid.sum() > 0:
        return [flag(level, table, f"{invalid.sum()} invalid values in '{column}': {df[column][invalid].unique().tolist()}")]
    return []