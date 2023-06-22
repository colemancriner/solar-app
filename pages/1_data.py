import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

# Initialize session state
st.session_state = st.session_state

# Retrieve data and date range from session state
df = st.session_state.usage.copy()
st.session_state.usage = df.copy()
df['ISO Date'] = pd.to_datetime(df['ISO Date'],format='%Y-%m-%dT%H:%M:%S')
hist_df = df.copy()

start = st.session_state.start_date
end = st.session_state.end_date

# Main page title
st.markdown("# Data Analysis")

# ------------SIDEBAR-------------

# Sidebar title
st.sidebar.markdown('# Data Analysis')

options = ['Hourly','Daily','Weekly','Monthly','Annual']
timeframe = st.sidebar.selectbox('Timeframe', options=options, help='Use this filter to see your Energy Data grouped by different timeframes. This will help to visualize large datasets.')

data = None
if timeframe == 'Hourly':
    data = df
    data['ISO Date'] = data['ISO Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
if timeframe == 'Daily':
    data = df.set_index('ISO Date')
    data = data.resample('D').sum()[['kWh','Cost']]
    data = data.reset_index()
    data['ISO Date'] = data['ISO Date'].dt.strftime('%Y-%m-%d')
if timeframe == 'Weekly':
    data = df.set_index('ISO Date')
    data = data.resample('W').sum()[['kWh','Cost']]
    data = data.reset_index()
    data['ISO Date'] = data['ISO Date'].dt.strftime('%Y-%m-%d')
if timeframe == 'Monthly':
    data = df.set_index('ISO Date')
    data = data.resample('M').sum()[['kWh','Cost']]
    data = data.reset_index()
    data['ISO Date'] = data['ISO Date'].dt.strftime('%Y-%m')
if timeframe == 'Annual':
    data = df.set_index('ISO Date')
    data = data.resample('Y').sum()[['kWh','Cost']]
    data = data.reset_index()
    data['ISO Date'] = data['ISO Date'].dt.strftime('%Y')

# ----------SIDEBAR: END----------

# Create columns for describe dataset and raw data
if st.checkbox('Show Tables',help='Checking this box will display the Describe Table that gives a brief overview of the SRP dataset. It will also show the SRP raw dataset.'):

    describe_col, raw_col = st.columns([1, 1])

    # Describe Dataset section
    with describe_col:
        st.subheader('Describe Dataset')
        st.dataframe(data.describe())

    # Raw Data section
    with raw_col:
        st.subheader('Raw Data')
        st.dataframe(df)


st.write('Showing data from '+str(data.loc[0,'ISO Date'])+' to '+str(data.loc[len(data)-1,'ISO Date']))
# Energy Usage line chart
st.subheader('Energy Usage')
st.line_chart(data, x='ISO Date', y=['kWh'])

# Energy Cost line chart
st.subheader('Energy Cost')
st.line_chart(data, x='ISO Date', y='Cost')


#----------Histograms by hour, day, and month-------------
hour_hist = hist_df.copy()
hour_hist['HourOfDay'] = hour_hist['ISO Date'].dt.hour
avg_cost_by_hour = hour_hist.groupby('HourOfDay')['Cost'].mean()
# Define the desired order for the hours of the day
hour_order = list(range(24))
# Reindex the series to ensure the labels appear in the desired order
avg_cost_by_hour = avg_cost_by_hour.reindex(hour_order)


week_hist = hist_df.copy()
week_hist['DayOfWeek'] = week_hist['ISO Date'].dt.strftime('%A')
avg_cost_by_day = week_hist.groupby('DayOfWeek')['Cost'].mean()
# Define the desired order for the days of the week
new_index = {'Sunday': '1 Sunday', 'Monday': '2 Monday', 'Tuesday': '3 Tuesday','Wednesday': '4 Wednesday', 'Thursday': '5 Thursday', 'Friday': '6 Friday', 'Saturday': '7 Saturday'}
avg_cost_by_day = avg_cost_by_day.rename(new_index)


month_hist = hist_df.copy()
month_hist['MonthOfYear'] = month_hist['ISO Date'].dt.month
avg_cost_by_month = month_hist.groupby('MonthOfYear')['Cost'].mean()
# Define the desired order for the months of the year
month_order = list(range(1, 13))
# Reindex the series to ensure the labels appear in the desired order
avg_cost_by_month = avg_cost_by_month.reindex(month_order)



# Write the histograms to website
st.subheader('Cost of Energy Use by Hour of the Day')
st.bar_chart(avg_cost_by_hour)
left_col,right_col = st.columns(2)
with left_col:
    st.subheader('Cost of Energy Use by Day of the Week')
    st.bar_chart(avg_cost_by_day)
with right_col:
    st.subheader('Cost of Energy Use by Month of the Year')
    st.bar_chart(avg_cost_by_month)


#----------Histograms by hour, day, and month: END-------------

