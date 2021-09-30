import pyttsx3
speaker=pyttsx3.init()

name=input("enter your name")

speaker.say(name+"good morning")
#print(speaker)

speaker.runAndWait()