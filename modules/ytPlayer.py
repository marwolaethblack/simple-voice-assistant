import urllib.request
import urllib.parse
import re
import pafy
import pprint
import vlc





class ytPlayer():

	def yt_link_from_query(query):
		query_string = urllib.parse.urlencode({"search_query" : query})
		html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
		return "http://www.youtube.com/watch?v=" + search_results[0]

	def streamAudio(query, engine):
		yt_url = ytPlayer.yt_link_from_query(query)
		video = pafy.new(yt_url)
		engine.say("Playing " + video.title)
		bestaudio = video.getbestaudio()
		stream = vlc.MediaPlayer(bestaudio.url)
		stream.play()
		return stream
		






