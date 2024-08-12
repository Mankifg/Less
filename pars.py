import functions

FILES="abcdef"

def from_coord_notation(coord_not):
    if len(coord_not) != 4:
        return False,"Len != 4"
    
    x1,y1,x2,y2 = coord_not
    
    if not (x1 in FILES and x2 in FILES):
        return False,"Out of bounds"
 
    x1 =  FILES.index(x1)
    x2 =  FILES.index(x2)
    
    y1,y2 = int(y1),int(y2)
    
    y1 = 6-y1
    y2 = 6-y2
    
    if not(functions.is_valid_cords(x1, y1) and functions.is_valid_cords(x2, y2)):
        print(x1,y1,"->",x2,y2)
        return False,"Coords not good" 
        
    return True,[x1,y1,x2,y2]

def from_arry_notation(arry):
    if len(arry) != 4:
        return False,"Len != 4"
    
    x1,y1,x2,y2 = arry 

    x1 = FILES[x1]
    x2 = FILES[x2]
    y1 = 6-y1
    y2 = 6-y2
      
    return True,f"{x1}{y1}{x2}{y2}"

