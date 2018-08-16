import numpy as np
from scipy.special import gamma
import pylab

x = pylab.linspace(0,15,200)
a=1
b=3
c=5
y=[]
for i in x:
    y.append(max(min(i-a/b-a,c-i/c-b),0))
pylab.plot(x,y)
pylab.show()

