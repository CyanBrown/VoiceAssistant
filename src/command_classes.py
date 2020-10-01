from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import webbrowser
import os
from random import choice
from pyowm import OWM
import requests
import json
import smtplib


class joke:
    @staticmethod
    def sexJoke():
		# EXAMPLE OF SPECIALIZED TASK THAT YOU CAN ADD
        response = requests.get('https://inews.co.uk/light-relief/jokes/dirty-jokes-funny-100-best-229105')
        soup = BeautifulSoup(response.content, 'html.parser')

        section = soup.find_all('blockquote', class_='qa')[0]
        jokes = section.find_all('p')

        joke = choice(jokes).text
        joke = joke[1:joke.index('–') - 2]
        joke = joke.replace('“', "").replace('”', "")

        return joke

    @staticmethod
    def joke():
        with open('C:\\users\\cyanb\\python\\voiceassistant\\random\\jokes1.txt', 'r') as f:
            jokes = f.readlines()
            f.close()

        return " ".join(choice(jokes).split()[1:])


class scraping:

    @staticmethod
    def search(speech):

        scraping.getLink(speech[7:])

    def play(speech):
        scraping.getVid(speech[5:])

    @staticmethod
    def getVid(search_term, reply_num=1):

        """
		TODO: This method does not work yet, it is not capable of parsing through youtube html
		"""
        reply_num = reply_num - 1
        # term = text_correction(search_term)
        search_term = quote_plus(search_term)

        url = f"https://www.youtube.com/results?search_query={search_term}"
        # from urllib.parse import quote_plus

        response = requests.get(url)

        # print(response.content)

        soup = BeautifulSoup(response.text, 'html.parser')
        vids = soup.findAll('a', attrs={'class': 'yt-simple-endpoint style-scope ytd-video-renderer'})

        videolist = []
        for v in vids:
            tmp = 'https://www.youtube.com' + v['href']
            videolist.append(tmp)

        print(vids, videolist)

        scraping.open(videolist[reply_num])

    @staticmethod
    def getLink(search_term, reply_num=1):
        reply_num = reply_num - 1
        # term = text_correction(search_term)
        search_term = quote_plus(search_term)

        url = f"https://www.google.com/search?sxsrf=ALeKk00nB90mtI6s_pXmt3Ez_P6gUkgE3g%3A1600008673059&ei=4TFeX4yaA8TysQXFqq7gBg&q={search_term}"
        # from urllib.parse import quote_plus

        response = requests.get(url)

        # print(response.content)

        soup = BeautifulSoup(response.content, 'html.parser')

        divs = soup.find_all('a', class_='', href=True)

        try:
            href = [i['href'][7:] for i in divs if i['href'][7:12] == 'https'][reply_num]
        except IndexError:
            return None

        while 'https://www.youtube.com/watch' in href:
            reply_num += 1

            href = [i['href'][7:] for i in divs if i['href'][7:12] == 'https'][reply_num]

        # last_word = term.split()[-1]
        # print(last_word,href)
        # print(last_word,href.index(last_word))

        if requests.get(href).status_code == 404:
            try:
                href = href[0:href.index('&')]
            except:
                href = href.rsplit("/", 1)[0]
        # value = divs.div.span.text

        scraping.open(href)

    @staticmethod
    def open(url):
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)

    @staticmethod
    def define(word, def_num=1):
        def_num -= 1
        word = quote_plus(word)
        url = f'https://www.dictionary.com/browse/{word}?s=t'

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        big = soup.find_all('div', class_='css-1o58fj8 e1hk9ate4')[0]
        definition = big.find_all('span')[def_num].text

        return definition.replace("(", "").replace(")", "")


# class weather:
#
# 	owm = OWM('you api key here')
# 	mgr = owm.weather_manager()
#
#
# 	@staticmethod
# 	def getTemperatureInfo(city,metric = 'fahrenheit',measurement = 'temp'):
# 		obs = weather.mgr.weather_at_place(city)
# 		w = obs.weather
# 		# {'temp': 68.52, 'temp_max': 71.6, 'temp_min': 64.99, 'feels_like': 65.25, 'temp_kf': None}
# 		return w.temperature(metric)[measurement]
#
# 	@staticmethod
# 	def getSunTime(city):
# 		obs = weather.mgr.weather_at_place(city)
# 		w = obs.weather
#
# 		return w.sunrise_time(timeformat='iso')
#
# 	@staticmethod
# 	def hasRain(city):
# 		obs = weather.mgr.weather_at_place(city)
# 		w = obs.weather
#
# 		return w.rain
# 	#def clouds
# 	#preassure
# 	#more

serversmtp = smtplib.SMTP( "smtp.gmail.com", 587 )

serversmtp.ehlo()
serversmtp.starttls()
serversmtp.ehlo()

serversmtp.login( 'your gmail account', 'your gmail account password')

class message:

	@staticmethod
	def get_carrier(number):
		url = 'https://api.telnyx.com/v1/phone_number/1' + str(number)
		html = requests.get(url).text
		data = json.loads(html)
		data = data["carrier"]
		carrier = data["name"]
		carrier = carrier.lower()

		if 'verizon' in carrier:
			return "@vzwpix.com"
		elif 'cingular' in carrier:
			return '@mms.att.net'
		elif 'cricket' in carrier:
			return '@mms.mycricket.com'
		elif 'sprint' in carrier:
			return '@pm.sprint.com'
		elif 't-mobile' in carrier:
			return '@tmomail.net'


	@staticmethod
	def sendText(number, message):
		serversmtp.sendmail("your phonenumber+gateway",str(number),message)

	@staticmethod
	def sendEmail(number, message):
		serversmtp.sendmail("your email",str(number),message)

