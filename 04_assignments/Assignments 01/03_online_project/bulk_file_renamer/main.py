import streamlit as st
import os
from zipfile import ZipFile
import tempfile
import shutil

st.set_page_config(page_title="Bulk File Renamer", page_icon="📝", layout="centered")

st.title("📝 Bulk File Renamer")
st.markdown("Rename multiple files easily with a custom base name and numbering.")

# Upload multiple files
uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)

# User input for base name and file extension
base_name = st.text_input("Enter base file name", "renamed_file")
start_number = st.number_input("Start numbering from", min_value=1, step=1, value=1)
add_numbering = st.checkbox("Add numbering to file names", value=True)

# Rename files logic
if uploaded_files and st.button("Rename Files"):
    with tempfile.TemporaryDirectory() as tmpdir:
        renamed_files = []
        for i, uploaded_file in enumerate(uploaded_files, start=start_number):
            # Get file extension
            file_ext = os.path.splitext(uploaded_file.name)[1]
            # Build new name
            if add_numbering:
                new_name = f"{base_name}_{i}{file_ext}"
            else:
                new_name = f"{base_name}{file_ext}"
            # Save file to temp directory with new name
            file_path = os.path.join(tmpdir, new_name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())
            renamed_files.append(file_path)

        # Create a ZIP file of renamed files
        zip_path = os.path.join(tmpdir, "renamed_files.zip")
        with ZipFile(zip_path, "w") as zipf:
            for file in renamed_files:
                zipf.write(file, os.path.basename(file))

        # Provide download button
        with open(zip_path, "rb") as zipf:
            st.success("Files renamed successfully!")
            st.download_button("📦 Download Renamed Files", zipf, file_name="renamed_files.zip")
