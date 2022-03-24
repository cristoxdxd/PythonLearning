from googletrans import Translator
import pyttsx3

translator = Translator()
engine = pyttsx3.init()
engine.setProperty('rate', 145)
engine.setProperty('voice', '0x7f259f5f3760')

try:
    with open('Libros/evangelio_segun_marcos.txt', mode='r') as myFile:
        # Translate the text
        text = myFile.read()
        translatedText = translator.translate(text=text).text
        # Write the translation
        txtOutput = open('Books/Gospel_According_to_Mark.txt','w')
        txtOutput.write(translatedText)
        # Read the audiobook
        #engine.say('Gospel According to Mark')
        engine.save_to_file(translatedText,'Gospel_According_to_Mark.wav')
        engine.runAndWait()
except FileNotFoundError as error:
    print('Error:', error)
