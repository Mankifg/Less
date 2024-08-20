import requests
import json
import urllib.request
import random

import pars
import functions
import game_utils

BASE_URL = "https://less.palcka.si"
START_POS = "bb4/bb4/6/6/4ww/4ww"
START_POS = "bb4/bb4/6/5w/4w0/4ww"
#START_POS = "ww4/w1w3/6/6/bb4/bb4"
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
    
    

current_player = "w" 

print(functions.convert_to_url(b10_board,lbp,BASE_URL))

cost_of_moves = functions.cost_of_moves(lbp,b10_board,"w")
for i,v in cost_of_moves:
    print(pars.from_arry_notation(i),v)
    

while 1: #? game
    move_power = 3     
    while 1: #? player move
        while 1: #? good input
            print(functions.convert_to_url(b10_board,lbp,BASE_URL))
            print(f"INFO | Move power left: {move_power}")
            color_legal_cost = functions.cost_of_moves(lbp,b10_board,current_player)
            #print("ebug",len(color_legal_cost),color_legal_cost)
            
            print("ebug",len(color_legal_cost),)
            for i,v in color_legal_cost:
                print(pars.from_arry_notation(i),v)
            user_move = input(f"INFO | {current_player} | Enter move in coordnite notation a1a3 >")
            succes,move_ary = pars.from_coord_notation(user_move)
            print(move_ary)
            if not succes:
                print(move_ary)
                continue
            
            cost = functions.singe_move_cost(color_legal_cost,move_ary)
            print(cost)
            if cost == 0:
                print("INFO | Not legal")
                continue
            if cost > move_power:
                print("INFO | You dont have enought Move Power™")
                continue
            
            break
        
        print("# move ")
        lbp = functions.push_move(lbp,move_ary)
        print("Move done")
        
        checkForWin,color = game_utils.is_win(lbp)
        
        if checkForWin:
            if color == 1:
                print("WHite win")
            elif color == -1:
                print("Black Win")
            else:
                raise ValueError("Not 1 nor -1 ??")
            
            exit()

    
        move_power = move_power -  cost
        
        if move_power == 0:
            break
        
        print("move finished")
        
    print("Player finish")
    current_player = swap_players(current_player)
