def process_input():
	inputs = [(i.rstrip()).split(' ') for i in open("input.txt", "r")]
	inputs = [[int(i) for i in j] for j in inputs]
	return inputs

def process_array(arr):
	flag = True
	firstvals = []
	while flag:
		temp = []
		for i in range(1,len(arr)):
			temp.append(arr[i] - arr[i-1])
		firstvals.append(arr[0])
		if len(set(temp)) == 1 and temp[0] == 0:
			flag = False 
		arr = temp
	firstvals = firstvals[::-1]
	coun = firstvals[0]
	for i in range(1,len(firstvals)):
		coun = firstvals[i] - coun
	return coun

inputs = process_input()
total = sum([process_array(i) for i in inputs])
print(total)


