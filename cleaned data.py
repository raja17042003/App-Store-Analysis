import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna(subset=['App', 'Installs', 'Category'])
    df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
    df = df.dropna(subset=['Installs'])
    return df

def convert_size(size_str):
    if size_str.endswith('M'):
        return float(size_str[:-1]) * 1_000_000
    elif size_str.endswith('k'):
        return float(size_str[:-1]) * 1_000
    else:
        return None
