def most_and_least_installed(df):
    most = df.loc[df['Installs'].idxmax()]
    least = df.loc[df['Installs'].idxmin()]
    return most[['App', 'Category', 'Installs']], least[['App', 'Category', 'Installs']]

def top_categories_and_apps(df):
    top_cats = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(5)
    filtered = df[df['Category'].isin(top_cats.index)]
    top_apps = filtered.loc[filtered.groupby('Category')['Installs'].idxmax()]
    return top_cats, top_apps

def type_install_correlation(df):
    df = df.dropna(subset=['Type'])
    df['Type_num'] = df['Type'].map({'Free': 0, 'Paid': 1})
    df = df.dropna(subset=['Type_num'])
    return df['Type_num'].corr(df['Installs'])

def rating_extremes(df):
    df = df.dropna(subset=['Rating'])
    top = df.sort_values(by='Rating', ascending=False).head(5)
    low = df.sort_values(by='Rating').head(5)
    return top[['App', 'Rating']], low[['App', 'Rating']]

def size_price_correlation(df):
    df = df.dropna(subset=['Size', 'Price'])
    df = df[df['Size'] != 'Varies with device']
    df['Size'] = df['Size'].apply(convert_size)
    df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)
    df = df.dropna(subset=['Size', 'Price'])
    return df['Size'].corr(df['Price'])

def category_counts(df):
    return df['Category'].value_counts()

def avg_rating_by_cat_type(df):
    df = df.dropna(subset=['Category', 'Rating', 'Type'])
    df = df[df['Type'].isin(['Free', 'Paid'])]
    return df.groupby(['Category', 'Type'])['Rating'].mean().reset_index()

def content_rating_breakdown(df):
    ratings = df['Content Rating'].unique()
    breakdown = {}
    for rating in ratings:
        top = df[df['Content Rating'] == rating]['Category'].value_counts().head(5)
        breakdown[rating] = top
    return breakdown
