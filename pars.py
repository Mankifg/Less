import functions

files="abcdef"

def parse_move(coord_not):
    if len(coord_not) != 4:
        return False,"Len != 4"
    
    x1,y1,x2,y2 = coord_not
    
    if not (x1 in files and x2 in files):
        return False,"Out of bounds"
 
   
    x1 =  files.index(x1)
    x2 =  files.index(x2)
    
    y1,y2 = int(y1),int(y2)
    
    if not (functions.is_valid_cords(x1, y1) and functions.is_valid_cords(x2, y2) and \
        functions.is_valid_cords(x2, y2)):
            return False,"Coords not good"
        
        
    return True,[x1,y1,x2,y2]