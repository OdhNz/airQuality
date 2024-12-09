# Air Quality Analysis: Wanshouxigong Station

## 🚀 [Live Dashboard](https://odihn-airquality.streamlit.app/)

## Overview

This project analyzes air quality data from the Wanshouxigong station, focusing on PM2.5 levels. It explores trends, seasonal variations, and the influence of weather conditions on air quality.

### Course Submission

This analysis is part of the **"Learn Data Analysis with Python"** course on **Dicoding**, showcasing the application of data analysis techniques learned in the course.

## Table of Contents

- [Introduction](#introduction)
- [Data Source](#data-source)
- [Libraries Used](#libraries-used)
- [Key Insights](#key-insights)
- [How to Run the Dashboard](#how-to-run-the-dashboard)
- [About Me](#about-me)

---

## Introduction

This project aims to analyze PM2.5 levels and their relationship with weather conditions, uncovering seasonal patterns and trends to better understand air quality.

## Data Source

The dataset consists of air quality measurements, specifically PM2.5 levels, from the Wanshouxigong station, along with related environmental data.

## Libraries Used

- **Streamlit**: For building the interactive dashboard
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Data visualization
- **NumPy**: Numerical operations
- **Statsmodels**: Time series analysis

## Key Insights

- Higher PM2.5 concentrations are observed in colder months.
- Temperature and humidity show strong correlations with PM2.5 levels.
- Seasonal trends and patterns in air quality are revealed through time series analysis.

---

## How to Run the Dashboard

### Setup Environment

1. **Create and Activate a Python Environment**:

   - **With Conda**:

     ```
     conda create --name airquality-ds python=3.9
     conda activate airquality-ds
     ```

   - **With venv**:
     ```
     python -m venv airquality-ds
     source airquality-ds/bin/activate  # For Windows: `airquality-ds\Scriptsctivate`
     ```

2. **Install Required Packages**:
   ```
   pip install -r requirements.txt
   ```

### Run the App

1. Navigate to the project directory (where `dashboard.py` is located).
2. Run the Streamlit app:
   ```
   streamlit run dashboard.py
   ```

---

## About Me

- **Name**: Odih Nurzaman
- **Email**: [odihnurzaman@gmail.com](mailto:odihnurzaman@gmail.com)
- **Dicoding ID**: [odihnz](https://www.dicoding.com/users/odihnz/)

Find my notebook on Kaggle: [Air Quality Analysis - Kaggle](https://www.kaggle.com/odhnurzaman/air-quality)

---
