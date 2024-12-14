import streamlit as st
from pydub import AudioSegment
from io import BytesIO
import os

# Title of the app
st.title("Minimal Audio Converter")

# Description
st.write("Upload an audio file and convert it to **WAV** or **MP3** format.")

# Supported audio formats
SUPPORTED_FORMATS = ["mp3", "wav", "ogg", "flac", "aac", "m4a"]

def convert_audio(uploaded_file, target_format):
    """
    Converts the uploaded audio file to the target format.
    """
    try:
        # Read the file content
        audio_bytes = uploaded_file.read()
        
        # Load the audio file using pydub
        original_audio = AudioSegment.from_file(BytesIO(audio_bytes), format=uploaded_file.name.split(".")[-1])
        
        # Output buffer
        output_buffer = BytesIO()
        
        # Export audio to desired format
        original_audio.export(output_buffer, format=target_format)
        output_buffer.seek(0)
        
        return output_buffer
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# File uploader
uploaded_file = st.file_uploader("Choose an audio file", type=SUPPORTED_FORMATS)

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio", start_time=0)
    
    # Buttons for conversion
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Convert to WAV"):
            converted_file = convert_audio(uploaded_file, "wav")
            if converted_file:
                st.download_button(
                    label="Download WAV",
                    data=converted_file,
                    file_name=os.path.splitext(uploaded_file.name)[0] + ".wav",
                    mime="audio/wav"
                )
    
    with col2:
        if st.button("Convert to MP3"):
            converted_file = convert_audio(uploaded_file, "mp3")
            if converted_file:
                st.download_button(
                    label="Download MP3",
                    data=converted_file,
                    file_name=os.path.splitext(uploaded_file.name)[0] + ".mp3",
                    mime="audio/mpeg"
                )
