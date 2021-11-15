import pyttsx3
import speech_recognition as sr
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new ChatBot with name Dev.to
chatbot = ChatBot(
    'Neon',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

print("\nHello there, Im Neon and I am at your service:\n")
while True:
    try:
      r = sr.Recognizer()                                     
      with sr.Microphone() as source:                        
        audio = r.listen(source)   
        try:
          bot_input = (r.recognize_google(audio))
        except sr.UnknownValueError:
          print("Could not understand audio")
        except sr.RequestError as e:
          print("Could not request results; {0}".format(e))
        bot_input = (r.recognize_google(audio))
        r = sr.Recognizer()

# Function to convert text to
# speech
        def SpeakText(bot_response):
          
          # Initialize the engine
          engine = pyttsx3.init()
          engine.say(bot_response)
          engine.runAndWait()
        if bot_input.strip()=='Bye':
            print('Neon: Bye')
            break

        bot_response = chatbot.get_response(bot_input)
        print(bot_response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
 
      
#Test Code
