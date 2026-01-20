import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 180)

engine.setProperty('volume', 0.1)

def dubbing(text_for_dubbing: str):
    if not text_for_dubbing:
        print("Error: No text provided for dubbing")
        return
    
    try:
        engine.say(text_for_dubbing)
        engine.runAndWait()
    except Exception as e:
            # Если что-то пойдет не так со звуком, программа не вылетит
        print(f"CRITICAL ERROR in Voice Module: {e}")

