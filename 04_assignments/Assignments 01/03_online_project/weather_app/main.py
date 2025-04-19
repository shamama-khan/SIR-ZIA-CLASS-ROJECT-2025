import streamlit as st
import uvicorn
import random
import matplotlib.pyplot as plt

# Function to simulate weather data visualization
def plot_weather_data(temperature, humidity, condition):
    conditions = {
        "Sunny": "yellow",
        "Rainy": "blue",
        "Cloudy": "gray",
        "Windy": "green",
    }

    # Simulate a basic weather condition chart
    fig, ax = plt.subplots(figsize=(5, 3))

    # Plot data
    ax.bar(["Temperature", "Humidity"], [temperature, humidity], color=[conditions.get(condition, "gray")] * 2)

    ax.set_title(f"Weather Report: {condition}")
    ax.set_ylabel("Value")
    ax.set_ylim(0, 100)
    ax.set_xticks(["Temperature", "Humidity"])

    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title("Weather Program with Streamlit and UV")

    # Get weather data input from the user
    st.subheader("Enter Weather Information")
    temperature = st.slider("Temperature (°C)", -30, 50, random.randint(15, 30))  # Default temp range: -30 to 50
    humidity = st.slider("Humidity (%)", 0, 100, random.randint(30, 80))  # Default humidity range: 0-100
    condition = st.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy", "Windy"])

    # Show the input data
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Humidity: {humidity}%")
    st.write(f"Condition: {condition}")

    # Visualize the weather data
    plot_weather_data(temperature, humidity, condition)

# Run the app
if __name__ == "__main__":
    main()

