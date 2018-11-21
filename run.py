import numpy as np 


class Run():

    def __init__(self, game_map, position):
        self.map = game_map
        self.count = 1 
        self.dimension = game_map.dimension  
        self.current_position = self.set_current(position) 
        self.count += 1
        self.path = ""


    def set_current(self, coords):
        self.map.grid[coords[0], coords[1]] = self.count
        self.current_position = coords 
        return coords 



    def move(self, direction):
        if direction in 'U D L R'.split():
            return self.move_cartesian(direction)
        if direction in 'UR UL DR DL'.split():
            return self.move_diagonal(direction)
        else: 
            raise Exception('Invalid direction provided')


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
                    self.path = ' '.join([self.path, direction])
                    return self.current_position 

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
                    self.path = ' '.join([self.path, direction])                    
                    return self.current_position 

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
                    self.path = ' '.join([self.path, direction])                                        
                    return self.current_position 

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
                    self.path = ' '.join([self.path, direction]) 
                    return self.current_position 

                else: 
                    return False 
            else: 
                return False 

        else: 
            raise Exception("invalid cartesian direction")


    def move_diagonal(self, direction):
        x, y = self.current_position

        #  Directions: 
        #       UR 
        #       UL
        #       DR
        #       DL

        if direction == 'UL':
            x1 = x - 1 
            x2 = x - 2 
            y1 = y - 1
            y2 = y - 2

            if all(0 <= x < self.dimension for x in [x1, x2, y1, y2]):
                if all(self.map.can_i_move_here(coords) for coords in [[x1, y1], [x2, y2]]):
                    self.set_current([x1, y1])
                    self.set_current([x2, y2])
                    self.count += 1
                    self.path = ' '.join([self.path, direction]) 
                    return self.current_position 

                else:
                    return False 
            else: 
                return False 

        if direction == 'UR':
            x1 = x + 1 
            x2 = x + 2 
            y1 = y - 1
            y2 = y - 2

            if all(0 <= x < self.dimension for x in [x1, x2, y1, y2]):
                if all(self.map.can_i_move_here(coords) for coords in [[x1, y1], [x2, y2]]):
                    self.set_current([x1, y1])
                    self.set_current([x2, y2])
                    self.count += 1
                    self.path = ' '.join([self.path, direction]) 
                    return self.current_position 

                else:
                    return False 
            else: 
                return False 

        if direction == 'DR':
            x1 = x + 1 
            x2 = x + 2 
            y1 = y + 1
            y2 = y + 2

            if all(0 <= x < self.dimension for x in [x1, x2, y1, y2]):
                if all(self.map.can_i_move_here(coords) for coords in [[x1, y1], [x2, y2]]):
                    self.set_current([x1, y1])
                    self.set_current([x2, y2])
                    self.count += 1
                    self.path = ' '.join([self.path, direction]) 
                    return self.current_position 
                    
                else:
                    return False 
            else: 
                return False 


        if direction == 'DL':
            x1 = x - 1 
            x2 = x - 2 
            y1 = y + 1
            y2 = y + 2

            if all(0 <= x < self.dimension for x in [x1, x2, y1, y2]):
                if all(self.map.can_i_move_here(coords) for coords in [[x1, y1], [x2, y2]]):
                    self.set_current([x1, y1])
                    self.set_current([x2, y2])
                    self.count += 1
                    self.path = ' '.join([self.path, direction]) 
                    return self.current_position 
                    
                else:
                    return False 
            else: 
                return False 



        else: 
            raise Exception('Invalid diagonal direction')