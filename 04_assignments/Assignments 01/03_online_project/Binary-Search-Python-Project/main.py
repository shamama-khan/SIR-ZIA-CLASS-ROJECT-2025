import streamlit as st

def binary_search(arr, target):
    steps = []
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        steps.append((left, mid, right))  # Keep track of steps

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps


# Streamlit UI
st.set_page_config(page_title="Binary Search Visualizer", layout="centered")

st.title("🔍 Binary Search Visualizer")
st.markdown("Enter a sorted list and a target number to visualize binary search.")

# Input list
user_input = st.text_input("Enter sorted numbers (comma-separated):", "1, 3, 5, 7, 9, 11, 13, 15")
target = st.number_input("Enter the target number to search:", step=1, format="%d")

# Convert input string to list of integers
try:
    arr = list(map(int, user_input.split(',')))
    arr.sort()  # Ensure it's sorted
except:
    st.error("Please enter a valid list of comma-separated integers.")
    st.stop()

if st.button("🔎 Start Binary Search"):
    index, steps = binary_search(arr, target)

    st.subheader("🔁 Steps:")
    for step_num, (left, mid, right) in enumerate(steps, 1):
        st.write(f"**Step {step_num}:** Left = {left}, Mid = {mid}, Right = {right} → Value at Mid = {arr[mid]}")

    st.subheader("📍 Result:")
    if index != -1:
        st.success(f"Target {target} found at index {index} in the list.")
    else:
        st.warning(f"Target {target} not found in the list.")
