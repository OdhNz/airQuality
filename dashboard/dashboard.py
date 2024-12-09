import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

# Title page
st.set_page_config(page_title="Air Quality Analysis Dashboard", page_icon="🌱", layout="wide")

# Load dataset
data = pd.read_csv('./data/PRSA_Data_Wanshouxigong_20130301-20170228.csv')

# Title of the dashboard
st.title('🌿 Air Quality Analysis Dashboard: Wanshouxigong Station 🌿')

# Description
st.markdown("""
This dashboard presents an analysis of air quality data from the Wanshouxigong station, 
with a focus on PM2.5 levels and their relationship with various weather conditions. 
Explore trends, seasonality, and the impact of weather on air quality.
""")

# Sidebar: User Input Features
st.sidebar.header('📊 Explore Data')
selected_year = st.sidebar.selectbox('Select Year', list(data['year'].unique()))
selected_month = st.sidebar.selectbox('Select Month', list(data['month'].unique()))

# Sidebar: About Me
st.sidebar.markdown("""
### About Me
👤 **Name**: Odih Nurzaman  
📧 **Email**: [odihnurzaman@gmail.com](mailto:odihnurzaman@gmail.com)  
🌍 **LinkedIn**: [Odih Nurzaman](https://www.linkedin.com/in/odih-nurzaman/)  
🌐 **Dicoding Profile**: [OdhNz](https://www.dicoding.com/users/odihnz/)

**Project Overview**:  
This project aims to analyze air quality, with a particular focus on PM2.5 levels from the Wanshouxigong station. It explores seasonal trends and weather factors influencing air quality.
""")

# Filter data based on the selected year and month
data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)].copy()

# Check if data is filtered correctly
if data_filtered.empty:
    st.warning(f"No data available for {selected_month}/{selected_year}. Please select another option.")
else:
    # Data Overview
    st.subheader(f"Data Overview for {selected_month}/{selected_year}")
    st.write(data_filtered.describe())

    # Layout with two columns for graphs
    col1, col2 = st.columns(2)

    with col1:
        # Line chart for PM2.5 levels over selected month
        st.subheader('Daily PM2.5 Levels')
        fig, ax = plt.subplots()
        ax.plot(data_filtered['day'], data_filtered['PM2.5'], color='darkgreen', linewidth=2)
        ax.set_xlabel('Day of the Month')
        ax.set_ylabel('PM2.5 Concentration')
        plt.title(f"PM2.5 Levels for {selected_month}/{selected_year}")
        st.pyplot(fig)

    with col2:
        # Correlation heatmap for the selected month
        st.subheader('Correlation Heatmap of Air Quality Indicators')
        corr = data_filtered[['PM2.5', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP']].corr()
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, ax=ax, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap')
        st.pyplot(fig)

    # Seasonal Trend Analysis
    st.subheader('Seasonal Trend of PM2.5 Levels')
    seasonal_trends = data.groupby('month')['PM2.5'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    seasonal_trends.plot(kind='bar', color='skyblue', ax=ax)
    plt.title('Average Monthly PM2.5 Levels')
    plt.xlabel('Month')
    plt.ylabel('Average PM2.5')
    st.pyplot(fig)

    # Pollutant Distribution
    st.subheader('Pollutant Distribution')
    selected_pollutant = st.selectbox('Select Pollutant', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='month', y=selected_pollutant, data=data[data['year'] == selected_year], ax=ax)
    plt.title(f'{selected_pollutant} Distribution')
    st.pyplot(fig)

    # Time Series Decomposition of PM2.5
    st.subheader('Time Series Decomposition of PM2.5')
    try:
        data_filtered['PM2.5'].ffill(inplace=True)
        decomposed = seasonal_decompose(data_filtered['PM2.5'], model='additive', period=24)
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
        decomposed.trend.plot(ax=ax1, title='Trend', color='green')
        decomposed.seasonal.plot(ax=ax2, title='Seasonality', color='orange')
        decomposed.resid.plot(ax=ax3, title='Residuals', color='red')
        plt.tight_layout()
        st.pyplot(fig)
    except ValueError as e:
        st.error("Unable to perform time series decomposition: " + str(e))

    # Wind Direction Analysis
    st.subheader('Wind Direction Analysis')
    wind_data = data_filtered.groupby('wd')['PM2.5'].mean()
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, polar=True)
    theta = np.linspace(0, 2 * np.pi, len(wind_data))
    bars = ax.bar(theta, wind_data.values, align='center', alpha=0.6, color='salmon')
    plt.title('PM2.5 Levels by Wind Direction')
    st.pyplot(fig)

    # Rainfall vs. Air Quality
    st.subheader('Rainfall vs. PM2.5 Levels')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='RAIN', y='PM2.5', data=data_filtered, ax=ax, color='purple')
    plt.title('Rainfall vs. PM2.5 Levels')
    st.pyplot(fig)

    # Conclusion
    st.subheader('Conclusion')
    st.write("""
    - The dashboard provides an interactive exploration of air quality data.
    - Insights into PM2.5 levels, pollutant distribution, and seasonal variations are clearly presented.
    - Weather conditions, including wind direction, temperature, and rainfall, have significant correlations with air quality.
    - Users can dive deeper into specific months, pollutants, and trends to make informed decisions.
    """)
