import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import comb

#Apolarity condition for P(x) and Q(x)
def apolarity(p, q):
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
roots=[[1,np.pi*(2)], [1,np.pi*(1)],  [0,np.pi*(1)], [0,np.pi*(4/3)], [0.8,np.pi*(2/1)], [0.05,np.pi*(2/1)]]



z=[]
for i in range(n):
    z.append(roots[i][0]*np.exp(1j*roots[i][1]))

p=np.poly1d(z, True)
pDash=np.polyder(p)

r=[1, -(2*z[0]+(z[0]+z[1]+z[2]+z[3])/4), -pDash[1]/6, -(pDash[0]/4)-z[0]*(pDash[1])]
   


q=np.poly1d(r)




print("Q(x)=")
print(q)
print("P'(x)=")
print(pDash)    
print("sum=", "%.2f" % apolarity(pDash,q).real, "+", "%.2f" % apolarity(pDash,q).imag,"j")


for i in range(n-1):
    print(np.roots(q))
    print(abs(np.roots(q)[i]-z[0]))