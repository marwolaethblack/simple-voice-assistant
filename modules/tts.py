from gtts import gTTS
import vlc



def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save("tts.mp3")
    vlc.MediaPlayer('./tts.mp3').play()
