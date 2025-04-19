import streamlit as st
import random
from fpdf import FPDF

def generate_story(template, user_inputs):
    return template.format(*user_inputs)

# Define multiple Mad Libs templates
templates = [
    "Ek din, {} ek {} ja raha tha, jab usne achanak {} dekha. Usne {} ki aur sab log {} ho gaye!",
    "{} aur {} ek {} par gaye the. Wahan unko {} mila jo bohot {} tha!"
]

st.set_page_config(page_title="Mad Libs Generator", layout="centered")
st.title("🎭 Advanced Mad Libs Game")

# Select a story template
if "story" not in st.session_state:
    st.session_state["story"] = ""

selected_template = random.choice(templates)
st.subheader("Apni kahani likhne ke liye fields bharen:")

# Get placeholders from template
placeholders = selected_template.count("{}")

# User inputs
user_inputs = []
for i in range(placeholders):
    user_input = st.text_input(f"Word {i+1}:", key=f"input_{i}")
    user_inputs.append(user_input)

# Generate story
if st.button("📜 Generate Story"):
    if all(user_inputs) and len(user_inputs) == placeholders:
        st.session_state["story"] = generate_story(selected_template, user_inputs)
        st.success("Aapki kahani tayar hai!")
        st.write(st.session_state["story"])
    else:
        st.error("Error: Please fill all required words before generating the story!")

# Download as PDF
def save_to_pdf(story):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(190, 10, story)
    pdf_file = "mad_libs_story.pdf"
    pdf.output(pdf_file)
    return pdf_file

if st.button("📥 Download Story as PDF"):
    if st.session_state["story"]:
        pdf_file = save_to_pdf(st.session_state["story"])
        with open(pdf_file, "rb") as file:
            st.download_button(label="Download PDF", data=file, file_name="mad_libs_story.pdf", mime="application/pdf")
    else:
        st.warning("Pehle kahani generate karein!")