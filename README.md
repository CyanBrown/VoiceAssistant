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
      "phone": "%phone number+gateway%", //ex: 512690420@vtext.com the @vtext.com is the verizon gateway 
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
### Resources
***
##### Chatbot Tutorial from [here](https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44)