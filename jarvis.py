import pyttsx3
import os
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("How can i help you")


while True:
	print("How can i help you: "  , end='')
	p = input()

	

	if ("run" in p)  and ("chrome" in p):
	  os.system("chrome")

	elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")

	elif ("run" in p)  and ("player" in p) and ("media" in p):
	  os.system("wmplayer")

	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("dont support")