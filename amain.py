import requests
import json
import urllib.request

import functions
import pars

BASE_URL = "https://less.palcka.si"
START_POS = "0b4/bb4/b5/6/4ww/4ww"


new_game = f"{BASE_URL}/new"

#! random
b10_board = requests.get(url=new_game).json()["data"]

b10_board = [0, 11, 584, 288, 1280, 2048, 72, 0, 0]


current_pos = START_POS

game_url = functions.convert_to_url(b10_board, current_pos, BASE_URL)

temp_game_url = game_url.format(current_pos)

print(temp_game_url)

urllib.request.urlretrieve(temp_game_url, "image.png")


print("*"*30)
white_legal_cost = functions.cost_of_moves(current_pos,b10_board,"w")
print(white_legal_cost)

user_move = input("Enter move in coordnite notation a1a3 >")
move_ary = pars.from_coord_notation(user_move)
print(move_ary)


