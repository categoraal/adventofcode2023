import re

input = open('in24').read().strip().split('\n')
input = [[float(j) for j in re.findall(r'-?\d+',i)] for i in input]

def intersection(vx1,vx2,vy1,vy2,px1,px2,py1,py2):
    a1 = vy1/vx1;b1 = -a1*px1+py1
    a2 = vy2/vx2;b2 = -a2*px2+py2
    if a1 == a2:
        return False,False,False,False
    else:
        x = (b2-b1)/(a1-a2)
        y = a1*x+b1
        t1 = (x-px1)/vx1
        t2 = (x-px2)/vx2
        return x,y,t1,t2
    
lb = 200000000000000
ub = 400000000000000
cnt = 0
for i1 in range(len(input)):
    for i2 in range(i1+1,len(input)):
        px1,py1,pz1,vx1,vy1,vz1 = input[i1]
        px2,py2,pz2,vx2,vy2,vz2 = input[i2]
        x,y,t1,t2 = intersection(vx1,vx2,vy1,vy2,px1,px2,py1,py2)
        if t1 and lb <= x <= ub and lb <= y <= ub and t1 >= 0 and t2>=0:
            cnt += 1
print(cnt)

##Part 2:
##linear algebra?

