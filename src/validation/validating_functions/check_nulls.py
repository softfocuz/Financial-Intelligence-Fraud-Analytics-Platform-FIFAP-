from config import CRITICAL
from flag import flag

def check_nulls(df, table, columns, level=CRITICAL):
    issues = []
    for col in columns:
        n = df[col].isnull().sum()
        if n > 0:
            issues.append(flag(level, table, f'{n} nulls in {col} '))
    return issues