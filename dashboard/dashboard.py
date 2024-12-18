
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

# Title page
st.set_page_config(page_title="Air Quality from Wanshouxigong Analysis by odih nurzaman")


# Load dataset
data = pd.read_csv('./data/PRSA_Data_Wanshouxigong_20130301-20170228.csv')

# Title of the dashboard
st.title('Air Quality Analysis Dashboard: Wanshouxigong Station')



# Description
st.write('This dashboard provides an interactive way to explore air quality data, specifically focusing on PM2.5 levels and their relationship with various weather conditions.')


# About me
st.markdown("""
### About Me
- **Name**: Odih Nurzaman 
- **Email Address**: [odihnurzaman@gmail.com](mailto:odihnurzaman@gmail.com)
- **Dicoding ID**: [OdhNz](https://www.dicoding.com/users/odihnz/)

### Project Overview
This project aims to analyze air quality, with a particular focus on PM2.5 levels from the Wanshouxigong station. It explores seasonal trends and weather factors influencing air quality.
""")

# Adding a sidebar for interactive inputs
st.sidebar.header('User Input')

# Let users select a year and month to view data
selected_year = st.sidebar.selectbox('Select Year', list(data['year'].unique()))
selected_month = st.sidebar.selectbox('Select Month', list(data['month'].unique()))

# Filter data based on the selected year and month
data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)].copy()

# Displaying data statistics
st.subheader('Data Overview Selected Period')
st.write(data_filtered.describe())

# Line chart for PM2.5 levels over selected month
st.subheader('Daily PM2.5 Levels')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'])
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration')
st.pyplot(fig)

# Correlation heatmap for the selected month
st.subheader('Correlation Heatmap Air Quality Indicators')
corr = data_filtered[['PM2.5', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
plt.title('Correlation Heatmap')
st.pyplot(fig)

# Seasonal Trend Analysis
st.subheader('Seasonal Trend Analysis')
seasonal_trends = data.groupby('month')['PM2.5'].mean()
fig, ax = plt.subplots()
seasonal_trends.plot(kind='bar', color='skyblue', ax=ax)
plt.title('Average Monthly PM2.5 Levels')
plt.xlabel('Month')
plt.ylabel('Average PM2.5')
st.pyplot(fig)


# Daily PM2.5 Levels
st.subheader('Daily PM2.5 Levels')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'])
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration')
st.pyplot(fig)

# Pollutant Distribution
st.subheader('Pollutant Distribution')
selected_pollutant = st.selectbox('Select Pollutant', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
fig, ax = plt.subplots()
sns.boxplot(x='month', y=selected_pollutant, data=data[data['year'] == selected_year], ax=ax)
st.pyplot(fig)

# Time Series Decomposition of PM2.5
st.subheader('Time Series Decomposition of PM2.5')
try:
    data_filtered['PM2.5'].ffill(inplace=True)
    decomposed = seasonal_decompose(data_filtered['PM2.5'], model='additive', period=24) # Adjust period as necessary
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
    decomposed.trend.plot(ax=ax1, title='Trend')
    decomposed.seasonal.plot(ax=ax2, title='Seasonality')
    decomposed.resid.plot(ax=ax3, title='Residuals')
    plt.tight_layout()
    st.pyplot(fig)
except ValueError as e:
    st.error("Unable to perform time series decomposition: " + str(e))


# Hourly Averages Heatmap
st.subheader('Hourly Averages of PM2.5')
try:
    # Ensure correct data types and handle missing values
    data['hour'] = data['hour'].astype(int)
    data['PM2.5'] = pd.to_numeric(data['PM2.5'], errors='coerce')
    data['PM2.5'].ffill(inplace=True)

    # Calculate hourly averages
    hourly_avg = data.groupby('hour')['PM2.5'].mean()

    # Plotting
    fig, ax = plt.subplots()
    sns.heatmap([hourly_avg.values], ax=ax, cmap='coolwarm')
    plt.title('Hourly Averages of PM2.5')
    st.pyplot(fig)
except Exception as e:
    st.error(f"Error in plotting hourly averages: {e}")

# Wind Direction Analysis
st.subheader('Wind Direction Analysis')
wind_data = data_filtered.groupby('wd')['PM2.5'].mean()
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
theta = np.linspace(0, 2 * np.pi, len(wind_data))
bars = ax.bar(theta, wind_data.values, align='center', alpha=0.5)
plt.title('PM2.5 Levels by Wind Direction')
st.pyplot(fig)

# Rainfall vs. Air Quality
st.subheader('Rainfall vs. PM2.5 Levels')
fig, ax = plt.subplots()
sns.scatterplot(x='RAIN', y='PM2.5', data=data_filtered, ax=ax)
plt.title('Rainfall vs. PM2.5 Levels')
st.pyplot(fig)

# Correlation Heatmap - Interactive
st.subheader('Interactive Correlation Heatmap')
selected_columns = st.multiselect('Select Columns for Correlation', data.columns, default=['PM2.5', 'NO2', 'TEMP', 'PRES', 'DEWP'])
corr = data[selected_columns].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)


# Conclusion
st.subheader('Conclusion')
st.write("""
- The dashboard provides an in-depth and interactive analysis of air quality data.
- Various visualizations offer insights into PM2.5 levels, their distribution, and factors affecting them.
- Seasonal trends and the impact of different weather conditions and pollutants on air quality are clearly depicted.
- Users can explore the data dynamically to gain a deeper understanding of air quality trends.
""")