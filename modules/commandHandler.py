import pyttsx3
import wikipedia
from modules.ytPlayer import ytPlayer


class CommandHandler():
	stream = None
	engine = pyttsx3.init()

	def handler(self,text):
		
		if("play" in text):
			print("Playing")
			query = text.split("play",1)[1]
			print(query)
			self.stream = ytPlayer.streamAudio(query, self.engine)
			print(self.stream)
			self.engine.runAndWait()
		elif("search" in text):
			query = text.split("search",1)[1]
			self.engine.say('Searching')
			result = wikipedia.search(query)
			print(result[0])
			self.engine.runAndWait()
		elif("stop" in text):
			print("Stopping")
			if(self.stream is not None):
				self.stream.stop()
			else:
				print("Nothing to stop")
				self.engine.say("Nothing to stop")




