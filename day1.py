def summ(n):
	flag = 0 
	finalNum = ''
	dic = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

	timline = {}
	for k in dic.keys():
		for num in range(0,len(n) - len(k) + 1):
			number = n[num:num+len(k)]
			if number == k:
				timline[num] = dic[k]

	for j in range(len(n)):
		if n[j].isdigit(): 
			timline[j] = n[j]
	indexes = sorted(timline)
	return int(timline[indexes[0]] + timline[indexes[-1]])
	
print(sum([summ(i.rstrip()) for i in open("input.txt", "r")]))