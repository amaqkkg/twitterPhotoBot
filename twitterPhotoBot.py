import glob
import random

from twython import Twython

#Define our constant variables. Change accordingly
CONSUMER_KEY = 'xx'
CONSUMER_SECRET = 'yy'
ACCESS_KEY = 'zz'
ACCESS_SECRET = '11'

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

def RandomCatImage(folder):
        #image folder
        images = glob.glob(folder + '*')
        image_open = open(random.choice(images))
        #tweet
        image_select = api.upload_media(media=image_open)
        api.update_status(status=" ", media_ids=image_select['media_id'])


RandomCatImage('./images/')
