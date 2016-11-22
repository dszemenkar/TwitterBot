
from __future__ import print_function
import random
import os
import time
from twython import Twython
CONSUMER_KEY = '#######'
CONSUMER_SECRET = '#######'
ACCESS_KEY = '#######'
ACCESS_SECRET = '######'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

nostalgi = 0

while (nostalgi == 0):
    os.system('clear')
    quote_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'twitterbot.txt')
    f = open(quote_file)
    txt = f.read()
    lines = txt.split('\n.\n')
    api.update_status(status=random.choice(lines))
    time.sleep (120)
