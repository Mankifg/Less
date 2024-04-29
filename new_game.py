import requests
import json
import urllib.request

import functions



BASE_URL = "https://less.palcka.si"
START_POS = "bb4/bb4/6/6/4ww/4ww"


new_game = f"{BASE_URL}/new" 

#! random
b10_board = requests.get(url=new_game).json()["data"]


current_pos = START_POS

game_url = functions.convert_to_url(b10_board,current_pos,BASE_URL)
print(game_url)