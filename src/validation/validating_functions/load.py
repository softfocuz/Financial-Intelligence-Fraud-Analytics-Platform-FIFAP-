import pandas as pd
import os

from config import RAW

def load(filename):
    df = pd.read_csv(os.path.join(RAW, filename))
    return df