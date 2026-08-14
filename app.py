import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Inventory Reorder Alert System",
    page_icon="📦",
    layout="wide"
)

st.sidebar.title("📦 Inventory Dashboard")

st.sidebar.markdown("""
### Features
- 📊 Dashboard Summary
- 🔍 Inventory Filter
- 📥 Download Report

### Developed by
**RAHUL PV**
""")

st.title("📦 Inventory Reorder Alert System")

st.write("Welcome to the Inventory Reorder Alert Dashboard!")

st.info("This application helps identify items that need restocking.")

# Read inventory

uploaded_file = st.sidebar.file_uploader(
    "Upload Inventory CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("inventory.csv")

# Create Status column
df["Status"] = df.apply(
    lambda row: "🔴 Needs Reorder"
    if row["current_quantity"] < row["reorder_threshold"]
    else "🟢 Stock OK",
    axis=1
)

# Dashboard Metrics
total_items = len(df)
need_reorder = len(df[df["current_quantity"] < df["reorder_threshold"]])
stock_ok = total_items - need_reorder

col1, col2, col3 = st.columns(3)

col1.metric("📦 Total Items", total_items)
col2.metric("🔴 Need Reorder", need_reorder)
col3.metric("🟢 Stock OK", stock_ok)

st.divider()

st.subheader("🔍 Filter Inventory")

show_only_reorder = st.checkbox("Show only items that need reordering")

if show_only_reorder:
    filtered_df = df[df["current_quantity"] < df["reorder_threshold"]]
else:
    filtered_df = df

st.subheader("📋 Inventory Data")

st.dataframe(filtered_df, use_container_width=True)

st.subheader("📥 Download Restock Report")

reorder_df = df[df["current_quantity"] < df["reorder_threshold"]]

csv = reorder_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Restock Report",
    data=csv,
    file_name="restock_report.csv",
    mime="text/csv"
)
