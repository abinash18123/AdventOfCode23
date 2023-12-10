
def process_input():
	inputs = [(i.rstrip()) for i in open("input.txt", "r")]
	cards, vals = [(i.split(' ')[0]) for i in inputs], [int(i.split(' ')[1]) for i in inputs]
	card_val_dic = {}

	for i in range(len(cards)):
		card_val_dic[cards[i]] = vals[i]
	return cards,vals,card_val_dic

order = 'AKQT98765432J'
card_order = [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]]

def custom_sort(item):
    return tuple(order.index(char) for char in item)

def check_J(dic,order):
	sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
	return sorted_dict

def solve(card_order,cards):
	from collections import Counter
	ALL_CARDS = []
	for j in card_order:
		sub_cards = []
		for i in cards:
			sorted_dic = check_J(Counter(i),order)
			if 'J' in sorted_dic and len(sorted_dic)>1:
				val = sorted_dic['J']
				del sorted_dic['J']
				left = list(sorted_dic.keys())
				sorted_dic[left[0]] += val 

			temp = list(sorted_dic.values())
			temp.sort(reverse = True)
			if temp == j:
				sub_cards.append(i)
		if len(sub_cards)!= 0:
			sorted_arr = sorted(sub_cards, key=custom_sort)
			ALL_CARDS.extend(sorted_arr)

	ALL_CARDS = ALL_CARDS[::-1]
	total = 0 
	for i,j in enumerate(ALL_CARDS):
		total += (i + 1)*card_val_dic[j]
	print(total)


cards,vals,card_val_dic = process_input()
solve(card_order,cards)