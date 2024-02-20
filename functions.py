def is_valid_cords(x,y,max_x=5,max_y=5):
    return (x >= 0 and x <= max_x) and (y >= 0 and y <= max_y)
        
def what_is_here(board,x,y):
    return board[y][x]

def blockiy_positon(lbp):
    for i in range(2, 10):
        lbp = lbp.replace(str(i), "0" * i)

    lbp = lbp.split("/")

    # w white, b black, 0 empty

    arry = []
    for x in range(0, int(len(lbp)), 2):
        a2 = []

        upper_row = lbp[x]
        lower_row = lbp[x + 1]

        len_row = len(upper_row)

        for y in range(0, len_row, 2):

            block = [[upper_row[y], upper_row[y + 1]], [lower_row[y], lower_row[y + 1]]]

            lbp[x] = lbp[x][:-2]
            lbp[x + 1] = lbp[x + 1][:-2]

            a2.append(block)

        arry.append(a2)

    return arry

def boardify(lbp):
    for i in range(2, 10):
        lbp = lbp.replace(str(i), "0" * i)

    lbp = lbp.split("/")
    for i in range(len(lbp)):
        lbp[i] = list(lbp[i])

    return lbp

def binary_by_12(dec):
    b = bin(dec)
    b = str(b)[2::]
    added_0 = (12 - len(b)) * "0"
    b = added_0 + b
    return b

def filter_moves_out_of_bound(arry_of_moves):
    new_moves = []
    
    for move in arry_of_moves:
        #move = [[x1, y1], [x2, y2]]
        
        m1,m2 = move
        
        passing = is_valid_cords(m1[0], m1[1]) and is_valid_cords(m2[0], m2[1]) 
        
        if passing:
            new_moves.append(move)    
    return new_moves

    
def one_tile_moves_at(x,y):
    offsets = [
        # 1. row
        [[0,-1],[0,0]],
        [[1,-1],[1,0]],
        # 2.
        [[-1,0],[0,0]],
        [[0,0],[1,0]],
        [[1,0],[2,0]],
        # 3.
        [[0,0],[0,1]],
        [[1,0],[1,1]],
        # 4.
        [[-1,1],[0,1]],
        [[0,1],[1,1]],
        [[1,1],[2,1]],
        # 5.
        [[0,1],[0,2]],
        [[1,1],[1,2]],
    ]
    
    returning_offsets = offsets[:]
    
    for i in range(len(returning_offsets)):
        for j in range(len(returning_offsets[i])):
            for z in range(len(returning_offsets[i][j])):
                
                if z % 2 == 0: # x
                    returning_offsets[i][j][z] = returning_offsets[i][j][z] + x
                else:
                    returning_offsets[i][j][z] = returning_offsets[i][j][z] + y 

    return returning_offsets


def filter_block_moves(arry_of_corrds,base_10_num):
    binary = binary_by_12(base_10_num)

    good_connections = []
    
    for i in range(len(arry_of_corrds)):
        current_bin = binary[i]
        current_connections = arry_of_corrds[i]
        if int(current_bin) == 1:
            good_connections.append(current_connections)
            
    
    return good_connections
    
def all_absolute_moves():
    moves = []
    for x in range(0,6,2):
        for y in range(0,6,2):
            ot_moves = one_tile_moves_at(x,y)  # one tile move
            filter_out_of_boud = filter_moves_out_of_bound(ot_moves)
            moves = moves + filter_out_of_boud
            
            
    return moves
    ... 

def moves_that_cost(arry_of_nums):
    all_moves = []
    
    for i in range(len(arry_of_nums)):
        b10_num = arry_of_nums[i]
        #? b10_num = num given in main    

        x = int(i/3)
        y = int(i%3)
        
        moves = one_tile_moves_at(x,y)
        moves = filter_block_moves(moves,b10_num)

        all_moves = all_moves + moves
        
    return all_moves  
        
def reformate_wall_moves(normal_wall_moves):
    moves = []
    identical = []
    for i in range(len(normal_wall_moves)):
        m = normal_wall_moves[i]
        m1,m2 = m
        if not ([m1,m2] in identical or [m2,m1] in identical):
            identical.append([m1,m2,1])
        else:
            ...
    
    for move in identical:
        ...

    
    

    
    