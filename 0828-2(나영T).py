from gtts import gTTS

text=""
tts=gTTS(text=text, lang='ko')
tts.save(r"hi.mp3")