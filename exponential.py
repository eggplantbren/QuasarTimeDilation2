import numpy as np
import matplotlib.pyplot as plt

# Set up fonts
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 14
plt.rc("text", usetex=True)

x = np.linspace(-20.0, 20.0, 20001)

# Median and credible interval
mu = 3.0
x_l = 2.5
x_r = 3.4

beta_l = (mu - x_l)/1.1394
beta_r = (x_r - mu)/1.1394
print(beta_l, beta_r)

p = np.empty(x.shape)
p[x < mu]  = 1.0/(2.0*beta_l)*np.exp((x[x<mu] - mu) / beta_l)
p[x >= mu] = 1.0/(2.0*beta_r)*np.exp(-(x[x>=mu] - mu) / beta_r)


# These integrals should be 0.16, 0.5, 0.84, 1
print(np.trapz(p[x <= x_l], x=x[x <= x_l]))
print(np.trapz(p[x <= mu], x=x[x <= mu]))
print(np.trapz(p[x <= x_r], x=x[x <= x_r]))
print(np.trapz(p, x=x))

plt.plot(x, p, color="k", linewidth=2)
plt.xlim([0.0, 5.0])
plt.ylim(bottom=-0.02)
plt.xlabel("$x$")
plt.ylabel("$p(x)$")
plt.axvline(mu, color="b", linestyle="-", linewidth=3, alpha=0.5)
plt.axvline(x_l, color="r", linestyle="--", linewidth=3, alpha=0.5)
plt.axvline(x_r, color="r", linestyle="--", linewidth=3, alpha=0.5)
plt.savefig("exponential.pdf")
plt.show()
