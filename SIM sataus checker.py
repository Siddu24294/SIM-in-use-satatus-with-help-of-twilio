from twilio.rest import Client
import twilio
import time

account_sid = 'AC7546f1cb0d51bbbc0229b8d340bcfa00'
auth_token = '8a5ce693e4b2c12c8d1591f3fc850979'
client = Client(account_sid, auth_token)
call_connected=False

while 1:
	if call_connected:break
	try :
		call = client.calls.create(
			url='http://demo.twilio.com/docs/voice.xml',   # message for phone lost
			to='+91XXXXXXXXXX',  # number to be traced
			from_='+18123894633'
		)
		time.sleep(60)
		print(call)
		call_connected=True

	except twilio.base.exceptions.TwilioRestException:
		call_connected=False
		print('Call unable to connect.Phone is still switched off.')

		callnum2=client.calls.create(
			url='http://demo.twilio.com/docs/voice.xml', # message for phone found
			to='+91XXXXXXXXXX',                          # your numbr on which you will be notified
			from_='+18123894633'
		)
