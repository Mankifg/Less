import requests
import json
import urllib.request

import functions

def comma_separate(data:list):
    b10_board_list = list(map(str,data))
    return ",".join(b10_board_list)


BASE_URL = "https://less.palcka.si"
START_POS = "bb4/bb4/6/6/4ww/4ww"


new_game = f"{BASE_URL}/new" 

#! random
b10_board = requests.get(url=new_game).json()["data"]

b10_board = [36, 320, 292, 42, 128, 288, 2304, 528, 9]


b10_board_list = comma_separate(b10_board)


game_url = f"{BASE_URL}/image?nums={b10_board_list}&lbp=" + "{}"

current_pos = START_POS

temp_game_url = game_url.format(current_pos)

print(temp_game_url)

urllib.request.urlretrieve(temp_game_url, "image.png")


boardify = functions.boardify(current_pos)

print(current_pos)
print(boardify)

MOVES_THAT_COST = functions.moves_that_cost(b10_board)

print(len(MOVES_THAT_COST))

moves_from_1_1 = functions.moves_from_x_y(boardify,1,1)

"""
all_possible_moves = functions.all_absolute_moves()

print(len(all_possible_moves))


"""