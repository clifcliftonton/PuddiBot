import tweepy
import json
import random
from keys import keys


#Required for twitter app authorization
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET_KEY = keys['consumer_secret']		
ACCESS_TOKEN = keys['access_token']
ACCESS_SECRET_TOKEN = keys['access_token_secret']

#Override tweepy's listener class's functions to customize handling of returned data from twitter stream
class PuddiListener(tweepy.StreamListener):

	#Injection of api necessary for on_data() to be able to make API calls to twitter app
	def __init__(self, api):
		self.api = api
		super(tweepy.StreamListener, self).__init__()

	def on_status(self, status):
		print(status.text)

	def on_data(self, data):
		#Handles returned json data from on_data()
		decoded = json.loads(data)
		sn = decoded['user']['screen_name']

		#Enter various messages here
		m = [' 超ギガプリン ',
			 ' プリン プリン',
			 ' puddi puddi ',
			 ' giga puddi ',
			 ' ᵖᵘᵈᵈᶦ ᵖᵘᵈᵈᶦ ']

		c = random.choice(m)

		#Actual api call using tweepy
		try:
			if decoded['user']['id'] != 780242910130282496:
				api.update_status(status='@%s %s' % (sn, u"\U0001F36E"+c+u"\U0001F36E"))
		except Exception as e:
			pass

		return True

	def on_error(self, status):
		print(status.text)
		return True

#Authorization needed to connect to twitter app
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)

Puddi = PuddiListener

#Connects the listener to twitter stream
stream = tweepy.Stream(auth = auth, listener = Puddi(api))

#Strings being tracked on twitter stream
track = ['#puddipuddi', '#gigapuddi', '#gigapudding', 'puddi puddi', 'giga puddi', 'giga pudding']

stream.filter(track=track)
