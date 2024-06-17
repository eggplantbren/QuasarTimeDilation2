# Corner plot
import corner
import matplotlib.pyplot as plt
import numpy as np

# Set up fonts
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 14
plt.rc("text", usetex=True)

posterior_sample = np.loadtxt("posterior_sample.txt")

corner.corner(posterior_sample,
    labels=["$\\beta_0$", "$\\beta_1$", "$\\beta_2$",
               "$\\beta_{12}$", "$n$", "$\\sigma$"], plot_contours=False,
        plot_density=False, fontsize=14)
plt.savefig("cornerplot.png", dpi=450)


## For small cornerplot with only beta3 and n
#corner.corner(posterior_sample[:, [6, 4]],
#                labels=["$\\beta_3$", "$n$"],
#                plot_density=False, plot_contours=False, fontsize=14)
#plt.savefig("cornerplot2.png")
