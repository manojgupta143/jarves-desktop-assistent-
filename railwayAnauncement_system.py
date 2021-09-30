import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine. setProperty("rate", 190)

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
tno=int(input("Enter Train Number :"))
tname=input("Enter Train Name :")
whereFrom=input("Enter Sarting Point :")
to=input("Enter End Point :")
via=input("Enter Root :")
pno=input("Enter Platform no")

repeat=int(input("How many timedo you want to repeat :"))
for  i in range(repeat):
    speak("May I Have Your Attention Plese")
    speak(f" Train No {tno} from {whereFrom} to {to}   {tname}    via {via}   is Araving on Platform number {pno}")