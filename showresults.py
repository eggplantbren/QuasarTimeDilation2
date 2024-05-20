import numpy as np
import matplotlib.pyplot as plt
import dnest4.classic as dn4
dn4.postprocess()

posterior_sample = np.loadtxt("posterior_sample.txt")

C = posterior_sample[:,0]
beta1 = posterior_sample[:,1]
beta2 = posterior_sample[:,2]
beta12 = posterior_sample[:,3]

lamb = np.linspace(800, 7000, 1001)
lbol = np.linspace(44.8, 47.2, 1001)
lamb, lbol = np.meshgrid(lamb, lbol)
lbol = lbol[::-1, :]

data = np.loadtxt("data.txt")
lbol_data = data[:,1]
lamb_data = data[:,2]

f = C.mean() + beta1.mean()*(lamb - lamb_data.mean()) + beta2.mean()*(lbol - lbol_data.mean()) \
                + beta12.mean()*(lamb - lamb_data.mean())*(lbol - lbol_data.mean())

plt.imshow(f, aspect="auto", extent=[lamb.min(), lamb.max(), lbol.min(), lbol.max()],
            cmap="jet", vmin=2.2, vmax=3.6)
plt.plot(lamb_data, lbol_data, "ko", alpha=0.3)
plt.colorbar()
plt.show()

