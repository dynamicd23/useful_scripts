from twython import Twython, TwythonError
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
import glob
import os


twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

def main():
	try:
		for fileName in glob.glob('/home/pi/twitter/tweetPics/mypic*'):
			message = "Yo!"
			with open(fileName, 'rb') as photo:
				twitter.update_status_with_media(status=message, media=photo)
				print("Tweeted: %s" % message)
				os.remove(fileName)
	except TwythonError as e:
		print(e)


if __name__ == '__main__':
    main()

