input = open('in11').read().strip().split('\n')
input = [list(i) for i in input]

emptyr = []
for i in range(len(input)):
	if set(input[i]) == {'.'}:
		emptyr.append(i)

emptyc = []
for i in range(len(input[0])):
	col = []
	for j in range(len(input)):
		col.append(input[j][i])
	if set(col) == {'.'}:
		emptyc.append(i)

ogstars = []
for i in range(len(input)):
	for j in range(len(input[0])):
		if input[i][j] == '#':
			ogstars.append([i,j])

def newloc(r,c,d):
	nc = 0;	nr = 0
	for i in emptyr:
		if i < r:
			nr += d-1
	for j in emptyc:
		if j < c:
			nc += d-1
	return nr+r,nc+c	

stars = [newloc(i[0],i[1],2) for i in ogstars]
distances = []
for i in range(len(stars)-1):
	for j in range(len(stars)-i):
		s1 = stars[i]
		s2 = stars[i+j]
		d = abs(s1[0]-s2[0]) + abs(s1[1]-s2[1])
		distances.append(d)

print(sum(distances))	

stars = [newloc(i[0],i[1],1000000) for i in ogstars]
distances = []
for i in range(len(stars)-1):
	for j in range(len(stars)-i):
		s1 = stars[i]
		s2 = stars[i+j]
		d = abs(s1[0]-s2[0]) + abs(s1[1]-s2[1])
		distances.append(d)

print(sum(distances))
