
import os
import numpy as np
from matplotlib import pyplot as plt
import nlreg1d as nl


# set parameters:
niter     = 5
save      = True



# load and register data:
dataset   = nl.data.SimulatedB()
y         = dataset.dv
J         = (dataset.group==0).sum()     # number of observations in first group
yr,wf     = nl.register_srsf(y, MaxItr=niter)
wlist     = nl.Warp1DList( wf )
d         = wlist.get_displacement_field()



# plot:
plt.close('all')
colors    = '0.0', (0.3,0.5,0.99)
ylimt     = (-7, 7)
ylim      = [ (-5, 30), (-5, 30), (-0.3, 0.3), ylimt, (-2, 30), ylimt, ylimt ]
alpha_x   = [70, 70, 70, 70]
leg_loc   = [(0.99, 0.92), (0.99, 0.92), (0.99, 0.29)]
nl.plot.plot_multipanel(y, yr, d, J, colors, ylim, alpha_x, paired=False, dvlabel='Dependent variable value', leg_loc=leg_loc)
plt.show()
if save:
	plt.savefig( os.path.join(nl.dirFIGS, f'{dataset.name}.pdf')  )



