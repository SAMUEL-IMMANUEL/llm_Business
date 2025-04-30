
# 🧠 LLM-Powered Business Intelligence Assistant

This project is an AI-powered assistant that helps entrepreneurs explore and plan business setups based on their city and business type. It integrates a lightweight LLM with structured datasets to provide smart, actionable insights — including location suggestions, competition data, licensing requirements, loan options, and **sales analytics visualizations**.

---

## 🚀 Features

- 🔍 Search by **City** and **Business Type**
- 📍 Get suggested **Business Locations** based on foot traffic
- 🏢 View existing **Competitors**
- 📝 Retrieve required **Licenses & Permits**
- 💰 Explore **Loan Options**
- 📊 **Upload Sales Report CSV** to view **Graphical Insights**:
  - Best-selling product categories
  - Seasonal trends
  - Revenue breakdowns

---

## 📁 Dataset Overview

The assistant uses the following CSV files:

| Dataset Name         | Description                                  |
|----------------------|----------------------------------------------|
| `city_locations.csv` | City areas with foot traffic info            |
| `business_categories.csv` | Different business types and metadata |
| `competitors.csv`    | Existing businesses in various cities        |
| `licenses.csv`       | Required licenses per business type          |
| `bank_loans.csv`     | Loan options from different banks            |
| `sales_report.csv`   | *(Optional input)* Sales data for analysis   |

> All datasets should be placed inside the `datasets/` folder.

---

## 🛠️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Open in Google Colab**:
   - Upload your datasets.
   - Run the assistant using cells provided.

4. **Run the assistant**:
   ```bash
   python main.py
   ```

---

## 🧪 Sample Prompts to Try

Here are some ready-to-go demo prompts:

- `"Full setup report for a bakery in New York"`
- `"What licenses do I need to open a cafe in San Francisco?"`
- `"Show competitor analysis for bookstores in Chicago"`
- `"Suggest best locations to open a gym in Los Angeles"`
- `"Upload this sales report and tell me how to improve revenue"`

---

## 💡 Tech Stack

- Python
- Pandas
- Matplotlib / Seaborn (for visualizations)
- Lightweight LLM (Ollama / GPT-like backend)
- Google Colab for interactive execution

---

## 📂 Folder Structure

```
📁 datasets/
   ├── city_locations.csv
   ├── business_categories.csv
   ├── competitors.csv
   ├── licenses.csv
   ├── bank_loans.csv
   ├── sales_report.csv      # Optional
📄 main.py
📄 data_search.py
📄 sales_analyzer.py         # (if applicable)
📄 requirements.txt
📄 README.md
```
