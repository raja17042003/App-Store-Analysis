# Any utility functions (e.g., size conversion) that may be reused across modules
def convert_size(size_str):
    if size_str.endswith('M'):
        return float(size_str[:-1]) * 1_000_000
    elif size_str.endswith('k'):
        return float(size_str[:-1]) * 1_000
    else:
        return None
