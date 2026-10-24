# File: /streamlit-app/streamlit-app/app.py
import streamlit as st
import pandas as pd

# Title of the app
st.title("CSV File Uploader")

# File uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Check if the DataFrame is empty
    if df.empty:
        st.error("The uploaded file is empty.")
    else:
        # Display the first 10 rows
        st.subheader("First 10 Rows")
        st.write(df.head(10))

        # Display basic statistics
        st.subheader("Basic Statistics")
        st.write(df.describe())

        # Select a numeric column for plotting
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
        
        if not numeric_columns:
            st.error("No numeric columns found in the uploaded file.")
        else:
            selected_column = st.selectbox("Select a numeric column for line chart", numeric_columns)
            st.line_chart(df[selected_column])
else:
    st.info("Please upload a CSV file to get started.")