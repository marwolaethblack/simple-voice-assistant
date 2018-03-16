import pyttsx3
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
		elif("find" in text or "search" in text):
			self.engine.say('Searching')
			self.engine.runAndWait()
		elif("stop" in text):
			print("Stopping")
			if(self.stream is not None):
				self.stream.stop()




