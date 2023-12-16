def process_input():
	def rotate_clockwise(matrix):
	    transposed_matrix = list(map(list, zip(*matrix)))
	    rotated_matrix = [list(reversed(row)) for row in transposed_matrix]
	    rotated_matrix = [i[::-1] for i in rotated_matrix]
	    return rotated_matrix
	import numpy as np
	inputs = [(i.rstrip()).split(' ') for i in open("input.txt", "r")]
	matrix = []
	for i in inputs:
		matrix.append([j for j in i[0]])
	matrix = np.array(matrix)
	rotated = rotate_clockwise(matrix)
	matrix = np.array(matrix)
	rotated = np.array(rotated)
	return matrix,rotated

def find_rc(matrix,rotated):
	rr,cc = [],[]
	for p,i in enumerate(matrix):
		if len(set(i)) == 1 and i[0] == '.':
			rr.append(p)
	for p,i in enumerate(rotated):
		if len(set(i)) == 1 and i[0] == '.':
			cc.append(p)
	return rr,cc

def find_indexes(rr,cc,martix):
	r = 0    
	indexes = []
	for i in range(len(matrix)):
		c = 0
		for j in range(len(matrix[0])):
			if martix[i][j] == '#': indexes.append([r,c])
			if j in cc: c +=1000000
			else: c +=1   
		if i in rr: r += 1000000
		else: r += 1 

	return indexes

def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

def find_sum(points):
	total = 0
	for i in range(len(points)):
	    for j in range(i + 1, len(points)):
	        distance = manhattan_distance(points[i], points[j])
	        total += distance
	print(total)

matrix,rotated = process_input()
rr,cc = find_rc(matrix,rotated)
indexes = find_indexes(rr,cc,matrix)
find_sum = find_sum(indexes)
