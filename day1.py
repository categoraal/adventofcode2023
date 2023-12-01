import re

input = open('in1').read().strip().split('\n')
numbers = []
getal = []
for i in range(len(input)):
	getal.append(''.join(re.findall(r'\d+',input[i])))

		
for i in getal:
	numbers.append(int(i[0]+i[-1]))
	# print(numbers[-1])

#print(numbers)
print(sum(numbers))

## part 2
input = open('in1').read().strip().split('\n')
numbers = []
getal = []
vervangen = []
for i in input:
	a = re.sub(r'one','one1one',i)
	a = re.sub(r'two','two2two',a)
	a = re.sub(r'three','three3three',a) 
	a = re.sub(r'four','four4four',a)
	a = re.sub(r'five','five5five',a)
	a = re.sub(r'six','six6six',a)
	a = re.sub(r'seven','seven7seven',a)
	a = re.sub(r'eight','eight8eight',a)
	a = re.sub(r'nine','nine9nine',a)
	vervangen.append(a)

for i in range(len(input)):
	getal.append(''.join(re.findall(r'\d+',vervangen[i])))
	
		
for i in getal:
	numbers.append(int(i[0]+i[-1]))
	
print(sum(numbers))