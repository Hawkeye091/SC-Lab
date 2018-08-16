import numpy as np
from scipy.special import gamma
import pylab
import math

x = pylab.linspace(-5,15,200)
c=7.5
t=15
y=[]
for i in x:
    y.append(math.exp(math.pow(i-c/t,2)*(-1/2)))
pylab.plot(x,y)
pylab.show()

