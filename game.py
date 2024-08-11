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

lbp = START_POS


while 1:
    move_power = 3
        
    while 1:
        print(functions.convert_to_url(b10_board,lbp,BASE_URL))
        print(f"Move power left: {move_power}")
        white_legal_cost = functions.cost_of_moves(lbp,b10_board,"w")
        user_move = input("Enter move in coordnite notation a1a3 >")
        succes,move_ary = pars.parse_move(user_move)
        if not succes:
            print(move_ary)
            continue
        
        cost = functions.cost_of_move(white_legal_cost,move_ary)
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
    
    move_power -= cost
    
    if move_power == 0:
        break
    
    
print("Player done")