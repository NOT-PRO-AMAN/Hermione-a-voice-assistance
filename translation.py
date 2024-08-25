from googletrans import Translator
import pyttsx3

ttsx = pyttsx3.init()

translator = Translator()

def speak(text):                         
    ttsx.setProperty('rate', 130)     
    voices = ttsx.getProperty('voices')
    ttsx.setProperty('voice', voices[1].id)
    ttsx.say(text)
    ttsx.runAndWait()
import pyttsx3



def translate_to_hindi_transliterate(text):
    translation = translator.translate(text, src='en', dest='hi')
    return translation.pronunciation

def speak_print(eng_text):
    a = translate_to_hindi_transliterate(eng_text)
    print(f"your hindi translation is----{a}")
    speak("your translation is ready")







