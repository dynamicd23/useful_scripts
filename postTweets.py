from twython import Twython, TwythonError
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
import glob
import os
import sys


twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

def main():
	try:
		for fileName in glob.glob('/home/pi/twitter/tweetPics/mypic*'):
			if len(sys.argv) > 1:
				print(sys.argv[1])
				message = sys.argv[1]
			else:
				message = "Yo! Buzz I am sing song"
			with open(fileName, 'rb') as photo:
				twitter.update_status_with_media(status=message, media=photo)
				print("Tweeted: %s" % message)
				os.remove(fileName)
	except TwythonError as e:
		print(e)


if __name__ == '__main__':
    main()

