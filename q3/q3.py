# Assumption: Input is valid and complete
# General process goes as follows: 
# Construct an array representation of the locations and where they point to
# Iterate through the list, and for each location, trace the path, marking each location 
# with a -1 as we go
# Runtime is O(n): O(n) to construct the array, and when counting cycles we check each location at most twice

# INPUT FILE SHOULD BE NAMED 'example.txt' AND BE IN SAME DIRECTORY
# OUTPUT SENT TO FILE 'output.txt'

import sys

# class Puzzle is initialized with the list of locations and where they point to
class Puzzle:
	def __init__(self, locations, num_locations):
   		self.locations = locations
		self.num_locations = num_locations
   		self.num_cycles = 0

    # given array where index is location number and values are where locations point to,
	# returns the number of cycles in the array
	def countCycles(self):
		for i in range(self.num_locations):
			if self.tracePath(i):
				self.num_cycles += 1
		return self.num_cycles

	# starting at location i, determine if it is part of a cycle
	def tracePath(self, i):
		start_val = i
		while self.locations[i] != -1:
			# check if we have found a cycle
			old_i = i
			i = self.locations[i]
			if start_val == i:
				return True

			self.locations[old_i] = -1
		return False

# Read input, containing number of locations and where each location points to
locations = []
with open('example.txt','r') as f:
    for line in f:
        locations.append(int(line))
num_locations = locations.pop(0)

# create Puzzle instance, and count the number of cycles
puzzle = Puzzle(locations, num_locations)
sys.stdout = open('output.txt', 'w')
print puzzle.countCycles()
