import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Food Delivery Analytics",
    page_icon="🥪",
    layout="wide"
)

# Main Title
st.title("🥪 FOOD DELIVERY ANALYTICS")
st.caption("Smart Business Intelligence Dashboard")
st.divider()

# Sidebar
st.sidebar.title("⚙️ Dashboard Settings")
st.sidebar.info("Food Delivery Business Analysis")

city = st.sidebar.selectbox(
    "Select City",
    ["All Cities", "Delhi", "Mumbai", "Bangalore", "Kanpur"]
)

period = st.sidebar.selectbox(
    "Select Period",
    ["Last 7 Days", "Last 30 Days", "Last 6 Months"]
)

# Dashboard Metrics
st.subheader("📊 Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", "12,500", "+12%")
col2.metric("Total Revenue", "₹8.5 L", "+18%")
col3.metric("Avg Order Value", "₹680", "+5%")
col4.metric("Customer Rating", "4.6 ⭐", "+0.3")

st.divider()

# Charts
left, right = st.columns(2)

with left:
    st.subheader("📈 Monthly Orders")

    orders = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Orders": [1200, 1500, 1800, 1600, 2200, 2500]
    })

    st.line_chart(orders.set_index("Month"))

with right:
    st.subheader("💰 Monthly Revenue")

    revenue = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": [120000, 150000, 180000, 160000, 220000, 250000]
    })

    st.bar_chart(revenue.set_index("Month"))

st.divider()

# Food Analysis
st.subheader("🍕 Top Selling Food Items")

food = pd.DataFrame({
    "Food Item": ["Pizza", "Burger", "Biryani", "Pasta", "Sandwich"],
    "Orders": [2500, 2200, 2000, 1500, 1000]
})

st.bar_chart(food.set_index("Food Item"))

st.divider()

# Dataset Upload
st.subheader("📂 Upload Your Dataset")

uploaded_file = st.file_uploader(
    "Upload Food Delivery CSV File",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset Uploaded Successfully!")

    st.write("Dataset Preview")
    st.dataframe(df, use_container_width=True)

    st.write("Dataset Statistics")
    st.write(df.describe())

st.divider()

st.success("Food Delivery Analytics Dashboard is Ready!")

st.caption("Developed with Python, Pandas and Streamlit")