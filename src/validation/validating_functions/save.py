import os

from validating_functions.config import PROCESSED

def save(df, filename):
    df.to_csv(os.path.join(PROCESSED, filename), index=False)