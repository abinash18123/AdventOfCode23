# part 1

def process_input():
	inputs = [(i.rstrip()).split(',') for i in open("input.txt", "r")]
	return inputs[0]
def calChar(code):
	output = 0 
	for i in code:
		output += ord(i)
		output *= 17
		output = output%256
	return output

def partOne():
	codes = process_input()
	total = 0
	for i in codes:
		total += calChar(i)
	print(total)

partOne()


#part 2

def process_input():
	inputs = [(i.rstrip()).split(',') for i in open("input.txt", "r")]
	output = []
	for char in inputs[0]:
		if '-' in char:
			label = char.split('-')[0]
			output.append([calChar(label),label,'-',None])
		else:
			label = char.split('=')[0]
			val = int(char.split('=')[-1])
			output.append([calChar(label),label,'=',val])
	return output

def calChar(code):
	output = 0 
	for i in code:
		output += ord(i)
		output *= 17
		output = output%256
	return output

def logic(codes):
	boxes = {}
	for val in codes:
		boxNum,boxLabel,boxOperator,lens = val[0],val[1],val[2],val[3]
		if boxOperator == '=':
			if boxNum in boxes:
				data = boxes[boxNum]
				inBox = False
				for i in range(len(data)):
					if data[i][0] == boxLabel:
						boxes[boxNum][i][-1] = lens 
						inBox = True
						break
				if not inBox:
					boxes[boxNum].append([boxLabel,lens])
			else:
				boxes[boxNum] = [[boxLabel,lens]]

		elif boxOperator == '-':
			if boxNum in boxes:
				data = boxes[boxNum]
				index = -1
				for i in range(len(data)):
					if data[i][0] == boxLabel:
						index = i 
						break
				if index != -1:
					boxes[boxNum].pop(index)
	for i in list(boxes):
	    if len(boxes[i]) == 0:
	        del boxes[i]
	return boxes

def summ(dic):
	total = 0 
	for key in dic:
		var1 = key + 1
		for slot in range(len(dic[key])):
			var2 = slot + 1 
			var3 = dic[key][slot][-1]
			total += var1 * var2 * var3
	return total


def partTwo():
	codes = process_input()
	dic = logic(codes)
	total = summ(dic)
	print(total)

partTwo()

