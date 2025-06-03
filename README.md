# 📊 Leveraging AI for Exploratory Data Analysis: App Store Dataset

This project provides an in-depth analysis of app store data, focusing on app ratings, installs, prices, and categories. The goal is to uncover patterns and insights that can inform decisions such as app development, pricing strategy, and market segmentation.

---

## 📁 Project Structure

app_store_analysis_project/

├── data  
│ └── app_store_data.csv # Raw dataset  
│  
├── scripts/  
│ ├── clean_data.py # Data cleaning functions  
│ ├── analysis.py # Statistical analysis of the give data  
│ └── charts.py # Seaborn/Matplotlib chart functions  
│  
├── outputs/  
│ ├── charts/ # PNGs of static charts  
│ └── analysis/ #  result of analysis  
│  
├── utils/  
│ └── helpers.py # Helper/utility functions  
│  
├── main.py # Script to run all analysis  
├── requirements.txt # List of Python dependencies  
└── README.md # Project overview and instructions  
# 🔍 Features
**🔍 1. Most & Least Installed Apps:**  
Identifies the app with the highest and lowest number of installs.  
Displays the app name, category, and install count.

**📊 2. Top 5 Categories by Installs:**  
Calculates total installs per category.  
Finds the top 5 categories.Identifies the top app (by installs) in each of these categories.  
Creates a side-by-side bar chart comparing:Total installs by category.  
Top app installs within each category.

**📈 3. Correlation: App Type vs Installs:**  
Maps app type to numeric: Free = 0, Paid = 1.  
computes Pearson correlation between type and installs.  
**Interpretation:**  
Positive = Paid apps are more installed.  
Negative = Free apps are more installed.  
Near zero = No strong linear relation.  
**⭐ 4. Top 5 Most & Least Rated Apps:**  
Sorts apps by rating.Displays the top 5 highest-rated and bottom 5 lowest-rated apps.  
Uses horizontal bar charts for both.  
**💰 5. Correlation: App Size vs Price:**  
Converts app size (e.g., “23M”, “500k”) into numeric values (bytes). 
Computes correlation between size and price.  
Interpretation tells whether larger apps tend to cost more or less.  
**📦 6. App Count per Category:**  
Counts the total number of apps in each category.  
Visualized using a vertical bar chart with category names.  
**📐 7. Average Rating by Category & Type:**  
Groups by both category and type (Free/Paid).
Computes average rating.
Uses a Seaborn point plot with values displayed to compare Free vs Paid apps across categories.  
**🧒 8. Content Rating Breakdown:**  
For each Content Rating (e.g., "Everyone", "Teen"):Displays a pie chart of the top 5 categories within that rating.  

## 🛠️ Tools & Technologies
**📦 Programming Language :**  Python – Main language used for data processing, analysis, and visualization.  
**🧠 AI TOOL :**  ChatGpt –  Assisted in generating code, designing project structure, and data analysis logic.
