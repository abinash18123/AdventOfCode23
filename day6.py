inputs = [(i.rstrip()) for i in open("input.txt", "r")]
time = [int(i) for i in inputs[0].split(' ') if i.isdigit()]
distance = [int(i) for i in inputs[1].split(' ') if i.isdigit()]

new_time = ''
new_distance = ''

for i in range(len(time)):
	new_time += str(time[i])
	new_distance += str(distance[i])
new_time = int(new_time)
new_distance = int(new_distance)

import math
def solve(time,distance):
	out = 1
	# for i in range(len(time)):
	# 	x_time = time[i]
	# 	x_distance = distance[i]
	x_time = time 
	x_distance = distance
	minn = math.ceil(x_distance/x_time)
	for k in range(minn,x_time):
		if (x_time - k)*k > x_distance:
			minn = k 
			break
	maxx = x_time-minn
	for k in range(x_time-minn,0,-1):
		if (x_time - k)*k > x_distance:
			maxx = k 
			break
	out *= maxx-minn+1
	print(out)
solve(new_time,new_distance)











