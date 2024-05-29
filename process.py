import numpy as np
import pandas as pd

data = pd.read_csv("Quasar.csv")

for i in range(data.shape[0]):
    z = data["z"][i]

    lr_cols = ["lr_g_o", "lr_r_o", "lr_i_o"]
    tau_o_cols = ["tau_o_g", "tau_o_r", "tau_o_i"]
    tau_l_cols = ["tau_o_gl", "tau_o_rl", "tau_o_il"]
    tau_u_cols = ["tau_o_gu", "tau_o_ru", "tau_o_iu"]

    for j in range(3):
        lr = data[lr_cols[j]][i]
        lbol = data["lbol"][i]

        tau_o = data[tau_o_cols[j]][i]
        tau_l = tau_o - data[tau_l_cols[j]][i]
        tau_r = tau_o + data[tau_u_cols[j]][i]

        print(str(z) + " " + str(lbol) + " " + str(np.log10(lr)) + " "
                + str(tau_l) + " " + str(tau_o) + " " + str(tau_r))

