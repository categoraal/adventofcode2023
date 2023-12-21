from copy import deepcopy

input = [list(i) for i in open('in21').read().strip().split('\n')]

start = ()
for r in range(len(input)):
	for c in range(len(input[0])):
		if input[r][c] == 'S':
			queu= [(r,c)]
			start = (r,c)
			break

br = len(input);bc = len(input[0])
dirs = ((1,0),(0,1),(-1,0),(0,-1))
seen = set() 
for i in range(200):
	seen = set() 
	for r,c in queu:
		for dr,dc in dirs:
			nr = r+dr; nc = c+dc
			if 0 <= nr < br and 0 <= nc < bc and input[nr][nc] != '#':# and kaart[nr][nc] != '0':
				seen.add((nc,nr))	
	queu = deepcopy(seen)
	if i == 63:
		print(len(seen))
	if i == 130:
		odd = len(seen)		
		oddboard = deepcopy(seen)
	if i == 131:
		even = len(seen)
		evenboard = deepcopy(seen)
		break

steps = 26501365
radius = int((steps-65)/131)
rest = steps%len(input)

oddboards = 1
evenboards = 0
for i in range(2,radius+1):
	n = 4*(i-1)	
	if i%2 == 0:
		evenboards+=n
	else:
		oddboards+=n

oddnw = len([(i,j) for i,j in oddboard if i+j < 65])
oddne = len([(i,j) for i,j in oddboard if i-j < -65])
oddsw = len([(i,j) for i,j in oddboard if i-j > 65])
oddse = len([(i,j) for i,j in oddboard if i+j > 3*65])

evennw = len([(i,j) for i,j in evenboard if i+j < 65])
evenne = len([(i,j) for i,j in evenboard if i-j < -65])
evensw = len([(i,j) for i,j in evenboard if i-j > 65])
evense = len([(i,j) for i,j in evenboard if i+j > 3*65])
oddboards+=4*radius
rm = (radius+1)*(oddnw+oddne+oddsw+oddse)
ad = (radius)*(evennw+evenne+evensw+evense)
print(evenboards*even+oddboards*odd-rm+ad)
