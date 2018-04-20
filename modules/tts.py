from gtts import gTTS
import vlc
import time



def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save("tts.mp3")
    stream = vlc.MediaPlayer('./tts.mp3')
    stream.play()

    #block while playing the text to speech sound file so the voice recognition doesnt capture it
    while str(stream.get_state()) != "State.Ended":
        time.sleep(1)
    
    
