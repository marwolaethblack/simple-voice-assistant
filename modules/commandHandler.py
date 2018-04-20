import wikipedia
import datetime
import requests
from modules.ytPlayer import ytPlayer
from modules.tts import say




class CommandHandler():
	stream = None


	def handler(self,text):
		
		if("play" in text):
			print("Playing")
			query = text.split("play",1)[1]
			print(query)
			self.stream = ytPlayer.streamAudio(query)
			print(self.stream)
		elif("search" in text):
			query = text.split("search",1)[1]
			result = wikipedia.search(query)
			summary = wikipedia.summary(result[0])
			print(summary)
			say(summary)
		elif("what" in text and "time" in text):
			now = datetime.datetime.now()
			text = "It is " + str(now.hour) + (" hour " if now.hour == 1 else " hours ") + "and " + str(now.minute) + (" minute" if now.minute == 1 else " minutes")
			say(text)
			print(text)
		elif("what" in text and ("date" in text or "day" in text)):
			dt=datetime.date.today()
			say(dt.strftime('%A %B %d, %Y'))
		elif("tell" in text and "joke" in text):
			joke = requests.get("https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke").json()
			print(joke)
			say(joke["setup"] + "   " + joke["punchline"])
		elif("stop" in text):
			if(self.stream is not None):
				print("Stopping")
				say("Stopping")
				self.stream.stop()
				stream = None
			else:
				print("Nothing to stop")
				say("Nothing to stop")
		elif("thank you" in text):
			say("Gotchu FAM")
		elif(("why" in text and "so" in text and "bad" in text) or "sucks" in text):
			say("Sorry but please be patient with me. I am autistic.")





