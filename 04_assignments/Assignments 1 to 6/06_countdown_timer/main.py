import time
import streamlit as st
from datetime import datetime, timedelta
import asyncio

# Custom Styling
st.markdown(
    """
    <style>
        .timer-container {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
            background: linear-gradient(90deg, #ff8a00, #da1b60);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }
        .stButton>button {
            background-color: #ff8a00;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #da1b60;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App
st.title("⏳ Advanced Countdown Timer")
st.write("Set the timer and start counting down!")

# Input for time selection (minutes and seconds)
col1, col2 = st.columns(2)
with col1:
    minutes = st.number_input("Minutes", min_value=0, max_value=60, value=1, step=1)
with col2:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0, step=1)

total_seconds = minutes * 60 + seconds

# Timer State
if 'running' not in st.session_state:
    st.session_state.running = False
if 'stop' not in st.session_state:
    st.session_state.stop = False
if 'pause' not in st.session_state:
    st.session_state.pause = False
if 'remaining_seconds' not in st.session_state:
    st.session_state.remaining_seconds = total_seconds

col1, col2, col3, col4 = st.columns(4)

if col1.button("Start/Resume Timer"):
    st.session_state.running = True
    st.session_state.stop = False
    st.session_state.pause = False
    if st.session_state.remaining_seconds == total_seconds:
        st.session_state.remaining_seconds = total_seconds  # Reset only if starting fresh

if col2.button("Pause Timer"):
    st.session_state.running = False
    st.session_state.pause = True

if col3.button("Stop Timer"):
    st.session_state.running = False
    st.session_state.stop = True
    st.session_state.remaining_seconds = total_seconds

if col4.button("Reset Timer"):
    st.session_state.running = False
    st.session_state.stop = False
    st.session_state.pause = False
    st.session_state.remaining_seconds = total_seconds

if st.session_state.running:
    end_time = datetime.now() + timedelta(seconds=st.session_state.remaining_seconds)
    countdown_placeholder = st.empty()

    while st.session_state.remaining_seconds and not st.session_state.stop:
        if st.session_state.pause:
            break
        
        remaining_time = end_time - datetime.now()
        st.session_state.remaining_seconds = int(remaining_time.total_seconds())
        
        if st.session_state.remaining_seconds <= 0:
            countdown_placeholder.markdown("""
                <div class='timer-container'>
                    Time's up! ⏰
                </div>
            """, unsafe_allow_html=True)
            st.session_state.running = False
            break
        
        minutes, seconds = divmod(st.session_state.remaining_seconds, 60)
        countdown_placeholder.markdown(f"""
            <div class='timer-container'>
                {minutes:02d}:{seconds:02d}
            </div>
        """, unsafe_allow_html=True)
        
        time.sleep(1)

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: grey;'>Made with ❤️ using Streamlit</p>
""", unsafe_allow_html=True)
