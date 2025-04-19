import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Simple Data Dashboard")

# File uploader
uploaded_file = st.file_uploader("📂 Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.write(df.head())

    st.subheader("📊 Data Summary")
    st.write(df.describe())

    # Filter Data
    st.subheader("🎯 Filter Data")
    columns = df.columns.tolist()

    if columns:
        selected_column = st.selectbox("Select column to filter by", columns)
        
        if selected_column:
            unique_values = df[selected_column].dropna().unique()
            selected_value = st.selectbox("Select value", unique_values)

            filtered_df = df[df[selected_column] == selected_value]
            st.write(filtered_df)

            # Plot Data
            st.subheader("📈 Plot Data")

            x_column = st.selectbox("Select x-axis column", columns)
            y_column = st.selectbox("Select y-axis column", columns)

            if st.button("📌 Generate Plot"):
                if x_column in filtered_df.columns and y_column in filtered_df.columns:
                    try:
                        # Ensure the y_column is numeric
                        filtered_df[y_column] = pd.to_numeric(filtered_df[y_column], errors="coerce")
                        filtered_df = filtered_df.dropna(subset=[y_column])

                        # Plot using Streamlit's line_chart
                        st.line_chart(filtered_df.set_index(x_column)[y_column])
                    except Exception as e:
                        st.error(f"⚠️ Error generating plot: {e}")
                else:
                    st.error("⚠️ Please select valid columns for plotting.")
    else:
        st.error("⚠️ No columns available in the uploaded file.")
else:
    st.info("📌 Please upload a CSV file to proceed.")
