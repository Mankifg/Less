import requests
import json
import urllib.request
import utils

import pars
import functions


BASE_URL = "https://less.palcka.si"
START_POS = "bb4/bb4/6/6/4ww/4ww"
#START_POS = utils.random_lbp()
print(START_POS)

new_game = f"{BASE_URL}/new" 

#! random
b10_board = requests.get(url=new_game).json()["data"]
b10_board = [80,132,1280,288,9,292,1344,1280,164]
lbp = START_POS

def swap_players(p):
    if p == "w": return "b"
    if p == "b": return "w"
    
    
move_power = 3 
current_player = "w"   
while 1: #? player move
    while 1: #? good input
        print(functions.convert_to_url(b10_board,lbp,BASE_URL))
        print(f"Move power left: {move_power}")
        color_legal_cost = functions.cost_of_moves(lbp,b10_board,current_player)
        print(len(color_legal_cost),color_legal_cost)
        user_move = input(f"{current_player} | Enter move in coordnite notation a1a3 >")
        succes,move_ary = pars.from_coord_notation(user_move)
        if not succes:
            print(move_ary)
            continue
        print(move_ary)
        cost = functions.singe_move_cost(color_legal_cost,move_ary)
        print(cost)
        if cost == 0:
            print("Not legal")
            continue
        if cost > move_power:
            print("You dont have enought Move Power™")
            continue
        
        break
    
    print("# move ")
    lbp = functions.push_move(lbp,move_ary)
    print("Move done")
    
    move_power = move_power -  cost
    
    if move_power == 0:
        break
    
    print("move finished")
    
print("Player finish")
current_player = swap_players(current_player)
