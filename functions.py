def is_valid_cords(x,y,max_x=5,max_y=5):
    return (x >= 0 and x <= max_x) and (y >= 0 and y <= max_y)
        
def what_is_here(board,xy):
    x,y = xy
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


def all_off_sets_for_top_left(x,y):
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


def filter_one_block_tiles(arry_of_corrds,base_10_num):
    binary = binary_by_12(base_10_num)

    good_connections = []
    
    for i in range(len(arry_of_corrds)):
        current_bin = binary[i]
        current_connections = arry_of_corrds[i]
        
        if current_bin == 1:
            good_connections.append(current_connections)
            
    
    return good_connections
    
    

x,y = 0,0

stuff = all_off_sets_for_top_left(x,y)

print(stuff)