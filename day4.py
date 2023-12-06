def solve(arr,dic): 
	for p in range(len(arr)):dic.update({j: dic[j] + dic[p] for j in range(p + 1, p + 1 + (len(set([int(i)for i in arr[p].split(':')[-1].split('|')[0].split(' ') if i.isdigit()]).intersection(set([int(i)for i in arr[p].split(':')[-1].split('|')[1].split(' ') if i.isdigit()])))))})
	return sum(dic.values())
print(solve([(i.rstrip()) for i in open("input.txt", "r")],{i: 1 for i in range(len([(i.rstrip()) for i in open("input.txt", "r")]))}))