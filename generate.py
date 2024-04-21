"""
Generate a simple example of the quasar time dilation data.
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rng
import pandas as pd

# Set random seed
rng.seed(123)

# Number of quasars
N = 1000

# Cosmology parameter
n = 1.0

# Generate some redshifts from a lognormal distribution
z = np.exp(0.3*rng.randn(N))

# Generate some 'true' variability timescales (in 'days')
log10_tau_restframe = 2.0 + 0.1*rng.randn(N)

# Apply the redshift
log10_tau_now = log10_tau_restframe + n*np.log10(1.0 + z)

# Measurement noise
log10_tau_measured = log10_tau_now + 0.1*rng.randn(N)

# Save as CSV
data = pd.DataFrame()
data["z"] = z
data["log10_tau_lower"] = log10_tau_measured - 0.1
data["log10_tau_mid"] = log10_tau_measured
data["log10_tau_upper"] = log10_tau_measured + 0.1
data.to_csv("data.csv", index=False)
np.savetxt("data.txt", data)

plt.errorbar(z, log10_tau_measured, fmt="o", yerr=0.1,  alpha=0.3)
plt.show()


