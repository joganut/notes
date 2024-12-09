import streamlit as st
import os
import json

# Title of the app
st.title('Notes App')

# Path for storing notes in JSON format
notes_file = 'notes.json'

# Function to load notes from the file
def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, 'r') as file:
            return json.load(file)
    return {}

# Function to save notes to the file
def save_notes(notes):
    with open(notes_file, 'w') as file:
        json.dump(notes, file, indent=4)

# Load existing notes
notes = load_notes()

# Display existing notes
st.subheader('Saved Notes:')
for name, note in list(notes.items()):  # Convert to list to avoid modification during iteration
    # Expandable section for each note
    with st.expander(f"View/Edit/Delete {name}"):
        st.write(f"**{name}:**")
        st.write(note)
        
        # Update button for each note
        updated_note = st.text_area(f'Update note for {name}', value=note, height=100)
        if st.button(f'Save updated note for {name}'):
            notes[name] = updated_note
            save_notes(notes)
            st.success(f'Note for {name} updated!')
        
        # Delete button for each note
        if st.button(f'Delete {name}'):
            del notes[name]
            save_notes(notes)
            st.success(f'Note for {name} deleted!')

# Add a new note
st.subheader('Add a New Note:')
note_name = st.text_input('Enter the name for the note:')
note_content = st.text_area('Enter your note:')

if st.button('Save New Note'):
    if note_name and note_content:
        notes[note_name] = note_content
        save_notes(notes)
        st.success(f'Note for {note_name} saved!')
    else:
        st.error('Please provide both a name and a note.')
