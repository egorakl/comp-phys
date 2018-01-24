import math
import cmath
from mpmath import *

b=10**(20)
c=4
n=25
d=(b/2)**2-c

print ("b =",b)
print ("c =",c)
print()
def order(x):
  a=log10(abs(x))
  return a

def sd(b):
  sq=b*math.sqrt(1-(4*c/b**2))
  return sq

def csd(b):
  sq=b*cmath.sqrt(1-(4*c/b**2))
  return sq

def sol(d):
    if d>0: 
        p = taylor(sd, b, n)
        sqd=polyval(p[::-1], 0)
    else:
        p = taylor(csd, b, n)
        sqd=polyval(p[::-1], 0)
        
    if (order((-b + sqd))>order(-b - sqd)):
      x1=(-b+sqd)/2.0
    else:
      x1=(-b-sqd)/2.0
    x2=c/x1
    return x1, x2

print("Solution:")
if d == 0:
    x = (-b)/2.0
    print(x)
else:
    print(sol(d))
