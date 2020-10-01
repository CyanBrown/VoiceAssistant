# Python Voice Assistant
##### By: Cyan Brown
***
### Functionalities
***
#### Contacts
INFO: Contacts a person via text or email

IMPORTANT: Make sure to fill out the smtp data in command_classes.py starting at line 169

REQUIREMENTS: The %PersonName% is used in "text John hello" command

COMMANDS:
* Text (person name or number) (what you want to text)
* Email (person name) (what you want to email)
```json
{
  "Contacts":{
    "%PersonName%":{
      "phone": "%phone number+gateway%",
      "email": "exapleemail@gmail.com"
    } 
  }
}
```
***
#### Command Line
INFO: Runs a command

REQUIREMENTS: The %ProgramName% is used in "run %ProgramName%" command 

COMMANDS: 
* Run (program name)
```json
{
  "%ProgramName%": "%this is what you would type in command prompt to run the desired program",
  "%Example%": "python C:\\users\\you\\test.py"
}
```
***
#### Define
INFO: Defines a word

COMMANDS:
* Define (word you want to define)
***
#### Jokes
INFO: Tells a joke

COMMANDS (will trigger if following words are said at all):
* dirty joke
* joke
***
#### Search
INFO: Searches as pulls up the first response web page

COMMANDS:
* Search (keywords you want to search)
***
#### Repeat
INFO: Repeats words that you say

COMMANDS:
* Repeat (words you want it to repeat)
***
#### Exit
INFO: Stops the program

COMMANDS (must only say following words):
* Exit
***
#### Chatbot
INFO: Ai trained on simple commands that you can find [here](https://github.com/CyanBrown/VoiceAssistant/blob/master/src/Chatbot/intents.json)

COMMANDS: Any command that does not fall into the above categories will be responded to by the chatbot
```json
{"tag": "%name of type of conversation%",
         "patterns": ["%example statement 1%","%example statement 2%","You can do as many of these as you want"],
         "responses": ["%suggested response 1%","%suggested response 2%","You can do as many of these as you want"],
         "context": [""]
}
```
***
### Resources
***
##### Chatbot Tutorial from [here](https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44)