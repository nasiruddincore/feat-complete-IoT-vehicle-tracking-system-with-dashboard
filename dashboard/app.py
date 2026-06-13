# dashboard/app.py
import streamlit as st
import pandas as pd
import os

# Set page configuration
st.set_page_config(page_title="IoT Vehicle Tracker", layout="wide")

st.title("🚗 IoT Vehicle Tracking & Theft Prevention Dashboard")

# Function to load data
def load_data():
    file_path = 'data/sensor_logs.csv'
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame(columns=['Timestamp', 'Lat', 'Lon', 'Status', 'Alert'])

# Sidebar
st.sidebar.header("System Controls")
if st.sidebar.button('Refresh Data'):
    st.rerun()

# Load and display data
df = load_data()

# Main Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Current Status", df['Status'].iloc[-1] if not df.empty else "N/A")
col2.metric("Latest Latitude", f"{df['Lat'].iloc[-1]:.4f}" if not df.empty else "N/A")
col3.metric("Latest Longitude", f"{df['Lon'].iloc[-1]:.4f}" if not df.empty else "N/A")

# Data Table
st.subheader("Historical Location & Alert Logs")
st.dataframe(df.sort_values(by='Timestamp', ascending=False), use_container_width=True)

# Alerts Area
if not df.empty and df['Alert'].iloc[-1] == "!!! THEFT ALERT !!!":
    st.error("⚠️ THEFT DETECTED! Vehicle moved outside the safe zone.")
else:
    st.success("✅ System Secure: Vehicle within safe zone.")