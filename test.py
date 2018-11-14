import numpy as numpy
from map import Map 



m = Map(5)
m.set_current(0, 0)
m.print_board()



def move_cartesian(self, direction):
    x, y = self.current_position

    if direction == 'U':
        y1 = y - 1
        y2 = y - 2
        y3 = y - 3
        if all(0 <= y < self.dimension for y in [y1, y2, y3]): 
            if all(self.map.can_i_move_here([x, y]) for y in [y1, y2, y3]):
                self.set_current([x, y1])
                self.set_current([x, y2])
                self.set_current([x, y3])
                self.count += 1
                return True 

            else: 
                return False 
        else: 
            return False 
    

    if direction == 'D':
        y1 = y + 1
        y2 = y + 2
        y3 = y + 3
        if all(0 <= y < self.dimension for y in [y1, y2, y3]): 
            if all(self.map.can_i_move_here([x, y]) for y in [y1, y2, y3]):
                self.set_current([x, y1])
                self.set_current([x, y2])
                self.set_current([x, y3])
                self.count += 1
                return True 

            else: 
                return False 
        else: 
            return False 


    if direction == 'R':
        x1 = x + 1
        x2 = x + 2
        x3 = x + 3
        if all(0 <= x < self.dimension for x in [x1, x2, x3]): 
            if all(self.map.can_i_move_here([x, y]) for x in [x1, x2, x3]):
                self.set_current([x1, y])
                self.set_current([x2, y])
                self.set_current([x3, y])
                self.count += 1
                return True 

            else: 
                return False 
        else: 
            return False 


    if direction == 'L':
        x1 = x - 1
        x2 = x - 2
        x3 = x - 3
        if all(0 <= x < self.dimension for x in [x1, x2, x3]): 
            if all(self.map.can_i_move_here([x, y]) for x in [x1, x2, x3]):
                self.set_current([x1, y])
                self.set_current([x2, y])
                self.set_current([x3, y])
                self.count += 1
                return True 

            else: 
                return False 
        else: 
            return False 
##

   def move_unit(self, direction):
        x, y = self.current_position 
        
        self.move_cartesian()


        if direction == 'L':
            col = col-1
            if 0 <= col < dimension:
                if self.can_i_move_here([col, row]):
                    self.set_current(col, row)
                    return True 
                else:
                    return False 
            else: 
                return False 
            
        if direction == 'R':
            col = col+1 
            if 0 <= col < dimension: 
                if self.can_i_move_here([col, row]):
                    return [row, col]
                else:
                    return False 

            else: 
                return False 
        
        if direction == 'D':
            row = row + 1
            if 0 <= row < dimension:
                if self.can_i_move_here([col, row]):
                    return [row, col]
                else:
                    return False 
            else:
                return False 
                   
        if direction == 'U':
            row = row - 1
            if 0 <= row < dimension: 
                return [row, col]
            else:
                return False 
            
    #     if direction == 'UR':
    #         row = row - 1 
    #         col = col - 1
    #         if (0 < row < dimension-1) and (0 < col < dimension-1):
    #           pass 

                
