import requests
import json
import urllib.request
import random

import pars
import functions

BASE_URL = "https://less.palcka.si"
START_POS = "bb4/bb4/6/6/4ww/4ww"
#START_POS = utils.random_lbp()
print(START_POS)

new_game = f"{BASE_URL}/new" 

#! random
#b10_board = requests.get(url=new_game).json()["data"]

b10_board = [80,132,1280,288,9,292,1344,1280,164]
#b10_board = [0,0,0,0,8,0,16,0,32]

lbp = START_POS

print(functions.convert_to_url(b10_board,lbp,BASE_URL))

a = functions.get_wall_moves(b10_board)

print(a)
print(len(a)) 
print()
for m,v in a: 
    print(m,v) 
for b,v in a:
    print(pars.from_arry_notation(b))
