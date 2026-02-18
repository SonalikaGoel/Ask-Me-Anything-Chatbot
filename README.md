# Ask Me Anything - AI Voice Assistant

A Python-based voice assistant that listens to your questions and responds with intelligent answers using Google Gemini AI. Features speech recognition, text-to-speech output.

## Features

- **🎤 Voice Recognition**: Listen to voice commands using Google Speech Recognition
- **🤖 AI Responses**: Get intelligent answers using Google Gemini API (completely free)
- **📅 Calendar Integration**: Check your Google Calendar events and schedule
- **📝 Note Taking**: Create and save notes with voice commands
- **🔊 Text-to-Speech**: Hear AI responses with natural voice output
- **💻 Completely Free**: No paid APIs required

## Tech Stack

- **Python 3.13+**
- **Google Gemini API** - AI responses (free tier)
- **Google Calendar API** - Calendar access
- **SpeechRecognition** - Voice input
- **pyttsx3** - Text-to-speech
- **PyAudio** - Microphone access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Ask-me-Anything.git
cd Ask-me-Anything
2. Create a virtual environment:
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate   # macOS/Linux
3. Install dependencies:
pip install -r requirements.txt
4. Get API Credentials:

Google Gemini API: Get free API key from Google AI Studio
Google Calendar API: Set up from Google Cloud Console
5. Add credentials:

Place credentials.json in the project directory (for Calendar API)
Update Ask Me Anything.py line 17 with your Gemini API key

Usage
Run the application:

python "Ask Me Anything.py"
