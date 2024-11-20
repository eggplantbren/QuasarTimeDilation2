#%%
# Corner plot
import corner
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(plt.rcParamsDefault)


# Set up fonts
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 14
plt.rcParams["lines.markersize"] = 10
##plt.rc("text", usetex=True)

ndim = 6

posterior_sample = np.loadtxt("posterior_sample.txt")

figure = corner.corner(posterior_sample,
    labels=["$\\beta_0$", "$\\beta_1$", "$\\beta_2$",
               "$\\beta_{12}$", "$n$", "$\\sigma$"], plot_contours=False,
        plot_density=False, fontsize=14 , hist_kwargs={"color":"blue", "alpha":0.3, "histtype":"stepfilled", "edgecolor":"black","lw":"3"} )

axes = np.array(figure.axes).reshape((ndim, ndim))

for i in range(ndim):
	
	ax = axes[i,i]
	print( ax )

plt.savefig("cornerplot.png", dpi=450)


## For small cornerplot with only beta3 and n
#corner.corner(posterior_sample[:, [6, 4]],
#                labels=["$\\beta_3$", "$n$"],
#                plot_density=False, plot_contours=False, fontsize=14)
#plt.savefig("cornerplot2.png", dpi=450)


## For posterior histogram of beta3 when n is fixed to 1
#counts, bins, patches = plt.hist(posterior_sample[:,-1], bins=20, alpha=0.5, edgecolor=None)
#plt.xlabel("$\\beta_3$")
#plt.ylabel("Number of samples")
#plt.axvline(0.0, linestyle="--", color="r", linewidth=3)
#for i, patch in enumerate(patches):
#    # Get the x position, width, and height of each bar
#    x = patch.get_x()
#    width = patch.get_width()
#    height = patch.get_height()
#    
#    # Get heights of neighboring bars
#    if i == 0:
#        left_height = 0   #No left neighbor for the first bar
#    else:
#        left_height = patches[i - 1].get_height()
#    
#    if i == len(patches) - 1:
#        right_height = 0   #No right neighbor for the last bar
#    else:
#        right_height = patches[i + 1].get_height()
#    
#    # Draw a black line on the top of the bar
#    plt.plot([x, x + width], [height, height], color='black')
#    
#    # Draw the left edge, limited by the left neighbor's height
#    plt.plot([x, x], [left_height, height], color='black')
#    
#    # Draw the right edge, limited by the right neighbor's height
#    plt.plot([x + width, x + width], [right_height, height], color='black')

#plt.savefig("beta3.pdf")
#plt.savefig("beta3.png")


# %%
