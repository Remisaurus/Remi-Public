import pyttsx3

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)
    '''
    install NL/BE microsoft language,
    then regedit is needed on windows 10/11, look on internet for instructions.
    '''
    
    
say = pyttsx3.init()
voice = say.getProperty('voices') 
say.setProperty('voice', voice[1].id)  # set to NL language speech
def sayit(text):
    say.say(text)
    say.runAndWait()
    
sayit('maar zeg alee, ik ben toch niet zot')