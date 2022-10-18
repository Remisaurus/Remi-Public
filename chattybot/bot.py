print('breaking in eggbot')
'venv/scripts/activate'

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

chategg = ChatBot("Chategg")
trainer = ListTrainer(chategg)
CORPUS_FILE = "chat.txt"

cleaned_corpus = clean_corpus(CORPUS_FILE)

trainer.train(cleaned_corpus)
trainer = ListTrainer(chategg)
trainer.train([
    "Hoi",
    "Hallo, vriend 🤗",
])
trainer.train([
    "ben jij een ei?",
    "Nee, ik zit in een ei",
])
exit_conditions = (":q", "quit", "exit", "stop", 'Quit', 'Exit', 'QUIT', 'EXIT')

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🥚 {chategg.get_response(query)}")

