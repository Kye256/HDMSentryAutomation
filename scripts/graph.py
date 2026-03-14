import matplotlib.pyplot as plt
from pylab import show

import matplotlib.cbook as cbook

fname = cbook.get_sample_data('../results/factorial/trial7/pyinput.csv' , asfileobj=False)
#fname2 = cbook.get_sample_data('../results/factorial/trial7/pyresults7reconstruction.csv' , asfileobj=False)

plt.plotfile(fname, ('run','tg','co','tv','ge'), subplots=True )
#plt.plotfile(fname2, ('run','npv','ave_iri'), subplots=True, newfig=False, label = 'Reconst')
#plt.legend()

plt.show()