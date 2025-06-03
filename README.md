# 📊 App Store Ratings & Insights Analyzer (Using AI)

# 📌 Overview

This project analyzes a dataset of apps from the Google Play Store to uncover patterns, trends, and insights related to installs, ratings, prices, and categories. The development process was accelerated using AI tools (ChatGPT), demonstrating how modern AI can complement human-driven data science.

---

# 🔍 Features
- 📥 Identify the most and least installed apps

- 🏆 Analyze the top 5 app categories by total installs and highlight the top app in each

- 💰 Evaluate the correlation between app type (Free/Paid) and installs

- ⭐ Compare the top 5 highest and lowest rated apps

- 📏 Analyze the relationship between app size and price

- 📊 Visualize the distribution of apps across categories

- 📈 Compare average ratings by app type (Free/Paid) across categories

- 🧒 Explore content rating breakdown using pie charts

---

## 🛠️ Tools & Technologies

| Tool                 | Purpose                                                                         |
| -------------------- | ------------------------------------------------------------------------------- |
| **Python**           | Core programming language                                                       |
| **Pandas**           | Data loading, cleaning, transformation                                          |
| **Matplotlib**       | Custom visualizations (bar, pie, etc.)                                          |
| **Seaborn**          | Advanced statistical plots                                                      |
| **ChatGPT (OpenAI)** | Assisted in generating and refining code, analysis logic, and project structure |


---

## 📂 Dataset

- <a href="https://github.com/raja17042003/App-Store-Analysis/blob/main/Play_Store_Apps_Data.xlsx">Play_Store_Apps_Data</a>

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

---

# 🚀 How to Run
**1. Clone this repository**
git clone https://github.com/yourusername/app-store-analyzer.git
cd app-store-analyzer
