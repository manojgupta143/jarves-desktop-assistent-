import pyttsx3
tym=int(input("Enter your time in 24 hours format :"))
speaker=pyttsx3.init()
if (tym>4) and (tym<12):
    speaker.say("i'm  jarves  your virtul assistant how can help you good morning guys have a good day")
elif (tym>12) and (tym<17):
    speaker.say("good afternoon sir hope you injoying your day")
elif (tym>17) and (tym<21):
    speaker.say("good evening guys hope you injoying your wonderful evening")
    speaker.say("i guess you spend a wonderful day sir")
else:
    speaker.say("good night sweet dream")
speaker.runAndWait()
