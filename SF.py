import numpy as np
from scipy.special import gamma
import pylab

x = pylab.linspace(-20,20,20000)
a=3
b=2.1
y=[]
for i in x:
    if i<=a :
        y.append(0)
    elif i>a and i<(a+b)/2 :
        y.append(2*math.pow((i-a/b-a),2))
    elif i>((a+b)/2) and i<b:
        y.append(1-2*math.pow((i-a/b-a),2))
    elif i>=b :
        y.append(1)
pylab.plot(x,y)
pylab.show()

