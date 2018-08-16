import numpy as np
from scipy.special import gamma
import pylab

ax = pylab.linspace(-5, 5, 1000)
pylab.plot(ax, gamma(ax))