from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values

def validate_merchants(df):
    issues = []
    issues += check_nulls(df, "merchants", ["merchant_id", "name", "category", "risk_level"])
    issues += check_duplicates(df, "merchants", "merchant_id")
    issues += check_values(df, "merchants", "risk_level", ["LOW", "HIGH"])
    issues += check_values(df, "merchants", "category", ["Retail", "Food", "Travel", "Electronics",
                                                        "Healthcare", "Gambling", "Crypto", "Wire Transfer"
    ])
    return issues