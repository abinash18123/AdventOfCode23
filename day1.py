def solve(arr):
	global dic 
	dic = {}
	total = 0
	
	for i in range(len(arr)):
		num = ''
		indices = []
		for j in range(len(arr[i])):
			curr = arr[i][j]
			if curr.isdigit():
				num += curr 
				indices.append([i,j])
			else:
				if len(num) != 0:
					findNum(num,indices,arr)
					num = ''
					indices = []
		if len(num) !=0:
			findNum(num,indices,arr)

	for i in dic:
		if len(dic[i]) == 2:
			total += int(dic[i][0])*int(dic[i][1])
	return total
	
def findNum(num,indices,arr):
	mapper = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
	for i in indices:
		x = i[0]
		y = i[1]
		for j in mapper:
			newx = x + j[0]
			newy = y + j[1]
			booll = validCheck(arr,newx,newy)
			if booll:
				coor = (newx,newy)
				if coor in dic: 
					dic[coor].append(num)
				else: 
					dic[coor]=[num]
				break
		if booll: 
			break
			
			
def validCheck(arr,newx,newy):
	if 0 <= newx <= len(arr)-1 and 0 <= newy <= len(arr[0]) -1:
		newnum =  arr[newx][newy]
		if not newnum.isdigit() and newnum == '*':
			return True
	return False
				
print(solve([(i.rstrip()) for i in open("input.txt", "r")]))




