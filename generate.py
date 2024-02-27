"""
Generate a simple example of the quasar time dilation data.
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rng

# Set random seed
rng.seed(123)

# Number of quasars
N = 1000

# Generate some redshifts from a lognormal distribution
z = np.exp(0.3*rng.randn(N))

# Generate some 'true' variability timescales (in 'days')
log10_tau = 2.0 + 0.3*rng.randn(N)



plt.hist(10.0**log10_tau, 100)
plt.show()
