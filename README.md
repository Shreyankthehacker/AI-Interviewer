# 🤖 AI Interviewer System

Welcome to the **AI Interviewer** — an intelligent, voice-interactive system designed to conduct and evaluate technical interviews autonomously. It uses a combination of large language models, real-time audio handling, and analysis tools to simulate an immersive interview experience.

---

## 🧠 Overview

The AI Interviewer mimics a professional interview setup, asking progressively complex technical questions and evaluating the candidate's answers based on content, tone, and authenticity.

---

## 🔧 Technologies Used

- **LangGraph** - Manages the flow of the interview in a graph-like state machine.
- **Gemini**- For dynamic question generation, grading, summarization, and cheating detection.
- **gTTS (Google Text-to-Speech)** - Converts AI-generated questions into speech.
- **Whisper** - For converting spoken answers back into text (Speech-to-Text).
- **Python** - Core logic and orchestration.
- **Vosk (alternative STT)** - Optional offline STT engine.

---

## 🔁 Interview Flow

![AI Interviewer](images/ai_interviewer.png)

### 1. `start_message`

Initializes the session, explains the rules or topic.

### 2. `call_model`

Generates and vocalizes the next most relevant interview question using GPT and gTTS.

### 3. `human_answer`

Captures the user's voice response, transcribes it via Whisper, and stores it.

### 4. `summarizer`

Updates a contextual summary of the interview using the conversation history.

### 5. `grading`

Scores the response (1-10) based on relevance, clarity, and depth.

### 6. `cheatingcheck`

Estimates whether the answer might be AI-generated based on phrasing.

### 7. `ending`

Presents a final summary and closes the interview.

---

## 💡 Features Explained

### 🎤 Voice Interaction

- Real-time TTS (via `gTTS`) to speak questions.
- STT via Whisper to transcribe spoken answers.

### 🧠 Contextual Questions

- Each new question is generated considering all previous Q&As.
- LLM ensures questions become more specific or challenging.

### 📝 Intelligent Grading

- Custom prompts enable fair scoring of answers.
- Focuses on reasoning, structure, examples, and relevance.

### 🚨 Cheating Detection

- Detects potential AI-generated answers.
- In the future: will include **camera-based** cheating detection using computer vision.

### 📋 Interview Summary

- Generates a running summary after each round.
- Useful for feedback or review.

---

## 🛠️ Implementation Guide

1. **Clone the repo** and set up the virtual environment:

   ```bash
   git clone your-repo-url
   cd ai-interviewer
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Download Whisper models** and place them in the correct path.

3. **Run the system**:

   ```bash
   python interview_main.py
   ```

4. **Audio Files**:

   - Ensure questions are saved as `.mp3` or `.wav`
   - Answers are recorded and passed to Whisper or Vosk

---

## 🚀 Future Developments

### 🧑‍💻 Web Interface

- Build frontends using **Flask** and **Streamlit**
- Deploy via **Docker** or **AWS EC2 / Lambda** for scalable usage

### 📷 Camera-Based Cheating Detection

- Use **OpenCV** and pose estimation to track eye movement or devices
- Integrate with real-time webcam feed analysis

### 🗃️ Answer Analytics

- Store each candidate's answers for analysis
- Use NLP techniques to highlight weak areas

### 🛡️ Secure Authentication

- Role-based access and timed interview sessions
- Logging and audit trails

---

## 🧪 Final Thoughts

This AI Interviewer is more than a bot — it's a foundation for scalable, fair, and intelligent hiring. With powerful future upgrades like camera cheating checks and a rich web interface, it will soon redefine how interviews are conducted.

> Feel free to fork and customize for your domain (e.g., Data Science, DevOps, System Design, etc.)

---

## 📄 License

MIT License © Shreyank

---

Stay tuned! 🚀

