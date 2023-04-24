import googletrans
import speech_recognition
import gtts
import playsound

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Please say what you want to translate")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="en")



translator = googletrans.Translator()
translation = translator.translate(text, dest='fr')
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang='fr')
converted_audio.save("frenchspeech1.mp3")
playsound.playsound("frenchspeech1.mp3")

print(googletrans.LANGUAGES)








'''import googletrans
import speech_recognition
import gtts
from pydub import AudioSegment
from pydub.playback import play

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Please say what you want to translate")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="en")

translator = googletrans.Translator()
translation = translator.translate(text, dest='fr')
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang='fr')
converted_audio.save("frenchspeech1.mp3")
audio = AudioSegment.from_file("frenchspeech1.mp3", format="mp3")
play(audio)
print(googletrans.LANGUAGES)'''
