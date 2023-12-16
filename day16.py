input = open('in16').read().strip().split('\n')
card = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)} #north, easth, south, west
slash = {0:1,1:0,2:3,3:2}
bslash = {0:3,3:0,1:2,2:1}

rb = len(input)-1
cb = len(input[0])-1

def chb(r,c):
	if 0 <= r <= rb and 0 <= c <= cb:
		return True
	return False

def energized(start):
	directionmap = []
	for i in range(len(input)):
		row = []
		for j in range(len(input[0])):
			row.append([])
		directionmap.append(row)

	visited = set()
	visited.add((start[0],start[1]))
	queu = [(start)]
	for i in queu:
		r,c,d = i
		b = input[r][c]
		match b:
			case '.':
				nd = [d]
			case '|':
				if d == 1 or d == 3:
					nd = [0,2]
				else:
					nd = [d]	
			case '-':
				if d == 0 or d == 2:
					nd = [1,3]
				else:
					nd = [d]
			case '/':
				nd = [slash[d]]
			case other: 	
				nd = [bslash[d]]
			
		for i in nd:
			dr,dc = card[i]
			nr = r+dr;nc = c+dc			
			if chb(nr,nc):
				if i not in directionmap[nr][nc]:
					directionmap[nr][nc].append(i)
					queu.append((nr,nc,i))
				visited.add((nr,nc))
	return len(visited)
print(energized((0,0,1)))

high = 0
for i in range(len(input[0])):
	val = energized((0,i,2))
	if val > high:
		high = val

for i in range(len(input[0])):
	val = energized((len(input)-1,i,0))
	if val > high:
		high = val

print(high)
