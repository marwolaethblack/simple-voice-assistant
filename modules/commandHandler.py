import pyttsx3


def commandHandler(text):

	engine = pyttsx3.init()


	if("play" in text):
		engine.say('Playing')
		engine.runAndWait()
	elif("find" in text or "search" in text):
		engine.say('Searching')
		engine.runAndWait()


