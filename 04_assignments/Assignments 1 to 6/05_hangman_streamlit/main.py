import random
import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e2e;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
        }
        .word-display {
            font-size: 28px;
            text-align: center;
            letter-spacing: 5px;
        }
        .attempts {
            font-size: 20px;
            color: #ff5555;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# List of words
WORDS = ['python', 'streamlit', 'developer', 'hangman', 'challenge', 'code', 'project']

def get_new_word():
    return random.choice(WORDS).lower()

# Session state to store game data
if 'word' not in st.session_state:
    st.session_state.word = get_new_word()
    st.session_state.guesses = []
    st.session_state.attempts = 6
    st.session_state.game_over = False

def display_word():
    return ' '.join([letter if letter in st.session_state.guesses else '_' for letter in st.session_state.word])

st.markdown('<p class="title"> 🎮 Hangman Game</p>', unsafe_allow_html=True)

st.markdown(f'<p class="word-display">{display_word()}</p>', unsafe_allow_html=True)

if st.session_state.game_over:
    if '_' not in display_word():
        st.success("Congratulations! You guessed the word! 🎉")
    else:
        st.error(f"Game Over! The word was: {st.session_state.word}")
    if st.button("Play Again"):
        st.session_state.word = get_new_word()
        st.session_state.guesses = []
        st.session_state.attempts = 6
        st.session_state.game_over = False
    st.stop()

guess = st.text_input("Enter a letter:", max_chars=1).lower()
if st.button("Submit Guess"):
    if guess and guess.isalpha():
        if guess in st.session_state.guesses:
            st.warning("You've already guessed this letter!")
        else:
            st.session_state.guesses.append(guess)
            if guess not in st.session_state.word:
                st.session_state.attempts -= 1
    
    if st.session_state.attempts == 0 or '_' not in display_word():
        st.session_state.game_over = True
    
st.markdown(f'<p class="attempts">Attempts left: {st.session_state.attempts}</p>', unsafe_allow_html=True)
