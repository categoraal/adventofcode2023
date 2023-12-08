import re
import math


input = open('in8').read().strip().split('\n\n')

ins = input[0]
dirs = dict()

for i in input[1].split('\n'):
	dirs[i[:3]] = [i[7:10],i[12:15]]

c = 0
end = False
loc = 'AAA'
while end is not True:
	c += 1
	LR = ins[(c-1)%len(ins)]	
	if LR == 'L':
		loc = dirs[loc][0]
	elif LR == 'R':
		loc = dirs[loc][1]	
	if loc == 'ZZZ':
		end = True

print(c)


# part 2
ins = input[0]
dirs = dict()
locs = []

for i in input[1].split('\n'):
	dirs[i[:3]] = [i[7:10],i[12:15]]
	if i[2] == 'A':
		locs.append(i[:3])

ends = []
for i in locs:
	ends_sub = []	
	c = 0
	while c < 100000:
		c += 1
		LR = ins[(c-1)%len(ins)]	
		if LR == 'L':
			i = dirs[i][0]
		elif LR == 'R':
			i = dirs[i][1]
		if i[-1] == 'Z':
			ends_sub.append(c)
	nns = []
	for i in range(len(ends_sub)-1):
		nns.append(ends_sub[i+1]-ends_sub[i])
	ends.append(nns)
factors = []
for i in ends:
	factors.append(i[1])

print(math.lcm(*factors))
