import re
import numpy as np
import sympy
input = open('in24').read().strip().split('\n')
input = [[int(j) for j in re.findall(r'-?\d+',i)] for i in input]

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
##linear algebra? Doesn't work all the time??? don't know why.
## the sympy solution works all the time.
input = open('in24').read().strip().split('\n')
input = [[np.double(j) for j in re.findall(r'-?\d+',i)] for i in input]
hailstone1,hailstone2,hailstone3 = input[6:9]
x1,y1,z1,vx1,vy1,vz1 = hailstone1
x2,y2,z2,vx2,vy2,vz2 = hailstone2
x3,y3,z3,vx3,vy3,vz3 = hailstone3

A = np.array([ #X,Y,Z,VX,VY,VZ
    [-vy1+vy2,vx1-vx2,0,y1-y2,-x1+x2,0],
    [-vy1+vy3,vx1-vx3,0,y1-y3,-x1+x3,0],
    [-vz1+vz2,0,vx1-vx2,z1-z2,0,-x1+x2],
    [-vz1+vz3,0,vx1-vx3,z1-z3,0,-x1+x3],
    [0,-vz1+vz2,vy1-vy2,0,z1-z2,-y1+y2],
    [0,-vz1+vz3,vy1-vy3,0,z1-z3,-y1+y3],
])

B = [
        (y1*vx1-y2*vx2)-(x1*vy1-x2*vy2),
        (y1*vx1-y3*vx3)-(x1*vy1-x3*vy3),
        (z1*vx1-z2*vx2)-(x1*vz1-x2*vz2),
        (z1*vx1-z3*vx3)-(x1*vz1-x3*vz3),
        (z1*vy1-z2*vy2)-(y1*vz1-y2*vz2),
        (z1*vy1-z3*vy3)-(y1*vz1-y3*vz3),
]
np.set_printoptions(linewidth=1000000)
X = np.linalg.solve(A,B)
print(round(X[0]+X[1]+X[2]))
print(X[0]+X[1]+X[2])

## sympy solution:
x,y,z,vx,vy,vz = sympy.symbols("x,y,z,vx,vy,vz")

equations = []

for sx,sy,sz,svx,svy,svz in input[:3]:
    equations.append((x-sx)*(svy-vy)-(y-sy)*(svx-vx))
    equations.append((y-sy)*(svz-vz)-(z-sz)*(svy-vy))

answers = [i for i in sympy.solve(equations) if all(j%1==0 for j in i.values())]
ans = answers[0]
print(ans[x]+ans[y]+ans[z])