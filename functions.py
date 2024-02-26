def convert_to_url(b10_board,lbp,base_url):
    b10_board_list = list(map(str,b10_board))
    b10_board_list = ",".join(b10_board_list)

    return base_url + f"/image?nums={b10_board_list}&lbp={lbp}"

def is_valid_cords(x:int,y:int,max_x=5,max_y=5) -> bool:
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

def convert_to_binary_len12(dec:int) -> str:
    b = bin(dec)
    b = str(b)[2::]
    added_0 = (12 - len(b)) * "0"
    b = added_0 + b
    return b

def filter_moves_out_of_bound(arry_of_moves):
    new_moves = []
    for move in arry_of_moves:
        #move = [x1, y1,x2, y2]
        
        m1,m2 = move
        
        if is_valid_cords(m1[0], m1[1]) and is_valid_cords(m2[0], m2[1]):
            new_moves.append(move)    
    
    return new_moves

    
def moves_in_tile(x,y):
    offsets = [
        # 1. row
        [0,-1,0,0],
        [1,-1,1,0],
        # 2.
        [-1,0,0,0],
        [0,0,1,0],
        [1,0,2,0],
        # 3.
        [0,0,0,1],
        [1,0,1,1],
        # 4.
        [-1,1,0,1],
        [0,1,1,1],
        [1,1,2,1],
        # 5.
        [0,1,0,2],
        [1,1,1,2],
    ]
    
    returning_offsets = offsets[:]
    for i in range(len(returning_offsets)):
    
        returning_offsets[i][0] += x
        returning_offsets[i][2] += x
        
        returning_offsets[i][1] += y
        returning_offsets[i][3] += y
        
        '''for z in range(len(returning_offsets[i][j])):
                if z % 2 == 0: # x
                    returning_offsets[i][j][z] = returning_offsets[i][j][z] + x
                else:
                    returning_offsets[i][j][z] = returning_offsets[i][j][z] + y '''
    return returning_offsets


def moves_that_cost_in_tile(arry_of_corrds,b10_num):
    binary_num = convert_to_binary_len12(b10_num)

    good_connections = []
    
    for i in range(len(arry_of_corrds)):
        current_bin = binary_num[i]
        current_connections = arry_of_corrds[i]
        if int(current_bin) == 1:
            good_connections.append(current_connections)
            
    return good_connections
    
def every_absolute_moves():
    moves = []
    for x in range(0,6,2):
        for y in range(0,6,2):
            ot_moves = moves_in_tile(x,y)  # one tile move
            filter_out_of_boud = filter_moves_out_of_bound(ot_moves)
            moves = moves + filter_out_of_boud
            
    return moves
    
def moves_that_cost_all(arry_of_nums):
    all_moves = []
    
    for i in range(len(arry_of_nums)):
        b10_num = arry_of_nums[i]
        #? b10_num = num given in main    

        x = int(i/3)
        y = int(i%3)
        
        
        moves = moves_in_tile(x,y)
        moves = moves_that_cost_in_tile(moves,b10_num)

        all_moves = all_moves + moves
        
    return all_moves  
        
def start_end_flip(moves:list)-> list:
    # [x,y,a,b] -> [a,b,x,y]
    
    return [moves[2],moves[3],moves[0],moves[1]]
    
        
def reformate_wall_moves(normal_wall_moves):
    moves = []
    new_moves = []
    
    
    
    for i in range(len(normal_wall_moves)):
        m = normal_wall_moves[i]
        m1,m2 = m[0:2],m[2:4]
        if not ([m,1] in new_moves or [start_end_flip(m),1] in new_moves):
            new_moves.append([m,1])
        else:
            new_moves.remove([m,1])
            new_moves.append([m,2])
    
    return new_moves

def every_one_step_move(x:int,y:int):
    """every move from x,y
    Args:
        x (int): x
        y (int): y
    Returns:
        list [ [x,y,nx,ny] ]:
    """
    moves = []
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx == dy == 0:
                continue
            
            nx = x + dx
            ny = x + dy 
            
            if is_valid_cords(nx,ny):
                moves.append([x,y,nx,ny])
    return moves

