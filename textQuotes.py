from twilio.rest import TwilioRestClient 
import time
import schedule
import random

ACCOUNT_SID = "" 
AUTH_TOKEN = "" 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
now = time.strftime("%H:%M:%S")

def job():
	quotes = ["You fucking suck", "You are fat", "Tacos", "Pussy"]
	re = random.choice(quotes)
	client.messages.create(
		to="+", 
		from_="+", 
		body=re, 
	) 

schedule.every().day.at("20:48").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
