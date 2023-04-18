import gtts
import playsound
user_input = input("Enter what you want to hear:")

speech = gtts.gTTS(user_input, lang="en") #for french fr, Hi for hindi

speech.save("file1.mp3")
playsound.playsound("file1.mp3")