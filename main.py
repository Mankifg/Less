import requests
import json
import urllib.request

import functions

BASE_URL = "https://less.palcka.si"
START_POS = "bb4/bb4/6/6/4ww/4ww"


new_game = f"{BASE_URL}/new" 

random_board_pos_nums = requests.get(url=new_game).json()["data"]
random_board_pos_nums = list(map(str,random_board_pos_nums))
random_board_pos_nums = ",".join(random_board_pos_nums)


game_url = f"{BASE_URL}/image?nums={random_board_pos_nums}&lbp=" + "{}"

current_pos = START_POS

temp_game_url = game_url.format(current_pos)

print(temp_game_url)
urllib.request.urlretrieve(temp_game_url, "image.png")



current_pos = functions.boardify(current_pos)

print(current_pos)