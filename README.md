# Voice-Based Email for the Blind

## Description:
A simple Python application that allows users (especially visually impaired people) to send emails using voice commands.

## Requirements:
- Python 3.6+
- Install the following libraries:

pip install SpeechRecognition pip install pyttsx3 pip install pyaudio


- Also enable "less secure apps" or use an "App Password" for your Gmail account.

## How to Run:
1. Replace 'your_email@gmail.com' and 'your_app_password' with your actual Gmail credentials inside `voice_email.py`.
2. Run the script:

python voice_email.py


3. Follow voice instructions:
- Say the email ID (only the username part)
- Say the subject
- Say the message
4. Email will be sent!

## Notes:
- Microphone must be connected.
- Needs active Internet connection.