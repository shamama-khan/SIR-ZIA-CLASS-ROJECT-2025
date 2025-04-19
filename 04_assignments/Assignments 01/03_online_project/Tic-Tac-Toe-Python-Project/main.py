import streamlit as st

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# Title
st.title("🎮 Tic-Tac-Toe Game (Streamlit)")

# Function to check for a win or draw
def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for i, j, k in win_conditions:
        if board[i] == board[j] == board[k] and board[i] != "":
            return board[i]
    if "" not in board:
        return "Draw"
    return None

# Function to handle a move
def make_move(index):
    if st.session_state.board[index] == "" and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.current_player
        st.session_state.winner = check_winner(st.session_state.board)
        if st.session_state.winner is None:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# UI: Display the board
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = 3 * i + j
        with cols[j]:
            if st.button(st.session_state.board[idx] or " ", key=idx, help=f"Cell {idx+1}"):
                make_move(idx)

# Result message
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a Draw! 🤝")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")

# Reset button
if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
