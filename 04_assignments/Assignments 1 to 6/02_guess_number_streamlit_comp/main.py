import streamlit as st
import random

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
        }
        .stTextInput, .stButton, .stNumberInput {
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Game Initialization
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.title("🎯 Guess the Number Game")
st.write("I have picked a number between **1 and 100**. Can you guess it?")

# User Input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.random_number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.random_number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True

# Restart Game
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False