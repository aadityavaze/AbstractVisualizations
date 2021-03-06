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
roots=[[1,np.pi*(4/3)], [0.5,np.pi*(1/3)],  [1,np.pi*(2/3)], [0,np.pi*(4/3)], [0.8,np.pi*(2/1)], [0.05,np.pi*(2/1)]]



z=[]
for i in range(n):
    z.append(roots[i][0]*np.exp(1j*roots[i][1]))

p=np.poly1d(z, True)
pDash=np.polyder(p)
ui=[0.32275*1j, 0.25, -0.32275*1j]
r=[]
for i in range(n-1):
    r.append((n-1)*z[0]/n)        
#omega= np.exp(1j*(2*np.pi)/n)
power=1
for i in range(n-1):
    power=i-1
    for j in range(1,n):
        power+=1
        power%=n-1
        r[i]+=z[j]*(ui[power])
        print(ui[power])
        
print("r", r)
q=np.poly1d(r, True)




print("Q(x)=")
print(q)
print("P'(x)=")
print(pDash)    
print("sum=", "%.2f" % apolarity(pDash,q).real, "+", "%.2f" % apolarity(pDash,q).imag,"j")
    