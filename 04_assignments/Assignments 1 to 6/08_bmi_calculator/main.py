import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_bmi(weight, height):
    
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Streamlit UI customization
st.set_page_config(page_title="BMI Calculator", page_icon="⚖", layout="centered")
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .main-container {
            background: rgba(255, 255, 255, 0.15);
            padding: 25px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            text-align: center;
            max-width: 500px;
            margin: auto;
        }
        h1 {
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        .result {
            font-size: 22px;
            font-weight: bold;
            color: #ffffff;
            background-color: rgba(0, 0, 0, 0.4);
            padding: 10px;
            border-radius: 10px;
            margin-top: 15px;
            display: inline-block;
        }
        .stButton>button {
            background-color: #00b8db;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.title("⚖ Fancy BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and check your health category.")

# User input
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1, format="%.1f")
with col2:
    height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01, format="%.2f")

if st.button("Calculate BMI"):
    if weight and height:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        st.markdown(f"<div class='result'>Your BMI: {bmi:.2f} ({category})</div>", unsafe_allow_html=True)

        # Create a data frame for visualization
        df = pd.DataFrame({
            "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
            "BMI Range": [18.4, 24.9, 29.9, 35]
        })
        df["Current BMI"] = [bmi if category == x else None for x in df["Category"]]
        
        # Plotting
        fig = px.bar(df, x="Category", y="BMI Range", text="BMI Range",
                     color="Category", height=400, title="BMI Categories",
                     color_discrete_map={"Underweight": "blue", "Normal weight": "green", "Overweight": "orange", "Obese": "red"})
        st.plotly_chart(fig)
    else:
        st.error("Please enter valid weight and height values.")

st.markdown("</div>", unsafe_allow_html=True)
st.write("Developed by Sadiq Khan")