import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 14
plt.rc("text", usetex=True)

data = np.loadtxt("data.txt")
posterior_sample = np.loadtxt("posterior_sample.txt")

#data[:,4] = data[:,4]# - np.log10(1 + data[:,0])

plt.scatter(data[:,0], data[:,4], marker="o", alpha=0.5, c=data[:, 2])
plt.xlabel("$z$")
plt.ylabel("$\\log_{10}(\\tau/{\\rm days})$")

z = np.linspace(0.0, 4.3, 1001)

for i in range(min(100, posterior_sample.shape[0])):
    plt.plot(z, posterior_sample[i, 0] + posterior_sample[i, 4]*np.log10(1.0 + z), color="k", alpha=0.1)
plt.plot(z, 2.85 + 0.9*np.log10(1.0 + z), color="r", linewidth=3)
cbar = plt.colorbar()
cbar.set_label("$\\log_{10}(\\lambda/\\mathrm{Å})$")
plt.savefig("not_fitting.pdf")
plt.show()

