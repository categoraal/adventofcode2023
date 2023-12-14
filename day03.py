input = open('in3t').read().strip().split('\n')
input = ['..'+i+'..' for i in input]
a =[''.join( ['.']*len(input[0]))]
input = a+input+a 
[print(i) for i in input]
number = ''
ld = '.'
numbers = []

def bc(y,x,number):
	l = len(number)	
	sx = x-1-l; sy = y-1
	for idy in range(sy,sy+3):
		for idx in range(sx,sx+l+2):
			if input[idy][idx].isdigit() == False and input[idy][idx] != '.':
				return 1 
	return 0

for idy in range(1,len(input)-1):
	for idx in range(1,len(input[0])-1):
		ch = input[idy][idx]
		if ch.isdigit():
			number += ch 
			ld = ch 
		elif ld.isdigit() and ch.isdigit() == False:
			flag = bc(idy,idx,number)
#			print(number,flag)
			numbers.append(int(number)*flag)
			number = ''
			ld = '.'
			
print(sum(numbers))

## part 2

number = ''
ld = '.'
numbers = [] 
gears = dict()

def bc(y,x,number):
	flag = 0
	l = len(number)	
	sx = x-1-l; sy = y-1
	for idy in range(sy,sy+3):
		for idx in range(sx,sx+l+2):
			if input[idy][idx] =='*':
				return str(idy)+'_'+str(idx)

for idy in range(1,len(input)-1):
	for idx in range(1,len(input[0])-1):
		ch = input[idy][idx]
		if ch.isdigit():
			number += ch 
			ld = ch 
		elif ld.isdigit() and ch.isdigit() == False:
			flag = bc(idy,idx,number)
			if flag is not None:
				numbers.append([number,flag])
				if flag not in gears:
					gears[flag] = [int(number)]
				else:
					gears[flag] += [int(number)]
			
			number = ''
			ld = '.'


gearRatios = []
for gear in gears:
	if len(gears[gear]) == 2:
		gearRatios.append(gears[gear][0]*gears[gear][1])
print(sum(gearRatios))
