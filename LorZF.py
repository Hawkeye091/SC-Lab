import numpy as np
from scipy.special import gamma
import pylab

x = pylab.linspace(-15,20,2000)
a=4
b=7
y=[]
for i in x:
    if i<a :
        y.append(1)
    elif i>=a and i<b :
        y.append(i-a/b-a)
    elif i>=b :
        y.append(0)
pylab.plot(x,y)
pylab.show()

