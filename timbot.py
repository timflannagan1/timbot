import os
from slackclient import SlackClient
import random
import datetime


slack_token = os.environ['SLACK_API_TOKEN']
channel_name = os.environ['SLACK_CHANNEL_NAME']
timbot_user_id = os.environ['SLACK_TIMBOT_USER_ID']

sc = SlackClient(slack_token)

random.seed(datetime.datetime.now())

alert = True

while True:
	history = sc.api_call("groups.history", channel=channel_name, count=1)

	#lunch alert
	time = datetime.datetime.now().strftime('%H:%M')
	if time == '11:30':
		if alert:
			sc.api_call("chat.postMessage", channel=channel_name, text='IT IS THE IDEAL LUNCH TIME GO TO LUNCH', as_user=True)
			alert = False
	else:
		alert = True
					
	# look for a message in the chat that starts with '@timbot .....'
	if 'messages' in history:
		for message in  history['messages']:
			if 'text' in message:
				message = message['text']
				message = message.encode('UTF8')

				#openstack meme
				if 'openstack' in message:
					sc.api_call("chat.postMessage", channel=channel_name, text='i hear opensack is a career killer', as_user=True)


				if message.startswith(timbot_user_id):

					#message now equals what was after '@timbot'
					message = message.replace(timbot_user_id, '')

					#where to go to lunch
					if 'lunch' in message and 'where' in message:
						
						#if friday
						if datetime.datetime.today().weekday() == 4:
							#choose place to go
							places = ['pauls','moes','asian plus','99s']
							sc.api_call("chat.postMessage", channel=channel_name, text=random.choice(places), as_user=True)

						#mon-thur 
						else:
							sc.api_call("chat.postMessage", channel=channel_name, text='epicurean feast', as_user=True)

					#what time is lunch
					elif 'lunch' in message and ('time' in message or 'when' in message):
						sc.api_call("chat.postMessage", channel=channel_name, text="11:30", as_user=True)

					#base response 
					else:
						sc.api_call("chat.postMessage", channel=channel_name, text="keep pounding", as_user=True)

