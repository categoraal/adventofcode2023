input = open('in10').read().strip().split('\n')

start = 's'
for i in range(len(input)):
	for j in range(len(input[0])):
		if input[i][j] == 'S':
			start = (i,j)
			sy = i; sx = j
			break

kaart = []
for i in range(len(input)):
	kaart.append(len(input[0])*['.'])


dirs = {'|':[[-1,0],[1,0]],'-':[[0,1],[0,-1]],'L':[[-1,0],[0,1]],'J':[[-1,0],[0,-1]],'F':[[0,1],[1,0]],'7':[[0,-1],[1,0]],'S':[[-1,0],[0,1],[1,0],[0,-1]],'.':[[0,0]]}#|-LJf7

kaart[sy][sx]=0
def neighbors(lt,loc,d):
	y,x = loc
	dd = dirs[lt]
	res = []
	for i in dd:
		ny = y + i[0];nx = x + i[1]
		nlt = input[ny][nx]
		for j in dirs[nlt]:
			if [a + b for a, b in zip(i,j )] == [0,0]:
				if kaart[ny][nx] == '.':
					kaart[ny][nx]=d+1
					res.append([ny,nx])
				if kaart[ny][nx] != '.':
					if kaart[ny][nx] > d +1:
						kaart[ny][nx] = d+1
						res.append([ny,nx])
	return res	

cardinals = [(-1,0),(0,1),(1,0),(0,-1)] #u,r,d,l
queu = [[sy,sx]]
c = 0
for cloc in queu:
	y,x = cloc
	dist = kaart[y][x]
	nlocs = neighbors(input[y][x],(y,x),dist)
#	print(nlocs,'nlocs')
	[queu.append(i) for i in nlocs]
#	print(queu)
#[print(i) for i in kaart]
m = 0
for i in kaart:
	for j in i:
		if j != '.':
			if j > m:
				m = j
print(m)
#[print(i) for i in kaart]
# Part 2
#[print(i) for i in input]
k2 = []
#S = |
for i in input:
	l = []
	for j in i:
		if j != '.':
			l.append('/')
		else:
			l.append('.')
	k2.append(l)
#[print(i) for i in k2]
for i in range(len(kaart)):
	for j in range(len(kaart[0])):
		if kaart[i][j] != '.':
			k2[i][j] = 'b'

#[print(''.join(i)) for i in k2]

sx = 0; sy = 0
queu = [[sy,sx]]
k2[sy][sx] = 1
for i in queu:
	cy, cx = i
	for j in cardinals:
		dx, dy = j
		nx = cx+dx;ny = cy+dy
		if nx >= 0 and ny >= 0 and nx < len(k2[0]) and ny < len(k2):
			if k2[ny][nx] != 'b' and k2[ny][nx] != '1':
				queu.append([ny,nx])
				k2[ny][nx] = '1'



#[print(''.join(i)) for i in k2]
c = 0
for i in k2:
	for j in i:
		c += j.count('1')


tocheck = []
for idy in range(len(input)):
	for idx in range(len(input[0])):
		if k2[idy][idx] in '/.':
			tocheck.append([idy,idx])

def check(y,x):
	cnt = 0
	for i in range(x):
		if k2[y][i] == 'b' and input[y][i] in 'L|JS':
			cnt+=1
	return cnt%2


res = 0
for i in tocheck:
	y,x = i
	a = check(y,x)
	res += a
	if a == 1:
		k2[y][x] = '*'
	

#[print(''.join(i)) for i in k2]
print(res)


