import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', '0x7f70e5836610')

text = 'Hola'
engine.say(text)
engine.runAndWait