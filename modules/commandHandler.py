import pyttsx3
from modules.ytPlayer import ytPlayer


def commandHandler(text):

	engine = pyttsx3.init()


	if("play" in text):
		print("Playing")
		stream = ytPlayer.streamAudio("look at me", engine)
		engine.runAndWait()
	elif("find" in text or "search" in text):
		engine.say('Searching')
		engine.runAndWait()


