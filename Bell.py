import numpy as np
from scipy.special import gamma
import pylab
import math

x = pylab.linspace(-5,15,200)
a=6
b=8
c=10
y=[]
for i in x:
    y.append(1/(1+math.pow(abs(i-c/a),2*b)))
pylab.plot(x,y)
pylab.show()

