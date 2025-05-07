import pandas as pd

def read_csv(filepath):
    return pd.read_csv(filepath)

def write_csv(df, filepath):
    df.to_csv(filepath, index=False)
