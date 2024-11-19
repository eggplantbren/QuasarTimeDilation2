import numpy as np
import matplotlib.pyplot as plt
import dnest4.classic as dn4
dn4.postprocess(rng_seed=0)

posterior_sample = np.loadtxt("posterior_sample.txt")

# Set up fonts
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 14
plt.rc("text", usetex=True)

beta0 = posterior_sample[:,0]
beta1 = posterior_sample[:,1]
beta2 = posterior_sample[:,2]
beta12 = posterior_sample[:,3]
n = posterior_sample[:,4]

lamb = np.linspace(np.log10(800), np.log10(7000), 1001)
lbol = np.linspace(44.8, 47.2, 1001)
lamb, lbol = np.meshgrid(lamb, lbol)
lbol = lbol[::-1, :]

data = np.loadtxt("data.txt")
z_data = data[:,0]
lbol_data = data[:,1]
lamb_data = data[:,2]

ftot = np.zeros(lamb.shape)
for i in range(len(beta0)):
    f = beta0[i] + beta1[i]*(lamb - lamb_data.mean()) + beta2[i]*(lbol - lbol_data.mean()) \
                    + beta12[i]*(lamb - lamb_data.mean())*(lbol - lbol_data.mean()) \
                    + n[i]*(np.log10(1.0 + 0) - np.mean(np.log10(1.0 + z_data)))

    ftot += f
    print(i+1, flush=True)

fmean = ftot/len(beta0)

plt.imshow(fmean, aspect="auto", extent=[lamb.min(), lamb.max(), lbol.min(), lbol.max()],
            cmap="viridis", vmin=2.2, vmax=3.6)
plt.plot(lamb_data, lbol_data, "wo", markersize=7, alpha=0.3)
plt.xlabel("$\\log_{10}(\\lambda/\\textnormal{\\AA})$")
plt.ylabel("$\\log_{10}(L_{\\rm bol}/{\\rm (erg/s)})$")
cbar = plt.colorbar()
cbar.set_label("$\\log_{10}(\\tau/\\textrm{days})$")
plt.savefig("surface.pdf", pad_inches=0.2, bbox_inches="tight")
plt.show()


#lamb = np.linspace(1400, 4400, 4)
#lbol = np.linspace(45.45, 46.95, 4)
#lamb, lbol = np.meshgrid(lamb, lbol)
#lbol = lbol[::-1, :]

#for row in range(lbol.shape[0]):
#    for col in range(lbol.shape[1]):
#        plt.plot(lamb[row, col], lbol[row, col], "w*", markersize=15, alpha=0.8)

#plt.show()

#f = beta0.mean() + beta1.mean()*(lamb - lamb_data.mean()) + beta2.mean()*(lbol - lbol_data.mean()) \
#                + beta12.mean()*(lamb - lamb_data.mean())*(lbol - lbol_data.mean())

#print(lamb)
#print(lbol)
#print(f)
