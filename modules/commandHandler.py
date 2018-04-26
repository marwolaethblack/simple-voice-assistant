import wikipedia
import datetime
import requests
from modules.ytPlayer import ytPlayer
from modules.tts import say
from modules.search import searchGoogle, searchDDG



class CommandHandler():

	stream = None
	searchEngine = "Google"
	name = "alexa"


	def handler(self,text):
		text = text.lower()

		if( (self.name + " play") in text):
			if(self.stream is not None):
				self.stream.stop()
				stream = None
			print("Playing")
			query = text.split("play",1)[1]
			print(query)
			self.stream = ytPlayer.streamAudio(query)
			self.stream.audio_set_volume(99)
			print(self.stream.audio_get_volume())


		elif("turn down the volume" in text):
			if(self.stream is not None):
				currentVolume = self.stream.audio_get_volume()
				if(currentVolume == 33):
					say("Cannot decrease volume any more.")
					print("Cannot decrease the volume any more")
				else:
					newVolume = currentVolume - 33
					self.stream.audio_set_volume(newVolume)
			else:
				say("No stream is playing right now")


		elif("turn up the volume" in text):
			if(self.stream is not None):
				currentVolume = self.stream.audio_get_volume()
				if(currentVolume == 99):
					say("Cannot increase the volume any more")
					print("Cannot increase the volume any more")
				else:	
					newVolume = currentVolume + 33
					self.stream.audio_set_volume(newVolume)
			else:
				say("No stream is playing right now")


		elif((self.name + " wikipedia") in text):
			query = text.split("wikipedia",1)[1]
			result = wikipedia.search(query)
			summary = wikipedia.summary(result[0])
			print(summary)
			say(summary)


		elif((self.name + " search") in text):
			query = text.split("search",1)[1].lstrip()
			result = "No result"
			if(self.searchEngine == "Google"):
				result = searchGoogle(query)
			if(self.searchEngine == "DuckDuckGo"):
				result = searchDDG(query)
			print(result)
			say(result)


		elif((self.name + " what") in text and "time" in text):
			now = datetime.datetime.now()
			text = "It is " + str(now.hour) + (" hour " if now.hour == 1 else " hours ") + "and " + str(now.minute) + (" minute" if now.minute == 1 else " minutes")
			say(text)
			print(text)


		elif((self.name + " what") in text and ("date" in text or "day" in text)):
			dt=datetime.date.today()
			say(dt.strftime('%A %B %d, %Y'))


		elif((self.name + " tell") in text and "joke" in text):
			joke = requests.get("https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke").json()
			print(joke)
			say(joke["setup"] + "    " + joke["punchline"])


		elif("stop" in text):
			if(self.stream is not None):
				print("Stopping")
				say("Stopping")
				self.stream.stop()
				stream = None
			else:
				print("Nothing to stop")
				say("Nothing to stop")


		elif("change your name to" in text):
			new_name = text.split("to",1)[1]
			self.name = new_name.lstrip().lower()
			say("My new name is " + self.name)

		elif("what is your name" in text.lower() or "what's your name" in text.lower()):
			say("Hello my name is " + self.name + ". Nice to meet you !")

		elif("thank you" in text):
			say("No problem.")


		elif(("why" in text and "so" in text and "bad" in text) or "sucks" in text):
			say("Sorry but please be patient with me. I am autistic.")





