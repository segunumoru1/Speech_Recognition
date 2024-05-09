import streamlit as st
from new import transcribe_speech
import os

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Add a dropdown menu to select the speech recognition API
    recognition_api = st.selectbox("Select speech recognition API", ['google'])

    # Add a dropdown menu to select the language
    language = st.selectbox("Select language", ['en-US', 'fr-FR', 'es-ES', 'de-DE', 'it-IT'])

    # Add a checkbox to enable pause/resume feature
    pause_resume = st.checkbox("Pause and Resume")

    # Add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(recognition_api, language, pause_resume)
        st.write("Transcription: ", text)

        # Add a button to save the transcribed text to a file
        if st.button("Save to File"):
            user_home = os.path.expanduser("~")
            file_path = os.path.join(user_home, "transcription.txt")
            with open(file_path, "w") as f:
                f.write(text)
            st.success(f"Transcription saved to '{file_path}'.")

if __name__ == "__main__":
    main()
