import requests
import json
import urllib.request

import functions


BASE_URL = "https://less.palcka.si"
START_POS = "bb4/bb4/6/6/4ww/4ww"


new_game = f"{BASE_URL}/new"

#! random
b10_board = requests.get(url=new_game).json()["data"]

b10_board = [0, 11, 584, 288, 1280, 2048, 72, 0, 0]


current_pos = START_POS

game_url = functions.convert_to_url(b10_board, current_pos, BASE_URL)

temp_game_url = game_url.format(current_pos)

print(temp_game_url)

urllib.request.urlretrieve(temp_game_url, "image.png")

boardify = functions.boardify(current_pos)


print("*" * 10 + "Position")
print(current_pos)
print(boardify)

print("*" * 10, "\nMoves from x,y")
print("0,0", functions.every_one_step_move(0, 0))


cost_moves = functions.moves_that_cost_all(b10_board)

print("*" * 10 + "Double cost moves")
print(cost_moves)
print(len(cost_moves))

# moves_from_1_1 = functions.moves_from_x_y(boardify,1,1)

WALL_MOVES_WITH_COST = functions.reformate_wall_moves(cost_moves)
print(WALL_MOVES_WITH_COST)
print(len(WALL_MOVES_WITH_COST))

legal = functions.legal_moves_from_xy(boardify, WALL_MOVES_WITH_COST, 0, 1)
print("legal moves from 0 1")
print(legal)

white_places = functions.all_cords_that_match(boardify, "b")
print(white_places)

"""print("white legal")
all_white_legal = functions.legal_moves_for_color(boardify,WALL_MOVES_WITH_COST,"b")
print(len(all_white_legal),all_white_legal)"""
