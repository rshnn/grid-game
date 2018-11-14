import numpy as np 


class Map():
	"""
		5x5 square
		Starting at any point, fill in 0s with 1s
		Cartesian move = 3 spaces 
		Diagonal move = 2 spaces
	"""

	def __init__(self, dimension):
		self.grid = np.zeros([dimension, dimension])
		self.current_position = [np.nan, np.nan]


	def set_current(self, row, col):
		self.current_position = [row, col]
		self.grid[self.current_position] = 1


	def print_board(self):
		print(self.grid)


	def can_i_move_here(self, coords):
	    if self.grid[coords[0], coords[1]] > 0:
	        return False
	    else: 
	        return True 


	# def move_unit(direction, position, grid):
	#     col, row = self.current_position 
	    
	#     if direction == 'L':
	#         col = col-1
	#         if 0 <= col < dimension: 
	#             return [row, col]
	#         else: 
	#             return False 
	        
	#     if direction == 'R':
	#         col = col+1 
	#         if 0 <= col < dimension: 
	#             return [row, col]
	#         else: 
	#             return False 
	    
	#     if direction == 'D':
	#         row = row + 1
	#         if 0 <= row < dimension:
	#             return [row, col]
	#         else:
	#             return False 
	        
	        
	#     if direction == 'U':
	#         row = row - 1
	#         if 0 <= row < dimension: 
	#             return [row, col]
	#         else:
	#             return False 
	        
	#     if direction == 'UR':
	#         row = row - 1 
	#         col = col - 1
	#         if (0 < row < dimension-1) and (0 < col < dimension-1):
	#         	pass 

	            
	   	