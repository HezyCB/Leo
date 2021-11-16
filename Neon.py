from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new ChatBot with name Neon
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
        if bot_input.strip()=='Bye':
            print('Neon: Bye')
            break

        bot_response = chatbot.get_response(bot_input)
        print(bot_response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
 
      
#Test Code
