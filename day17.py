from queue import PriorityQueue
input = [[int(i) for i in j] for j in open('in17').read().strip().split('\n')]

s1 = (0,0,0,1,0,0)
s2 = (0,0,0,0,1,0)
goal = (len(input)-1,len(input[0])-1)
pq = PriorityQueue()
pq.put(s1)
pq.put(s2)
seen = {(0,0,1,0,0):0,(0,0,0,1,0):0}

while not pq.empty():
    heat,r,c,dr,dc,streak = pq.get()
    key = (r,c,dr,dc,streak)

    if (r,c) == goal:
        print(heat)
        break

    if heat > seen[key]:
        continue
    
    dirs = []
    if streak < 3:
        dirs.append((dr,dc))
    dirs.append((-dc,dr))
    dirs.append((dc,-dr))

    for drr,dcc in dirs:
        nr = r + drr;nc = c + dcc
        if 0 <= nr < len(input) and 0 <= nc < len(input[0]):
            nh = heat + input[nr][nc]
            key = (nr,nc,drr,dcc,streak +1 if (dr,dc) == (drr,dcc) else 1)
            if key not in seen or nh < seen[key]:
                seen[key] = nh
                pq.put((nh,*key))
            
##Part 2
s1 = (0,0,0,1,0,0)
s2 = (0,0,0,0,1,0)
goal = (len(input)-1,len(input[0])-1)
pq = PriorityQueue()
pq.put(s1)
pq.put(s2)
seen = {(0,0,1,0,0):0,(0,0,0,1,0):0}

while not pq.empty():
    heat,r,c,dr,dc,streak = pq.get()
    key = (r,c,dr,dc,streak)

    if (r,c) == goal:
        print(heat)
        break

    if heat > seen[key]:
        continue
    
    dirs = []
    if streak < 10:
        dirs.append((dr,dc))
    
    if streak > 3:
        dirs.append((-dc,dr))
        dirs.append((dc,-dr))

    for drr,dcc in dirs:
        nr = r + drr;nc = c + dcc
        if 0 <= nr < len(input) and 0 <= nc < len(input[0]):
            nh = heat + input[nr][nc]
            key = (nr,nc,drr,dcc,streak +1 if (dr,dc) == (drr,dcc) else 1)
            if key not in seen or nh < seen[key]:
                seen[key] = nh
                pq.put((nh,*key))
