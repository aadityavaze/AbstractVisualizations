import numpy as np
import matplotlib.pyplot as plt
import math



#polynomial objective function
def f(x,y):
    return ((x-roots[0][0])*(x-roots[0][0])+(y-roots[0][1])*(y-roots[0][1]))*((x-roots[1][0])*(x-roots[1][0])+(y-roots[1][1])*(y-roots[1][1]))*((x-roots[2][0])*(x-roots[2][0])+(y-roots[2][1])*(y-roots[2][1]))-1

def derivativeX(x,y):
    return (f(x+e,y)-f(x,y))/e

def derivativeY(x,y):
    return (f(x,y+e)-f(x,y))/e

def newton_raphsonX(x,y):
     return (x - (f(x,y) / derivativeX(x,y)))

def newton_raphsonY(x,y):
    return (y - (f(x,y) / derivativeY(x,y)))

def iterateX(x, y, n):
    for i in range(1,n):
        x = newton_raphsonX(x,y)
    return x

def iterateY(x, y, n):
    for i in range(1,n):
        y = newton_raphsonY(x,y)
    return y

def sign(x):
    return x/abs(x)

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))




#dx
s=0.003
e=0.001
k=0.00001
lim=5


#points A, B, C
roots=[[0, 0], [1.732, 0], [0.866, 1.5]]


#initial guesses for corresponding starting point used to trace on each loop
approxY=[-2,-2,roots[2][0]+3]

#declare 2d start array
start=[]
for j in range(3):
        column = []
        for i in range(2):
                column.append(0)
        start.append(column)
startLength=0
finalLength=0
dd=0.01

checkArray=[[roots[2][0], roots[2][1]],[roots[2][0]+dd, roots[2][1]],[roots[2][0], roots[2][1]+dd]]
disArray=[0,0,0]
for ch in range(1):
    totalDis=0
    countLoops=0
    roots[2][0]=checkArray[ch][0]
    roots[2][1]=checkArray[ch][1]
    for j in range(3):
        dis=0
        repeat=0
        x=roots[j][0]
        print("x:",x)
        y=approxY[j]
        y=iterateY(x,y,10)
        print("y:",y)
        start[j][0]=x
        start[j][1]=y
        for i in range(0,4000):
            px=x
            py=y
            H=-derivativeY(x,y)
            K=derivativeX(x,y)
            if abs(H)>abs(K):
                h=s*sign(H)
                x=x+h
                y=y+((h*K)/H)
                y=iterateY(x,y,8)
                #plt.plot([px,x],[py,y],'-b')
            elif K!=0:
                k=s*sign(K)
                y=y+k
                x=x+((k*H)/K)
                x=iterateX(x,y,8)
                #plt.plot([px,x],[py,y],'-b')
            for k in range(j):
                if (distance(start[k][0],start[k][1],x,y)<0.2):
                    repeat=1
                    break
            if repeat==1:
                break
            if (distance(start[j][0],start[j][1],x,y)<0.02 and i>20):
                break
            dis+=distance(px,py,x,y)
            plt.plot([px,x],[py,y])
        print("loop length:", dis)
        if repeat==0:
            totalDis+=dis
            countLoops+=1
        else:
            print("This is a repeated loop")

    print("total loop length", totalDis)
    disArray[ch]=totalDis

denominator = math.sqrt((disArray[1]-disArray[0])*(disArray[1]-disArray[0])+(disArray[2]-disArray[0])*(disArray[2]-disArray[0]))
roots[2][0]+= dd*(disArray[1]-disArray[0])/denominator
roots[2][1]+= dd*(disArray[2]-disArray[0])/denominator
print("final x", roots[2][0])
print("final y", roots[2][1])
plt.xlim(-lim,lim)
plt.ylim(-lim,lim)
plt.show()
