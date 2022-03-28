#Translation
from deep_translator import GoogleTranslator
#Text to speech
from gtts import gTTS
#Playing sound files
import playsound

def translator():
    global translated
    
    #input text
    to_translate = input("Enter the text to be translated: ")
    #translate text
    translated = GoogleTranslator(source='auto', target='fr').translate(to_translate)
    #output text
    print(translated)
    userInput()
    
def userInput():
    #Speak yes or no?
    runSpeak = input("Speak text? (y/n):")

    #lower() converts the input to lowercase
    if runSpeak.lower() == 'y':
        print('Speaking...')
        speak()
    elif runSpeak.lower() == 'n':
        print('No speach, program exited.')
    else:
        print('Invalid input, try again.\n')
        userInput()

def speak():
    global translated
    
    #create the audio file
    speakText = gTTS(text=translated, slow=False)
    
    #save the audio file
    speakText.save('speak.mp3')
    
    #speak the audio file
    #accent is automatically set to american
    playsound.playsound("speak.mp3", True)
    
    

translator()