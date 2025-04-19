import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type."
    
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
def main():
    st.set_page_config(page_title="Advanced Password Generator", page_icon="🔑", layout="centered")
    st.title("🔐 Advanced Password Generator")
    st.markdown("Generate strong and secure passwords with customization.")
    

    # User Input
    length = st.slider("Select password length", min_value=6, max_value=32, value=12)
    use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
    use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
    use_numbers = st.checkbox("Include Numbers", value=True)
    use_specials = st.checkbox("Include Special Characters", value=True)
    
    if st.button("Generate Password"):
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials)
        st.success(f"Generated Password: `{password}`")
        
        # Copy to clipboard feature
        st.code(password, language='plaintext')

if __name__ == "__main__":
    main()
