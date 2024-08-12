def moves_in_tile(x, y):
    print("running",x,y)
    offsets = [
        # 1. row
        [0, -1, 0, 0],
        [1, -1, 1, 0],
        # 2.
        [-1, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 2, 0],
        # 3.
        [0, 0, 0, 1],
        [1, 0, 1, 1],
        # 4.
        [-1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 2, 1],
        # 5.
        [0, 1, 0, 2],
        [1, 1, 1, 2],
    ]

    returning_offsets = offsets[:]
    for i in range(len(returning_offsets)):

        returning_offsets[i][0] += x
        returning_offsets[i][2] += x

        returning_offsets[i][1] += y
        returning_offsets[i][3] += y
        """for z in range(len(returning_offsets[i][j])):
                if z % 2 == 0: # x
                    returning_offsets[i][j][z] = returning_offsets[i][j][z] + x
                else:
                    returning_offsets[i][j][z] = returning_offsets[i][j][z] + y """
    return returning_offsets


print(moves_in_tile(0,0))