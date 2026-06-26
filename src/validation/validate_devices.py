from validating_functions.check_nulls import check_nulls
from validating_functions.check_duplicates import check_duplicates
from validating_functions.check_values import check_values
from validating_functions.check_fk import check_fk

def validate_devices(df, customers_df):
    issues = []
    issues += check_nulls(df, "devices", ["device_id", "customer_id", "device_type"])
    issues += check_duplicates(df, "devices", "device_id")
    issues += check_values(df, "devices", "device_type", ["Mobile", "Laptop", "Tablet"])
    issues += check_values(df, "devices", "os", ["Android", "iOS", "Windows", "macOS", "iPadOS"])
    issues += check_fk(df, "devices", "customer_id", customers_df, "customer_id")
    return issues