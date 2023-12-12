
def process_input():
	inputs = [(i.rstrip()) for i in open("input.txt", "r")]
	route = [0 if i == 'L' else 1 for i in inputs[0]]
	maps = {}
	for i in range(2,len(inputs)):
		temp = inputs[i]
		maps[temp[:3]] = [temp[7:10],temp[12:15]]
	return route,maps

def solve_firstpart(route,maps,start = 'AAA'):
	total_steps = 0 
	route_index = 0 
	flag = True
	while flag:
		if route_index == len(route):
			route_index = 0 
		indexx = route[route_index]
		route_index += 1 
		total_steps += 1 
		choice = maps[start][indexx]
		if choice[-1] == 'Z' : 
			flag = False
		start = choice

	return total_steps


def find_lcm_array(arr):
    def find_lcm(x, y):
        return x * y // math.gcd(x, y)

    import math
    lcm_result = arr[0]
    for i in range(1, len(arr)):
        lcm_result = find_lcm(lcm_result, arr[i])

    return lcm_result


def solve_secondpart(route,maps):
	import time
	total_steps = 0 
	route_index = 0 
	all_steps = []
	start = [i for i in maps if i[-1] == 'A']
	for i in start:
		all_steps.append(solve_firstpart(route,maps,start = i))
	return find_lcm_array(all_steps)
	
	
	
route,maps = process_input()
print(solve_secondpart(route,maps))

















