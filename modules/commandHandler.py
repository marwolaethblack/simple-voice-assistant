import pyttsx3
from modules.ytPlayer import ytPlayer


def commandHandler(text):

	engine = pyttsx3.init()
	stream = None


	if("play" in text):
		print("Playing")
		query = text.split("play",1)[1]
		print(query)
		stream = ytPlayer.streamAudio(query, engine)
		engine.runAndWait()
	elif("find" in text or "search" in text):
		engine.say('Searching')
		engine.runAndWait()
	elif("stop" in text):
		if(stream is not None):
			stream.stop()


