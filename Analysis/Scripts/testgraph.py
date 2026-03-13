'''from csv import reader
from matplotlib import pyplot

with open('C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\Results\Trial7\pyresults7minmaint.csv','r') as f:
    data = list(reader(f))

pyplot.plot('run','ave_iri')
pyplot.show()
'''

import matplotlop.pyplot as plt
import numpy as np

Y = Define the y value
X = Define the x values
plt.plot(X, Y) # Plot the values here and include the label
plt.xlable('string with x label')
plt.ylable('string with y label')
plt.legend(loc='upper left')
plt.show() 

