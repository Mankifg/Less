import functions

UP_LEFT = "w"
BOTTOM_RIGHT = "b"
START_POS = "bb4/bb4/6/6/4ww/4ww"


def is_win(lbp):
    if lbp[0:2] + lbp[4:6] == UP_LEFT*4:
        return True,1
    if lbp[-2:] + lbp[-6:-4] == BOTTOM_RIGHT*4:
        return True,-1
    return False,0
    
        