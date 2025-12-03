# Automotive Market Demand & Customer Segmentation Analysis

## ⭐ Overview
This project analyzes automotive demand patterns, customer purchase capacity, and regional vehicle trends using a structured dataset modeled after real business problems.

## 📂 Project Structure
```
automotive-market-analysis/
 ├── 📄 README.md               # Project documentation
 ├── 📄 data.csv                # Synthetic dataset
 ├── 📄 analysis.py             # Main analysis script (EDA, Clustering, Forecasting)
 ├── 📄 segmentation_model.ipynb # Jupyter Notebook for interactive analysis
 ├── 📄 insights_report.md      # Summary of key findings
 ├── 📄 requirements.txt        # Python dependencies
 └── 📂 dashboards/             # Generated plots and visualizations
```

## 🚀 Getting Started
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run Analysis**:
   ```bash
   python analysis.py
   ```
   This will generate visualizations in the `dashboards/` folder.
3. **Explore Notebook**:
   Open `segmentation_model.ipynb` in Jupyter/VS Code.

## ⭐ Key Features
- **Customer Segmentation**: K-Means clustering to identify Budget, Mid-tier, and Premium buyers.
- **Demand Forecasting**: Linear regression model to predict purchase probability.
- **Interactive Dashboards**: Visualizations of income distribution, vehicle preferences, and correlation matrices.

## ⭐ Insights
- **High-Income Segments** drive demand for EVs and Luxury vehicles.
- **Dealer Visits** are a key indicator of purchase intent.
- **Regional Trends** influence vehicle type preferences.
