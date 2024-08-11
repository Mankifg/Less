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
    to_spend = 3
        
    while 1:
        print(functions.convert_to_url(b10_board,lbp,BASE_URL))
        white_legal_cost = functions.cost_of_moves(lbp,b10_board,"w")
        user_move = input("Enter move in coordnite notation a1a3 >")
        move_ary = pars.parse_move(user_move)
        print(move_ary)
        cost = functions.cost_of_move(white_legal_cost,move_ary)
        print(cost)
        if cost == 0:
            print("Not legal")
            continue
        if cost > to_spend:
            print("You dont have enought Move Power™")
            continue
        
        break
    
    
    print("# move ")
    print(lbp)
    lbp = functions.push_move(lbp,move_ary)
    print(lbp)
    
    to_spend -= cost
    print("Move done")
    
print("Player done")