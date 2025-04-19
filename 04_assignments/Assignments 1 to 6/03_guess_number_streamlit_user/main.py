import streamlit as st
import random

# Custom CSS styling
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e2e;
            color: white;
        }
        .stButton>button {
            background-color: #ff7b00;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
        }
        .stTextInput>div>div>input {
            font-size: 18px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Game Logic
st.title("🎯 Guess the Number Game (user)")

# Difficulty selection
difficulty = st.radio("Select Difficulty:", ["Easy", "Medium", "Hard"])

# Set range based on difficulty
if difficulty == "Easy":
    number_range = 10
elif difficulty == "Medium":
    number_range = 50
else:
    number_range = 100

st.write(f"I'm thinking of a number between 1 and {number_range}.")

# Session state for storing the random number and attempts
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, number_range)
    st.session_state.attempts = 0

# User input
guess = st.text_input("Enter your guess:", key="guess")

if st.button("Submit Guess"):
    if guess.isdigit():
        guess = int(guess)
        st.session_state.attempts += 1
        
        if guess < st.session_state.target_number:
            st.warning("🔼 Too low! Try again.")
        elif guess > st.session_state.target_number:
            st.warning("🔽 Too high! Try again.")
        else:
            st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
            st.balloons()
            # Reset game
            st.session_state.target_number = random.randint(1, number_range)
            st.session_state.attempts = 0
    else:
        st.error("⚠️ Please enter a valid number.")
