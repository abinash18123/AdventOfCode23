#part 1

def process_input():
	import numpy as np
	maps = [(i.rstrip().split(' ')) for i in open("input.txt", "r") if len((i.rstrip().split(' '))) != 0 and (i.rstrip().split(' '))!=['']]
	out = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']
	indexes = []
	for i in out:
		for j in range(len(maps)):
			if i in maps[j]:
				indexes.append(j)
				break
	dic = {}
	dic['seeds'] = np.int64(maps[0][1:])
	for i in range(6):
		dic[out[i]] = np.int64(maps[indexes[i]+1:indexes[i+1]])
	dic[out[6]] = np.int64(maps[indexes[6]+1:])

	return dic

def process_seed(num, dic):
	seed = num
	soil = process_range(dic['seed-to-soil'],seed)
	fertilizer = process_range(dic['soil-to-fertilizer'],soil)
	water = process_range(dic['fertilizer-to-water'],fertilizer)
	light = process_range(dic['water-to-light'],water)
	temperature = process_range(dic['light-to-temperature'],light)
	humidity = process_range(dic['temperature-to-humidity'],temperature)
	location = process_range(dic['humidity-to-location'],humidity)

	return location

def process_range(ranges,val):
	out = val 
	for var in ranges:
		mapID = var[0]
		ownID = var[1]
		diff = var[2]
		if  ownID <= out <= ( ownID + diff - 1 ):
			steps = out - ownID 
			out = mapID + steps 
			break 
	return out


def solve():
	dic = process_input()
	minn = 1e10
	for i in dic['seeds']:
		val = process_seed(i,dic)
		if val < minn :
			minn = val 
	print(minn)

solve()






#part 2

def process_input():
	import numpy as np
	maps = [(i.rstrip().split(' ')) for i in open("input.txt", "r") if len((i.rstrip().split(' '))) != 0 and (i.rstrip().split(' '))!=['']]
	out = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']
	indexes = []
	for i in out:
		for j in range(len(maps)):
			if i in maps[j]:
				indexes.append(j)
				break
	dic = {}
	dic['seeds'] = np.int64(maps[0][1:])
	for i in range(6):
		dic[out[i]] = np.int64(maps[indexes[i]+1:indexes[i+1]])
	dic[out[6]] = np.int64(maps[indexes[6]+1:])

	return dic

def process_ranges(dic):
	coun = 0
	for i in dic:
		store = {}
		if coun >0:
			temp = dic[i]
			for index in temp:
				start = index[1]
				end = index[-1] + index[1] - 1 
				store[(start,end)] = index[0] - index[1]
			store = dict(sorted(store.items(), key=lambda x: int(x[0][0])))
			dic[i] = store 
			store = {}
		coun +=1
	return dic


def process_seed_range(dic):
	seeds_range = []
	seeds = dic['seeds']
	for i in range(0,len(seeds),2):
		seeds_range.append([seeds[i],seeds[i] + seeds[i+1] -1])
	return seeds_range


def process_seed(lower,upper, dic): 

	soil = process_range(dic['seed-to-soil'],[[lower,upper]])
	fertilizer = process_range(dic['soil-to-fertilizer'],soil)
	water = process_range(dic['fertilizer-to-water'],fertilizer)
	light = process_range(dic['water-to-light'],water)
	temperature = process_range(dic['light-to-temperature'],light)
	humidity = process_range(dic['temperature-to-humidity'],temperature)
	location = process_range(dic['humidity-to-location'],humidity)

	out = min([i[0] for i in location])
	return out

def process_range(mapto,mapfor):
	# print(mapto,mapfor,'mapps')
	total_range = []
	keys = list(mapto.keys())
	values = list(mapto.values())
	range_ = []
	for x in mapfor:
		flag3 = False
		# print(x,'x')
		start = x[0]
		end = x[-1] 
		if start < keys[0][0]:
			range_.append([start,keys[0][0] - 1])
			start = keys[0][0] 
		while start <= end and flag3 == False:
			cc = False
			if start == end:
				for i in range(len(keys)):
					upper_bound = keys[i][1]
					lower_bound = keys[i][0]
					if lower_bound <= start <= upper_bound:
						cc = True
						range_.append([start + values[i]])
				if cc == False:
					range_.append([start])
				start = end + 1

			else:
				for i in range(len(keys)):
					flag  = False
					upper_bound = keys[i][1]
					lower_bound = keys[i][0]

					if lower_bound <= start <= upper_bound:
						flag = True
						if end > upper_bound:
							range_.append([start + values[i],upper_bound + values[i]])
							start = upper_bound + 1 
						else:
							range_.append([start + values[i],end + values[i]])
							start = end 
							flag3 = True
							break
				if flag == False:
					flag_2 = False
					for j in range(len(keys)):
						if keys[j][-1] > start :
							range_.append([start,keys[j][0] - 1])
							start = keys[j][0] 
							flag_2 = True 
							break
					if flag_2 == False:
						range_.append([start,end])
						start = end 
						flag3 = True
						break	

	return range_


def solve():
	dic = process_input()
	seeds_range = process_seed_range(dic)
	new_dic = process_ranges(dic)
	minn = 1e10
	for r in seeds_range:
		lower = r[0]
		upper = r[1]
		val = process_seed(lower,upper,dic)
		if val < minn :
			minn = val 
	print(minn)

solve()









