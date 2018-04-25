# simple-voice-assistant
A simple voice asssistant using the Speech Recognition python module and google text to speech module.  
Written in Python 3.  

Requires pipenv to install dependecies and vlc to stream audio.  
Run `pipenv install` to install them. Next run `pipenv shell` followed by `python3 va.py` or `python va.py` depending on your python installation, to run the program.

The voice assisstant listens to specific keywords or commands.  
The key words implemented are:  
PLAY - When it recognized that you've said play it takes everything after 'play' and searches youtube for the first result whose audio is streamed afterwards  
STOP - Stops a stream started by PLAY. If no stream is running it informs you that there is nothing to stop.  
TURN UP/DOWN THE VOLUME - Increases or decreases the volume of the stream  
SEARCH - Scrapes google or duckduckgo for a relevant search result, says them out loud.  
WIKIPEDIA - Takes everything after the wikipedia command and searches wikipedia for the first result which is then read out loud.    
TIME - Tells you the current time   
DATE/DAY - Tells you the current date  
JOKE - Tells you a joke
