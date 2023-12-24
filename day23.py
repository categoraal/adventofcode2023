import time
from copy import deepcopy
input = open('in23').read().strip().split('\n')
input = [list(i) for i in input]

for idx,val in enumerate(input[0]):
    if val == '.':
        start = (0,idx)
        break

for idx,val in enumerate(input[-1]):
    if val == '.':
        stop = (len(input)-1,idx)

br = len(input);bc = len(input[0])

kruispunten = [] # 5 of minder hashtags
for r in range(1,len(input)-1):
    for c in range(1,len(input[0])-1):
        if input[r][c] != '#':
            l = input[r][c+1]+input[r][c-1]+input[r+1][c]+input[r-1][c]
            if l.count('#') < 2:
                kruispunten.append((r,c))
                input[r][c] = 'k'

def route(start,seen,dist,stop):
    queu = start
    for r,c,dr,dc in queu:
        dirs = {'<':[(0,-1)],'>':[(0,1)],'^':[(-1,0)],'v':[(1,0)],'.':((dr,dc),(-dc,dr),(dc,-dr))}
        cur = input[r][c]
        if (r,c) == stop:
            ends.append(dist)
            return dist
        if cur in '.<>v^':
            for drr,dcc in dirs[cur]:
                nr = r+drr;nc = c+dcc
                if drr == -dr and dcc == -dc:
                    return 0
                if 0 <= nr < br and 0 <= nc < bc:
                    if input[nr][nc] != '#':
                        queu.append((nr,nc,drr,dcc))
                        dist += 1
        if cur == 'k':
            lengths = []
            if (r,c) in seen:
                return 0
            else:
                dist += 1
                seen.append((r,c))
                for drr,dcc in dirs['.']:
                    nr = r+drr;nc = c+dcc
                    if input[nr][nc] != '#':
                        new = input[nr][nc]
                        lengths.append(route([(nr,nc,drr,dcc)],deepcopy(seen),dist,stop))
                return max(lengths)
    left = 1
    right = 2
    return 0

ends = []
seen = []
start = [(start[0],start[1],0,1)]
a = route(start,seen,0,stop)
print(a)

## part 2======================================================================
def route(start,seen,dist,stop):
    queu = start
    for r,c,dr,dc in queu:
        dirs = {'<':[(0,-1)],'>':[(0,1)],'^':[(-1,0)],'v':[(1,0)],'.':((dr,dc),(-dc,dr),(dc,-dr))}
        cur = input[r][c]
        if (r,c) == stop:
            ends.append(dist)
            cnt = len(ends)
            if cnt%10000 == 0:
                print(cnt)

            return dist
        if cur in '.<>v^':
            for drr,dcc in dirs['.']:
                nr = r+drr;nc = c+dcc
                if 0 <= nr < br and 0 <= nc < bc:
                    if input[nr][nc] != '#':
                        queu.append((nr,nc,drr,dcc))
                        dist += 1
        if cur == 'k':
            lengths = []
            if (r,c) in seen:
                return 0
            else:
                dist += 1
                seen.append((r,c))
                for drr,dcc in dirs['.']:
                    nr = r+drr;nc = c+dcc
                    if input[nr][nc] != '#':
                        lengths.append(route([(nr,nc,drr,dcc)],deepcopy(seen),dist,stop))
                return max(lengths)
    left = 1
    right = 2
    return 0

ends = []
seen = []
start = [(0,1,0,1)]
a = route(start,deepcopy(seen),0,(127,135))+65 #is distance from last print(a)
