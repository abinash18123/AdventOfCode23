def summ(n):
	flag = 0 
	finalNum = ''
	nums = ['one','two','three','four','five','six','seven','eight','nine']
	dic = {'one':str(1),'two':str(2),'three':str(3),'four':str(4),'five':str(5),'six':str(6),'seven':str(7),'eight':str(8),'nine':str(9)}

	timline = {}
	for k in nums:
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