import re
rules,data = open('in19t').read().strip().split('\n\n')

rules = rules.split('\n')
data = data.split('\n')

rd = {}
for i in rules:
	key,val = i[:-1].split('{')
	rd[key] = val.strip().split(',')	


def accepted(x,m,a,s,key):
	if key == 'A':
		return True
	elif key == 'R':
		return False

	h = {'s':s,'x':x,'a':a,'m':m}
	rule = rd[key]
	for i in rule:
		i = i.split(':')
		if len(i) > 1:
			num = int(*re.findall(r'\d+',i[0]))	
			key = i[-1]
			if '<' in i[0]:
				if h[i[0][0]] < num:
					return accepted(x,m,a,s,key)
			if '>' in i[0]:
				if h[i[0][0]] > num:
					return accepted(x,m,a,s,key)
		else:
			key = i[0]
			return accepted(x,m,a,s,key)	

res = 0
for i in data:
	l = [int(j) for j in re.findall(r'\d+',i)]
	if accepted(*l,'in'):
		res += sum(l)

ans1 = res
#print(res)

#Part 2
result_list = []
not_result_list = []
state = []
def acceptedRange(x,m,a,s,key):
	xl,xu = x; ml,mu = m; al,au = a; sl,su = s
	if xl>xu or ml>mu or al>au or sl>su:
		return 0	
#	print(x,m,a,s)
	if key == 'A':
		result_list.append((x,m,a,s))
		return (xu-xl+1)*(mu-ml+1)*(au-al+1)*(su-sl+1)
		#return 0
	elif key == 'R':
		not_result_list.append((x,m,a,s))
		#return (xu-xl+1)*(mu-ml+1)*(au-al+1)*(su-sl+1)
		return 0

	h = {'s':s,'x':x,'a':a,'m':m}
	rule = rd[key]
	res = 0
	passrange = []
	notpassrange = []
	for i in rule:
		i = i.split(':')
		print(i)
		if len(i) > 1:
			num = int(*re.findall(r'\d+',i[0]))	
			nkey = i[-1]
			lb,up = h[i[0][0]]
			print(x,m,a,s)
			if '<' in i[0]:
				if up < num:
					return acceptedRange(x,m,a,s,nkey)
				elif num <= lb:
					continue			
				else:
					passrange = (lb,num-1)
					notpassrange = (num,up)
					

			if '>' in i[0]:
				if lb > num:
					return acceptedRange(x,m,a,s,nkey)
				elif up <= num: 	
					continue
				else:
					notpassrange = (lb,num)
					passrange = (num+1,up)
			print(i[0][0])
			print(passrange,notpassrange)
			match i[0][0]:
				case 'x':
					res += acceptedRange(passrange,m,a,s,key)
					x = notpassrange
				case 'm':
					res += acceptedRange(x,passrange,a,s,key)
					m = notpassrange
				case 'a':
					res += acceptedRange(x,m,passrange,s,key)
					a = notpassrange
				case 's':					
					res += acceptedRange(x,m,a,passrange,key)
					s = notpassrange
				case _:
					print('error')
		else:
			nkey = i[-1]
			return res+acceptedRange(x,m,a,s,nkey)

#ans2 = acceptedRange((1,4000),(1,4000),(1,4000),(1,4000),'in')
ans2 = acceptedRange((787,787),(2655,2655),(1222,1222),(2876,2876),'in')

		
print('part 1:',ans1)
print('part 2:',ans2)
print(len(result_list))
print(len(set(result_list)))
res = 0
for x,m,a,s in set(result_list):
	xl,xu = x; ml,mu = m; al,au = a; sl,su = s
	res += (xu-xl+1)*(mu-ml+1)*(au-al+1)*(su-sl+1)
print(res)

res3 = 0
for x,m,a,s in set(not_result_list):
	xl,xu = x; ml,mu = m; al,au = a; sl,su = s
	res3 += (xu-xl+1)*(mu-ml+1)*(au-al+1)*(su-sl+1)
print(res3)
print(4000**4)
print(res+res3)
res2 = 0
for x,m,a,s in set(result_list):
	xl,xu = x; ml,mu = m; al,au = a; sl,su = s
	res2 += (xu-xl+1)*(mu-ml+1)*(au-al+1)*(su-sl+1)
print(res2)

print(4000**4-res2)

print(list(set(result_list) & set(not_result_list)))














#part 2 take 2
rules,data = open('in19t').read().strip().split('\n\n')

rules = rules.split('\n')
data = data.split('\n')

rd = {}
for i in rules:
	key,val = i[:-1].split('{')
	rd[key] = val.strip().split(',')	
from collections import deque
queu = deque([((1,4000),(1,4000),(1,4000),(1,4000),'in')])
rl = []
cnt = 0
while queu:
	cnt += 1
	x,m,a,s,key = queu.pop()
#	print(x,m,a,s,key)
	xl,xu = x; ml,mu = m; al,au = a; sl,su = s

	if key == 'A':
		rl.append((xu-xl+1)*(mu-ml+1)*(au-al+1)*(su-sl+1))	
		continue
	elif key == 'R':
		continue

	h = {'s':s,'x':x,'a':a,'m':m}
	rule = rd[key]
#	print(rule)	
	for r in rule:
		r = r.split(':')
#		print(r)
#		print(len(r))
		if len(r) == 1:
			nkey = r[-1]
			queu.append((x,m,a,s,nkey))	
			continue
		else:
			nkey = r[-1]
			num = int(*re.findall(r'\d+',r[0]))	
#			print(r)
			lb,up = h[r[0][0]]

			if '<' in r[0]:
				if up < num:
					queu.append((x,m,a,s,nkey))
					continue
				elif num <= lb:
					continue			
				else:
					passrange = (lb,num-1)
					notpassrange = (num,up)

			if '>' in r[0]:
				if lb > num:
					queu.append((x,m,a,s,nkey))
					continue
				elif up <= num: 	
					continue
				else:
					notpassrange = (lb,num)
					passrange = (num+1,up)
			match r[0][0]:
				case 'x':
					queu.append((passrange,m,a,s,key))
					queu.append((notpassrange,m,a,s,nkey))
				case 'm':
					queu.append((x,passrange,a,s,key))
					queu.append((x,notpassrange,a,s,nkey))
				case 'a':
					queu.append((x,m,passrange,s,key))
					queu.append((x,m,notpassrange,s,nkey))
				case 's':					
					queu.append((x,m,a,passrange,key))
					queu.append((x,m,a,notpassrange,nkey))

#		print(cnt)
		if cnt > 10:
			break


#print(sum(rl))

