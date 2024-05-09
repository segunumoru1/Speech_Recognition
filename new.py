import speech_recognition as sr
import time
import streamlit as st

def transcribe_speech(recognition_api='google', language='en-US', pause_resume=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio_text = r.listen(source)

        if pause_resume:
            st.info("Pausing speech recognition. Press 'Resume' to continue.")
            while True:
                if st.button("Resume"):
                    break
                time.sleep(1)

    try:
        if recognition_api == 'google':
            text = r.recognize_google(audio_text, language=language)
        
        else:
            return "Sorry, I did not understand that."
        return text
    except sr.UnknownValueError:
        return "Sorry, I did not understand the speech. Please try again."
    except sr.RequestError as e:
        return f"Error: {e}. Please check your API credentials or internet connection."
    except Exception as e:
        return f"Unexpected error: {e}. Please try again later."
