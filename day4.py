import re

input = open('in4').read().strip().split('\n')
#[print(i) for i in input]

res = []
for line in input:
	win,your = line.split('|')
	win = [int(i) for i in re.findall(r'\d+',win)[1:]]
	your = [int(i) for i in re.findall(r'\d+',your)]
	score = 0
	for num in your:
		if num in win:
			if score == 0:
				score += 1
			else:
				score *= 2
	res.append(score)

print(sum(res))	
	
#part 2
res = []
game_multiplier = [1]*len(input)
#print(game_multiplier)
for idx,line in enumerate(input):
	win,your = line.split('|')
	win = [int(i) for i in re.findall(r'\d+',win)[1:]]
	your = [int(i) for i in re.findall(r'\d+',your)]
	mult = game_multiplier[idx]
	wins = 0
	for num in your:
		if num in win:
			wins+=1
	for i in range(idx+1,idx+1+wins):
		game_multiplier[i] += mult
	
print(sum(game_multiplier))
