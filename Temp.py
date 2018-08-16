import numpy as np
from scipy.special import gamma
import pylab


ax = pylab.linspace(-5, 5, 1000)
pylab.plot(ax, gamma(ax))


pylab.ylim(-50,50)
pylab.xlim(-5, 5)
pylab.xlabel('$x$')
pylab.legend()
pylab.show()