import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Confirmation of file upload
    df = pd.read_csv(uploaded_file)

    # Data Preview Visualization, first 5 rows
    st.subheader("Data Preview")
    st.write(df.head())

    # Data Summary Visualization
    st.subheader('Data Summary')
    st.write(df.describe())

    # Data Filtering
    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    # Grabbing all of the rows that match the selected value
    filterd_df = df[df[selected_column] == selected_value]
    st.write(filterd_df)

    # Plotting Data
    st.subheader('Plot Data')
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    # Generating a button to generate the plot
    if st.button('Generate Plot'):
        st.line_chart(filterd_df.set_index(x_column)[y_column])

else:
    st.write("Please upload a CSV file to get started.")