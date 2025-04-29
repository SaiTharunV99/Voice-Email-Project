import speech_recognition as sr
import smtplib
import pyttsx3

# Text-to-Speech engine initialization
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            said = r.recognize_google(audio)
            print(f"You said: {said}")
            return said
        except Exception as e:
            print("Could not understand, please try again.")
            return None

def send_email(to_email, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Use your Gmail ID and App Password here
        server.login('your_email@gmail.com', 'your_app_password')

        email_message = f'Subject: {subject}\n\n{message}'
        server.sendmail('your_email@gmail.com', to_email, email_message)
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    speak("Welcome to voice-based email system.")
    speak("Whom do you want to send email to?")
    to_email = get_audio()
    if to_email:
        to_email = to_email.replace(' ', '') + "@gmail.com"

    speak("What is the subject of your email?")
    subject = get_audio()

    speak("What is your message?")
    message = get_audio()

    success = send_email(to_email, subject, message)

    if success:
        speak("Email sent successfully!")
    else:
        speak("Failed to send email.")

if __name__ == "__main__":
    main()
