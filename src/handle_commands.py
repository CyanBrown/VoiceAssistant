from src.command_classes import *
import json
import os
import re
from src.chatbot import chatbot_response
import pyttsx3
engine = pyttsx3.init()
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

with open('configs/commands.json') as f:
	json_data = json.load(f)

def say(words):
	engine.say(words)
	engine.runAndWait()

def command(text):
	text = text.lower()

	if text[0:6] == 'search':
		scraping.search(text)

	# Doesn't work yet
	# elif text[0:4] == 'play':
	# 	scraping.play(text)

	elif text[0:4] == 'text':
		person = text.split()[1]
		try:
			message.sendText(json_data['contacts'][person]['phone']," ".join(text.split()[2:]))
		except KeyError:
			person = re.sub("-","",person)

			person+=message.get_carrier(person)

			message.sendText(person," ".join(text.split()[2:]))
		except smtplib.SMTPRecipientsRefused:
			print("No contact given")

	elif text[0:4] == 'email':
		person = text.split()[1]

		try:
			message.sendEmail(json_data['contacts'][person]['email']," ".join(text.split()[2:]))
		except KeyError:
			message.sendEmail(person," ".join(text.split()[2:]))
		except smtplib.SMTPRecipientsRefused:
			print("No contact given.")
	
	elif text[0:3] == 'run':
		for i in json_data.keys():
			if text[4:] == i:
				os.system(json_data[i])
				# print(json_data[i])

	elif 'joke' in text:
		say(joke.joke())

	elif text[0:6]=='repeat':
		say(text[7:])

	else:
		if text != '':
			say(chatbot_response(text))



