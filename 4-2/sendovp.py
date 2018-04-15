import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import comb
import itertools


#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#Apolarity condition for P(x) and Q(x)
def apolarity(q, p):
    sum=0
    for i in range(p.order+1):
        sum+=((-1)**i)*(p[i]*q[p.order-i])/(comb(p.order,i))
    
    if sum==0:
        return(sum)
    else:
        return(sum)
    
    

#degree of the polynomial P(z)
n=4

#roots of P(z)
roots=[[1,np.pi*(2)], [1,np.pi*(2/3)],  [1,np.pi*(2)], [1,np.pi*(1/2)], [0.8,np.pi*(2/1)], [0.05,np.pi*(2/1)], [0.05,np.pi*(2/1)]]



z=[]

for i in range(n):
    z.append(roots[i][0]*np.exp(1j*roots[i][1]))

p=np.poly1d(z, True)
pDash=np.polyder(p)


array1toN=[]
for i in range(n-1):
    array1toN.append(i+1)    
perm=list(itertools.permutations(array1toN))


pp=[[1,2,3],[2,3,1],[3,1,2]]

print(pp)

r=[]
for i in range(len(pp)):
    r.append((n-1)*z[0]/n)        
omega= np.exp(1j*(2*np.pi)/n)

for i in range(len(pp)):
    for j in range(1,n):
        r[i]-=z[j]*(omega**(pp[i][j-1])/n)
        print("sum=", "%.2f" % (-omega**(pp[i][j-1])).real, "+", "%.2f" % (-omega**(pp[i][j-1])).imag,"j")
q=np.poly1d(r, True)


print("Q(x)=")
print(q)
print("P'(x)=")
print(pDash)    
print("sum=", "%.2f" % apolarity(pDash,q).real, "+", "%.2f" % apolarity(pDash,q).imag,"j")
    