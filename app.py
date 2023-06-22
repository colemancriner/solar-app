import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
from datetime import time
from srpenergy.client import SrpEnergyClient
import plotly.express as px
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Set page configuration
st.set_page_config(page_title='Real-Time Solar', page_icon=':dim_button:', layout='wide')

# Global variables for data and date range
global usage
global start_date
global end_date

# Function to fetch data using SRP Energy API
@st.cache_data
def fetch_data(account_id, username, password, start_date, end_date):
    # Create an instance of SrpEnergyClient
    client = SrpEnergyClient(account_id, username, password)
    
    # Retrieve usage data from the client for the specified date range
    usage = client.usage(start_date, end_date)
    
    # Create a DataFrame from the retrieved usage data
    df = pd.DataFrame(usage, columns=['Date', 'Hour', 'ISO Date', 'kWh', 'Cost'])
    
    return df

#-----------SIDEBAR----------------
# input fields for SRP Energy API credentials
st.sidebar.subheader('SRP Energy API Credentials')
account_id = st.sidebar.text_input('Account ID', key='account_id')
username = st.sidebar.text_input('Username', key='username')
password = st.sidebar.text_input('Password', type='password', key='password')
#-----------SIDEBAR: END-----------

#---------Instructions for user---------------
st.header('SRP Energy')
st.subheader('Instructions:')
"""
1. Using the sidebar menu, sign into your SRP account.
2. Choose the timeframe you would like to see your energy data for.
3. Press Fetch Data button.
4. If a table is displayed after you press the button, your SRP data has been loaded successfully.
5. Navigate to the Data tab from the sidebar menu in order to see your energy consumption insights.
"""
#---------Instructions for user: END----------

# Timeframe input fields
column1, column2 = st.columns([1, 1])
with column1:
    start_date = st.date_input('Start Date', value=datetime.now() - timedelta(days=2))
    st.write(start_date)
    end_date = st.date_input('End Date', value=datetime.now())
    st.write(end_date)
with column2:
    start_time = st.time_input('Start Time', value=time(12, 00))
    st.write(start_time)
    end_time = st.time_input('End Time', value=time(11, 59))
    st.write(end_time)

# Format datetime objects for the client
start_date = datetime.combine(start_date, start_time)
end_date = datetime.combine(end_date, end_time)

# Button to fetch data
st.session_state.fetch_button = st.button('Fetch Data', key='fetch_button1')

usage = None


# Display data if fetch button is clicked
describe_col, raw_col = st.columns([1, 2])
if st.session_state.fetch_button:
    usage = fetch_data(st.session_state.account_id, st.session_state.username, st.session_state.password, start_date, end_date)
    st.subheader('Raw Dataset')
    st.dataframe(usage)

# Store data and date range in session state
st.session_state.usage = usage
st.session_state.start_date = start_date
st.session_state.end_date = end_date
