import speech_recognition as sr
from gtts import gTTS
import playsound
from transformers import pipeline

def health_assistant():
    print("\n--- Voice-based Health Assistant ---")
    recognizer = sr.Recognizer()
    generator = pipeline("text2text-generation", model="google/flan-t5-base")

    with sr.Microphone() as source:
        print("Ask your health-related question...")
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            print(f"You asked: {query}")
            response = generator(f"What is a basic health suggestion for: {query}")[0]['generated_text']
            print(f"Assistant: {response}")

            tts = gTTS(text=response)
            tts.save("response.mp3")
            playsound.playsound("response.mp3")
        except Exception as e:
            print(f"Could not process audio: {e}")
