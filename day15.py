input = open('in15').read().strip().split(',')

def hash(x):
	c = 0
	for i in x:
		n = ord(i)
		c += n
		c *= 17
		c = c%256
	return c

res = 0
for s in input:
	res += hash(s)

print(res)

#part 2
box = dict()
for i in input:
	if '=' in i:
		l,r = i.split('=')
		lab = hash(l)
		if lab in box:
			cur = box[lab]
			n = -1
			for i,val in enumerate(cur):
				if l in val:
					n = i
					break
			if n >= 0:
				cur[n] = [l,int(r)]	
			else:
				cur.append([l,int(r)])
		else:
			cur = [[l,int(r)]]
		box[lab] = cur	
	else:
		l,r = i.split('-')
		lab = hash(l)	
		if lab in box:
			cur = box[lab]	
			for i,val in enumerate(cur):
				if l in val:
					cur.pop(i)
					break

res = 0
for i in box:
	for idx,val in enumerate(box[i]):
		if len(box[i]) > 0:
			res += (i+1)*val[1]*(idx+1) 
print(res)
