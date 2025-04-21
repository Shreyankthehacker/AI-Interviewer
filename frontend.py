import streamlit as st
import pyaudio
import wave
import requests
from io import BytesIO
from streamlit_lottie import st_lottie
import json

# Load the Lottie animation (optional)
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to play audio using Streamlit
def play_audio(audio_path):
    st.audio(audio_path, format="audio/mp3")

# Function to record audio when speech is detected
def record_audio(output_path):
    # Initialize audio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)
    frames = []
    print("Recording...")

    # Record audio for speech input (until silence is detected)
    while True:
        data = stream.read(1024)
        frames.append(data)

        # You can implement speech detection logic here.
        # For now, we are assuming to record for a fixed time.
        if len(frames) > 1000:  # Adjust the threshold as needed
            break

    print("Recording stopped.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save recorded audio to file
    with wave.open(output_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)
        wf.writeframes(b''.join(frames))
    print(f"Audio saved to {output_path}")

# API to send audio and receive question
def get_question_from_backend():
    # Simulate API call to backend for question
    # Replace with actual API call code
    response = requests.get("YOUR_BACKEND_API_URL/question")  
    question_data = response.json()
    question_text = question_data["text"]
    question_audio_url = question_data["audio_url"]
    
    # Download the question audio
    audio_response = requests.get(question_audio_url)
    audio_data = audio_response.content

    return question_text, audio_data

# Streamlit page 1: Begin Interview
def begin_interview_page():
    st.title("AI Interview")
    st.header("Welcome to the AI Interview!")
    
    # Load and display animation (optional)
    lottie_url = "https://assets6.lottiefiles.com/packages/lf20_kjxcnfdc.json"  # Replace with your desired Lottie URL
    lottie_data = load_lottie_url(lottie_url)
    if lottie_data:
        st_lottie(lottie_data, speed=1, width=700, height=700, key="begin")

    if st.button("Begin the Interview"):
        st.session_state.page = "interview"
        st.experimental_rerun()

# Streamlit page 2: Interview Processing
def interview_page():
    st.title("AI Interview - Interview in Progress")
    
    # Load and display animation (optional)
    lottie_url = "https://assets6.lottiefiles.com/packages/lf20_kjxcnfdc.json"  # Replace with your desired Lottie URL
    lottie_data = load_lottie_url(lottie_url)
    if lottie_data:
        st_lottie(lottie_data, speed=1, width=700, height=700, key="interview")

    # Get question from backend
    question_text, question_audio_data = get_question_from_backend()

    # Play the question audio
    play_audio(BytesIO(question_audio_data))

    # Display the text version of the question with animation
    st.write("### Question: ")
    st.write(f"{question_text}")

    # Button for answering
    if st.button("Start Answering"):
        answer_path = "answer.mp3"
        record_audio(answer_path)

        # Send the recorded answer to the backend
        with open(answer_path, "rb") as answer_file:
            files = {"file": answer_file}
            response = requests.post("YOUR_BACKEND_API_URL/answer", files=files)

        if response.status_code == 200:
            st.write("Your answer has been submitted!")
        else:
            st.write("Failed to submit answer.")

# Streamlit app logic
def main():
    # Custom CSS to set the background to white
    st.markdown("""
        <style>
        body {
            background-color: white;
            color: black;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .stText {
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

    if 'page' not in st.session_state:
        st.session_state.page = "begin"

    if st.session_state.page == "begin":
        begin_interview_page()
    elif st.session_state.page == "interview":
        interview_page()

if __name__ == "__main__":
    main()
