from validating_functions.config import CRITICAL
from validating_functions.flag import flag

def check_duplicates(df, table, column, level=CRITICAL):
    n = df[column].duplicated().sum()
    if n > 0:
        return [flag(level, table, f"{n} duplicate values in '{column}'")]
    return []