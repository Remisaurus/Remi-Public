from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
import pyttsx3
import speech_recognition

CORPUS_FILE = "./studydata/chat.txt"

chategg = ChatBot("Chategg")
trainer = ListTrainer(chategg)
say = pyttsx3.init()
recognize = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

voice = say.getProperty('voices') 
say.setProperty('voice', voice[1].id)  # set to NL language speech

exit_conditions = (":q", "quit", "exit", "stop")

def sayit(text):
    say.say(text)
    say.runAndWait()
    
def listen():
    with mic as source:
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source, phrase_time_limit=5)
    return audio
    
def querying():
    try:
        this = recognize.recognize_google(listen(), language = 'nl-NL')
        return this
    except speech_recognition.RequestError:
        sayit('I was unable to reach or get a response from the microphone')
    except speech_recognition.UnknownValueError:
        return 'Niet verstaan'

def communicate():
    query = querying()
    print('user said: ' + query)
    if query in exit_conditions:
        quit()
    else:
        respons = chategg.get_response(query)
        print(f"🥚 {respons}")
        sayit(respons)
        communicate()

# starting chatbot (Dutch in this case)
    
sayit('maar zeg alee, ik ben toch niet zot. Geef mij een paar minuten om gegevens te bestuderen. Ik ga nu beginnen.')

# teaching chatbot (with txt file exported with Whatsapp stated in CORPUS_FILE) 

cleaned_corpus = clean_corpus(CORPUS_FILE)

trainer.train(cleaned_corpus)
trainer.train([
    "Hoi",
    "Hallo, vriend",
])
trainer.train([
    "ben jij een ei?",
    "Nee, ik zit in een ei",
])

#starting communication

sayit('Ok, ik ben er klaar voor. de regels zijn dat ik elke keer 1 seconde nodig heb nadat ik wat heb gezegt om de microfoon te calibreren, en dat je daarna 5 seconden hebt om wat te zeggen.')

communicate()




