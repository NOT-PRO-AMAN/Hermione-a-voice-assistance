import speech_recognition as sr
import webbrowser
import pyttsx3
import playlist
import translation

ttsx = pyttsx3.init()
r = sr.Recognizer()


def speak(text):                         
    ttsx.setProperty('rate', 130)     
    voices = ttsx.getProperty('voices')
    ttsx.setProperty('voice', voices[1].id)
    ttsx.say(text)
    ttsx.runAndWait()


def kaam(k):
    if "google" in k.lower():
        webbrowser.open("https://www.google.com")
        speak("opening google")
    elif "youtube" in k.lower():
        webbrowser.open("https://www.youtube.com")
        speak("opening youtube")
    elif "chat gpt" in k.lower():
        webbrowser.open("https://chatgpt.com/")
        speak("opening chat GPT")
    elif "instagram" in k.lower():
        webbrowser.open("https://www.instagram.com")
        speak("opening inestagram")
    elif "discord" in k.lower():
        webbrowser.open("https://www.discord.com")
        speak("opening discord")
    elif "gmail" in k.lower():
        webbrowser.open("https://www.gmail.com")
        speak("opening G mail")
    elif "spotify" in k.lower():
        webbrowser.open("https://open.spotify.com/")
        speak("opening spotify")
    elif "play" in k.lower():
        playlist.play_song(k)   
    elif "translate" in k.lower():
        speak("say the english sentence you want to translate")
        with sr.Microphone() as source:
            print("listening for translation 🎙️ 🎙️ 🎙️")
            audio = r.listen(source)
            engtext = r.recognize_google(audio)
            translation.speak_print(engtext)





if __name__ == "__main__":
    
    while True:
        
        
        
            
            

            try:

                with sr.Microphone() as source:
                    print("listening  🎙️ 🎙️ 🎙️")
                    audio = r.listen(source,  timeout=2,phrase_time_limit=3)  
                    print("Processing ⌛⌛⌛")
                text = r.recognize_google(audio)
                print(text)
                if "hermione" in text.lower():
                     print("Hermione is here to help!")
                     speak("hey Amon")
                     print("listening  🎙️ 🎙️ 🎙️")
                     with sr.Microphone() as source:

                        audio = r.listen(source,  timeout=6,phrase_time_limit=3)
                        command = r.recognize_google(audio)
                        kaam(command)
           

            except Exception as e:
                print("Try again ↻")


