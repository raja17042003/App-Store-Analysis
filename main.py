#Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
df = pd.read_csv("googleplaystore.csv")
df.head()

#1.most and least installed app
print('\t\t\tMost & Least Installed Apps')
# Clean data
df = df.dropna(subset=['App', 'Installs'])

# Find most and least installed apps
most_installed = df.loc[df['Installs'].idxmax()]
least_installed = df.loc[df['Installs'].idxmin()]


# Combine into a new DataFrame
extremes = pd.DataFrame([most_installed, least_installed])[['App', 'Category', 'Installs']]
print(extremes)

#2.top 5 Category


# Step 1: Get top 5 categories by total installs (descending first)
top_categories = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(5)

# Step 2: Sort top categories ascending by total installs
top_categories = top_categories.sort_values(ascending=True)

# Step 3: Filter dataset for these categories
filtered_df = df[df['Category'].isin(top_categories.index)]

# Step 4: Get most installed app from each top category
top_apps = filtered_df.loc[filtered_df.groupby('Category')['Installs'].idxmax()][['Category', 'App', 'Installs']]
top_apps.set_index('Category', inplace=True)

# Step 5: Prepare data for plotting
categories = top_categories.index
cat_totals = top_categories.values
app_installs = top_apps.loc[categories]['Installs'].values
app_names = top_apps.loc[categories]['App'].values

x = range(len(categories))
bar_width = 0.35

plt.figure(figsize=(12, 7))

# Plot total installs per category
bars1 = plt.bar(x, cat_totals, width=bar_width, label='Category Total Installs', color='skyblue')

# Plot most installed app installs
bars2 = plt.bar([i + bar_width for i in x], app_installs, width=bar_width, label='Top App Installs', color='orange')

# Add data labels for category totals
for i, val in enumerate(cat_totals):
    plt.text(i, val + val*0.02, f"{val:,}", ha='center', va='bottom', fontsize=9, color='blue')

# Add data labels for top apps and app names
for i, (val, app) in enumerate(zip(app_installs, app_names)):
    plt.text(i + bar_width, val + val*0.02, f"{val:,}", ha='center', va='bottom', fontsize=9, color='darkorange')
    plt.text(i + bar_width, val + val*0.10, app, ha='center', va='bottom', fontsize=8, rotation=90, color='black')

# Final formatting
plt.xticks([i + bar_width / 2 for i in x], categories, rotation=45)
plt.ylabel('Install Count')
plt.title('Top 5 Most Installed Categories & Their Top App (Ascending Order)')
plt.legend()
plt.tight_layout()
plt.show()

#3.correlation of type and install

# Clean and filter necessary columns
df = df.dropna(subset=['Type', 'Installs'])

# Encode 'Type': Free = 0, Paid = 1
df['Type_num'] = df['Type'].map({'Free': 0, 'Paid': 1})

# Drop rows with unknown Type values (if any)
df = df.dropna(subset=['Type_num'])

# Compute correlation
correlation = df['Type_num'].corr(df['Installs'])
print(f"Correlation between Type and Installs: {correlation:.4f}")

if correlation>0 :
    print("Paid apps have more installs than free apps")
if correlation<0 :
    print("Free apps have more installs than paid apps")
else :
    print("both have same installs")
    
#4.top 5 most and least rated app

df = df.dropna(subset=['App', 'Rating'])

# Convert Rating to numeric
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Rating'])

# Get top 5 most rated apps
top_5_most = df.sort_values(by='Rating', ascending=False).head(5)[['App', 'Rating']]

# Get top 5 least rated apps
top_5_least = df.sort_values(by='Rating', ascending=True).head(5)[['App', 'Rating']]

# Plot settings
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Bar chart for top 5 most rated apps
axes[0].barh(top_5_most['App'], top_5_most['Rating'], color='green')
axes[0].set_title('Top 5 Most Rated Apps')
axes[0].set_xlabel('Rating')
axes[0].invert_yaxis()  # Highest rating on top

# Show rating values
for i, (app, rating) in enumerate(zip(top_5_most['App'], top_5_most['Rating'])):
    axes[0].text(rating + 0.02, i, f"{rating:.2f}", va='center')

