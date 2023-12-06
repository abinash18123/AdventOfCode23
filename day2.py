def solve(string):
	# for string in arr:
		game_no,sack = string.split(':')
		game_no = int(game_no.split(' ')[-1])
		picks = sack.split(';')
		red = -1e9
		green = -1e9 
		blue = -1e9  

		for pick in picks: 
			colors = pick.split(',')
			for num_col in colors:
				_,nums,color = num_col.split(' ')
				# print(numss,color)
				nums = int(nums)
				if color == 'blue':
					if blue < nums: 
						blue = nums
				if color == 'green':
					if green < nums: 
						green = nums 
				if color == 'red':
					if red < nums: 
						red = nums 
		# print(red,green,blue)
		return red * green * blue


arr = [(i.rstrip()) for i in open("input.txt", "r")]

print(sum([solve(i) for i in arr]))

