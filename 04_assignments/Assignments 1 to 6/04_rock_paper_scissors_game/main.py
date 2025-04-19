import streamlit as st
import random

# Custom CSS styling
st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stButton > button {
        background-color: #ff9800;
        color: white;
        font-size: 18px;
        border-radius: 10px;
    }
    .stButton > button:hover {
        background-color: #e65100;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎮 Rock, Paper, Scissors Game")
st.subheader("Challenge the AI!")

# Choices
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
ai_score = 0

# Game logic
def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and ai_choice == "Scissors") or \
         (user_choice == "Scissors" and ai_choice == "Paper") or \
         (user_choice == "Paper" and ai_choice == "Rock"):
        return "You win!"
    else:
        return "AI wins!"

# Random selection feature
def random_choice():
    return random.choice(choices)

# Game UI
user_choice = st.radio("Choose your move:", choices + ["Random"], horizontal=True)

if user_choice == "Random":
    user_choice = random_choice()
    st.write(f"**Randomly selected:** {user_choice}")

if st.button("Play"):  
    ai_choice = random.choice(choices)
    result = determine_winner(user_choice, ai_choice)
    
    if "You win" in result:
        st.session_state.user_score = st.session_state.get("user_score", 0) + 1
    elif "AI wins" in result:
        st.session_state.ai_score = st.session_state.get("ai_score", 0) + 1
    
    st.write(f"**Your Choice:** {user_choice}")
    st.write(f"**AI's Choice:** {ai_choice}")
    st.success(result)
    
    st.write(f"**Score:** You {st.session_state.get('user_score', 0)} - {st.session_state.get('ai_score', 0)} AI")
    
if st.button("Reset Score"):
    st.session_state.user_score = 0
    st.session_state.ai_score = 0
    st.rerun()