# Bar chart for top 5 least rated apps
axes[1].barh(top_5_least['App'], top_5_least['Rating'], color='red')
axes[1].set_title('Top 5 Least Rated Apps')
axes[1].set_xlabel('Rating')
axes[1].invert_yaxis()  # Lowest rating on top

# Show rating values
for i, (app, rating) in enumerate(zip(top_5_least['App'], top_5_least['Rating'])):
    axes[1].text(rating + 0.02, i, f"{rating:.2f}", va='center')

plt.tight_layout()
plt.show()

#5.Correlation of size and price of app

# Clean 'Size' column
df = df.dropna(subset=['Size', 'Price'])
df = df[df['Size'] != 'Varies with device']

# Convert Size to numeric (in bytes)
def convert_size(size_str):
    if size_str.endswith('M'):
        return float(size_str[:-1]) * 1_000_000
    elif size_str.endswith('k'):
        return float(size_str[:-1]) * 1_000
    else:
        return None

df['Size'] = df['Size'].apply(convert_size)

# Clean and convert Price column
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)

# Drop rows with missing or non-convertible Size
df = df.dropna(subset=['Size', 'Price'])

# Calculate correlation
correlation = df['Size'].corr(df['Price'])
print(f"\nCorrelation between Size and Price: {correlation:.4f}")

if correlation>0 :
    print("Larger apps tend to cost more")
if correlation<0 :
    print("Larger apps tend to cost less")
else :
    print("Little or no linear relationship between size and price")

#6.Total Apps from each Category

# Drop missing categories
df = df.dropna(subset=['Category'])

# Count total apps per category
category_counts = df['Category'].value_counts().sort_values(ascending=False)

# Plot
plt.figure(figsize=(12, 8))
bars = plt.bar(category_counts.index, category_counts.values, color='blue')

# Add data labels above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 5, str(height),
             ha='center', va='bottom', fontsize=9, color='black')

# Formatting
plt.title('Total Apps from Each Category')
plt.xlabel('Category')
plt.ylabel('Number of Apps')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#7.rating and Category


df = df.dropna(subset=['Category', 'Rating', 'Type'])

# Convert Rating to numeric
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Rating'])
df = df[df['Type'].isin(['Free', 'Paid'])]

# Calculate average ratings per Category and Type
avg_ratings = df.groupby(['Category', 'Type'])['Rating'].mean().reset_index()

# Sort categories by total number of apps (optional: helps with clearer plot)
top_categories = df['Category'].value_counts().index.tolist()
avg_ratings['Category'] = pd.Categorical(avg_ratings['Category'], categories=top_categories, ordered=True)
avg_ratings = avg_ratings.sort_values('Category')

# Plot the pointplot
plt.figure(figsize=(14, 7))
ax = sns.pointplot(
    data=avg_ratings,
    x='Category',
    y='Rating',
    hue='Type',
    dodge=0.5,
    markers=['o', 's'],
    palette='Set1'
)

# Add data values (rating) next to each point
for i in range(len(avg_ratings)):
    row = avg_ratings.iloc[i]
    x = list(avg_ratings['Category'].cat.categories).index(row['Category'])
    offset = -0.2 if row['Type'] == 'Free' else 0.2
    ax.text(x + offset, row['Rating'] + 0.02, f"{row['Rating']:.2f}", 
            ha='center', va='bottom', fontsize=8)

# Formatting
plt.xticks(rotation=90)
plt.title('Average Rating by Category and Type (with Values)')
plt.xlabel('Category')
plt.ylabel('Average Rating')
plt.legend(title='App Type')
plt.tight_layout()
plt.show()

# 8.Get unique content ratings
ratings = df['Content Rating'].unique()

# Set up plot layout
n_cols = 3
n_rows = -(-len(ratings) // n_cols)  # ceiling division

plt.figure(figsize=(n_cols * 5, n_rows * 5))

# Create a pie chart per content rating
for i, rating in enumerate(ratings, 1):
    # Filter data for the current content rating
    sub_df = df[df['Content Rating'] == rating]
    # Count categories
    category_counts = sub_df['Category'].value_counts().head(5)  # Top 5 categories

    # Create subplot
    plt.subplot(n_rows, n_cols, i)
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"Top 5 Categories apps rated by - {rating}")

plt.tight_layout()
plt.show()