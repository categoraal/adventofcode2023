import numpy as np
from copy import deepcopy
input = open('in14').read().strip().split('\n')


#[print(i) for i in input]
res = 0
for c in range(len(input[0])):
	current = 0
	for r in range(len(input)):
		if input[r][c] == '#':
			current = r+1
		if input[r][c] == 'O':
			res += len(input) - current
			current += 1				

print(res)

#part 2
input = [list(i) for i in input]
#input = np.array(input)


def rot(x,times):
	for j in range(times):
		x = [list(i) for i in zip(*reversed(x))]
	return x

def score(x):
	res = 0
	for r in range(len(x)):
		res += x[r].count('O')*(len(x)-r)
	return res

def roll(x):
	for c in range(len(x[0])):
		current = 0
		for r in range(len(x)):
			if x[r][c] == '#':
				current = r+1
			if x[r][c] == 'O':
				x[r][c] = '.'
				x[current][c] = 'O'	
				current += 1			
	return x

allres = []
cnt = 0
pattern = True
grids = []
while pattern:
	#mapping logic
	n = cnt%4
	input = rot(input,n)#point so that the current direction is up
	input = roll(input) #roll the stones 
	if n != 0:
		input = rot(input,4-n) #point the board back up
	#for east and west the scores don't change
	if n == 0 or n == 2:
		allres.append(score(input))	

	if (n,input) in grids:
		cycle = cnt-grids.index((n,input))
		cnt = 1000000000*4-1-(1000000000*4-cnt-1)%cycle
		
	if (n,input) not in grids:
		grids.append((n,deepcopy(input)))

	cnt += 1	
	if cnt == 1000000000*4-1:
		pattern = False
	
print(allres[-1])
