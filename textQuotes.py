import time
import schedule
import json
import urllib
from twilio.rest import TwilioRestClient

nums = [""]
ACCOUNT_SID = ''
AUTH_TOKEN = ''


def textIt():
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	url = "http://www.iheartquotes.com/api/v1/random?format=json&max_characters=160&source=hitchhiker+dune+plato+science+education+henry_david_thoreau+libery+wisdom+love+literature+technology+nietzsche+math+oscar_wilde+wisdom+humorists+art+platitudes"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	quote = data["quote"]
	for n in nums: 
		client.messages.create(
			to=n, 
			from_="", 
			body=quote 
		) 


schedule.every().day.at("10:00").do(textIt)
schedule.every().day.at("13:00").do(textIt)
schedule.every().day.at("16:00").do(textIt)
schedule.every().day.at("20:00").do(textIt)

while True:
    schedule.run_pending()
    time.sleep(1)
