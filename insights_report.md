# Automotive Market Analysis: Insights Report

## Executive Summary
This report summarizes the findings from the analysis of 1,000 customer records. The goal was to understand market demand, segment customers, and forecast purchase probability.

## Key Findings

### 1. Customer Segmentation
Using K-Means clustering, we identified three distinct customer segments:
- **Budget Buyers**: Lower income, preference for Hatchbacks and Sedans.
- **Mid-Market**: Moderate income, mixed preference for SUVs and Sedans.
- **Premium/Luxury**: High income (> $100k), strong preference for Luxury and EV models.

### 2. Vehicle Preference Trends
- **SUVs** are the most popular category across the mid-to-high income range.
- **EV adoption** is strongly correlated with higher income and younger demographics in urban regions.
- **Regional differences**: The 'North' region shows a slightly higher affinity for SUVs compared to 'South'.

### 3. Purchase Probability Drivers
- **Annual Income** is the strongest predictor of purchase probability.
- **Dealer Visits**: Customers with 3-5 dealer visits have the highest conversion probability.
- **Age**: Younger customers (25-35) show higher interest in EVs but have lower immediate purchasing power compared to the 45-55 age group.

## Recommendations
1. **Target Premium Segment**: Launch targeted campaigns for Luxury/EV models in high-income regions.
2. **Mid-Market Strategy**: Focus on financing options for the mid-market segment to convert high interest into sales.
3. **Dealer Engagement**: Optimize dealer follow-up processes for customers with >3 visits to maximize conversion.

## Methodology
- **Data Source**: Synthetic dataset modeling real-world automotive trends.
- **Techniques**: EDA, K-Means Clustering, Linear Regression.
- **Tools**: Python (Pandas, Scikit-learn, Seaborn).
