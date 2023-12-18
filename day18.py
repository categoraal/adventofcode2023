from copy import deepcopy
input = open('in18').read().strip().split('\n')
input = [i.split() for i in input]

dirs = {'R':(0,1),'D':(1,0),'L':(0,-1),'U':(-1,0)}
points = [(0,0)]
for i in input:
	dist = int(i[1])
	sr,sc = points[-1]
	dr,dc = dirs[i[0]]
	nr = sr+dr*dist	
	nc = sc+dc*dist
	points.append((nr,nc))

rc = list(map(list,zip(*points)))
maxr = max(rc[0]);maxc = max(rc[1]);minr = min(rc[0]);minc = min(rc[1])

kaart = []
for i in range(minr,maxr+1):
	r = []
	for j in range(minc,maxc+1):
		r.append('.')
	kaart.append(r)
points = [(r-minr,c-minc) for r,c in points]

lr,lc = (-minr,-minc)
for r,c in points:
	if r != lr:
		for i in range(min(lr,r),max(lr+1,r+1)):
			kaart[i][c] = '#'
	else:
		for i in range(min(lc,c),max(lc+1,c+1)):
			kaart[r][i] = '#'
	lr = r
	lc = c			

queu = [(0,0),(0,len(kaart[0])-1),(len(kaart)-1,0),(len(kaart)-1,len(kaart[0])-1)]
cnt = 0
for i in queu:
	r,c = i
	if kaart[r][c] == '.':
		kaart[r][c] = 'O'
		cnt += 1
		for j in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
			if 0 <= j[0] < len(kaart) and 0 <= j[1] < len(kaart[0]):
				row,col = j
				queu.append((row,col))	

print(len(kaart)*len(kaart[0])-cnt)


## part 2
oldpoints = deepcopy(points)
dirs = {'0':(0,1),'1':(1,0),'2':(0,-1),'3':(-1,0)}
points = [(0,0)]
for i in input:
	dist = 0
	conv = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
	for j in i[-1][2:-2]:
		dist = dist*16+conv[j]	
	sr,sc = points[-1]
	dr,dc = dirs[i[-1][-2]]
	nr = sr+dr*dist	
	nc = sc+dc*dist
	points.append((nr,nc))
	
rc = list(map(list,zip(*points)))
maxr = max(rc[0]);maxc = max(rc[1]);minr = min(rc[0]);minc = min(rc[1])
points = [(r-minr,c-minc) for r,c in points]

def shoelace(x):
	res = 0
	l = 0
	for i in range(len(x)):
		a,c = x[i]
		b,d = x[(i+1)%len(x)]					
		l += abs(a-b+c-d)
		res += a*d - b*c	
	res = abs(res)/2
	return res+l/2+1

print(shoelace(points))
