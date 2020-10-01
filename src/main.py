import speech_recognition as sr
from src.handle_commands import command
import pyttsx3
engine = pyttsx3.init()

# print(sr.Microphone.list_microphone_names())
r = sr.Recognizer()
mic = sr.Microphone()
r.energy_threshold = 1500
r.dynamic_energy_threshold = True

# harvard = sr.AudioFile('recording.wav')
while True:
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)


	try:
		words = r.recognize_google(audio)
	except sr.UnknownValueError:
		words = ""
		print('nope')
		# engine.say("Sorry, I didn't catch that.")
		# engine.runAndWait()

	if words == 'exit':
		break

	print(words)
	command(words)

