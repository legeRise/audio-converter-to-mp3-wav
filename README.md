# Minimal Audio Converter

This is a minimal Streamlit application that allows you to upload an audio file and convert it to one of the following formats:
- MP3
- WAV

## File Structure

The project consists of the following main files:

1. **`converter.py`**: The Streamlit app that performs the audio conversion.
2. **`requirements.txt`**: A list of Python dependencies required for the app.
3. **`packages.txt`**: A special file that tells Streamlit Cloud to install `ffmpeg`, which is required for the audio conversion.

## Features
- Upload an audio file in various formats (MP3, WAV, OGG, FLAC, AAC, M4A).
- Convert the file to either MP3 or WAV format.
- Download the converted file.

## Installation

To run this app locally, follow the steps below:

### 1. Clone the repository or download the files.

### 2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
