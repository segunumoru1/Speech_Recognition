# Speech Recognition Application

This is a Streamlit-based application that allows users to transcribe speech using various speech recognition APIs, including Google Speech Recognition, Wit.ai, Bing Speech, Houndify, and IBM Speech to Text.

## Features

1. **Speech Transcription**: The application provides a button to start recording audio from the user's microphone. The recorded audio is then transcribed using the selected speech recognition API, and the transcription is displayed in the application.

2. **API Selection**: Users can select the speech recognition API they want to use from a dropdown menu. The available options are Google Speech Recognition, Wit.ai, Bing Speech, Houndify, and IBM Speech to Text.

3. **Language Selection**: Users can select the language they are speaking from a dropdown menu. The supported languages are English (US), French (France), Spanish (Spain), German (Germany), and Italian (Italy).

4. **Pause and Resume**: Users can pause the speech recognition process and resume it later using a checkbox in the application.

5. **Save Transcription to File**: Users can save the transcribed text to a file named `transcription.txt` in their home directory.

## Installation

To run this application, you'll need to have the following dependencies installed:

- Python 3.7 or later
- Streamlit
- SpeechRecognition
- PyAudio

You can install these dependencies using pip:

```
pip install streamlit SpeechRecognition PyAudio
```

## Usage

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/speech-recognition-app.git
   ```

2. Navigate to the project directory:

   ```
   cd speech-recognition-app
   ```

3. Run the Streamlit application:

   ```
   streamlit run app.py
   ```

   This will launch the application in your default web browser.

4. In the application, select the speech recognition API, language, and whether you want to pause and resume the process.

5. Click the "Start Recording" button to begin transcribing your speech.

6. Once the transcription is complete, you can click the "Save to File" button to save the text to a file named `transcription.txt` in your home directory.

## Configuration

To use the non-Google speech recognition APIs (Wit.ai, Bing Speech, Houndify, and IBM Speech to Text), you'll need to provide your own API credentials in the `transcribe_speech()` function in the `speech_recognition.py` file.

Replace the placeholders with your actual API credentials:

```python
def transcribe_speech(recognition_api='google', language='en-US', pause_resume=False):
    # ...
    if recognition_api == 'wit':
        text = r.recognize_wit(audio_text, key="YOUR_WIT_AI_API_KEY")
    elif recognition_api == 'bing':
        text = r.recognize_bing(audio_text, key="YOUR_BING_SPEECH_API_KEY")
    elif recognition_api == 'houndify':
        text = r.recognize_houndify(audio_text, client_id="YOUR_HOUNDIFY_CLIENT_ID", client_key="YOUR_HOUNDIFY_CLIENT_KEY")
    elif recognition_api == 'ibm':
        text = r.recognize_ibm(audio_text, username="YOUR_IBM_SPEECH_TO_TEXT_USERNAME", password="YOUR_IBM_SPEECH_TO_TEXT_PASSWORD")
    # ...
```

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/your-username/speech-recognition-app).

## License

This project is licensed under the [MIT License](LICENSE).
```
