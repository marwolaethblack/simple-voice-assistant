import wikipedia
from modules.ytPlayer import ytPlayer
from modules.tts import say



class CommandHandler():
	stream = None


	def handler(self,text):
		
		if("play" in text):
			print("Playing")
			query = text.split("play",1)[1]
			print(query)
			self.stream = ytPlayer.streamAudio(query, self.engine)
			print(self.stream)
		elif("search" in text):
			query = text.split("search",1)[1]
			result = wikipedia.search(query)
			print(result[0])
			say(result[0])
		elif("stop" in text):
			print("Stopping")
			if(self.stream is not None):
				self.stream.stop()
			else:
				print("Nothing to stop")




