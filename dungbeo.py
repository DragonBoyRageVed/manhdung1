# app.py
import streamlit as st
import pandas as pd

st.title("Excel Data Viewer")

# Load Excel file
uploaded_file = 'TABLE-T12-2024.xlsx'

try:
    df = pd.read_excel(uploaded_file)
    st.write("### Full Data", df)

    # Optional: Add a filter
    st.write("### Filtered View")
    selected_column = st.selectbox("Select a column to filter by", df.columns)
    filter_value = st.text_input(f"Enter value to filter `{selected_column}`:")

    if filter_value:
        filtered_df = df[df[selected_column].astype(str).str.contains(filter_value, case=False)]
        st.write(filtered_df)
except Exception as e:
    st.error(f"Error loading file: {e}")






 