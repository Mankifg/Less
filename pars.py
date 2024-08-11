files="abcdef"

def parse_move(coord_not):
    if len(coord_not) != 4:
        return False,"Len != 4"
    
    
    return [
        files.index(coord_not[0]),
        6-int(coord_not[1]),
        files.index(coord_not[2]),
        6-int(coord_not[3]),
    ]
    
    