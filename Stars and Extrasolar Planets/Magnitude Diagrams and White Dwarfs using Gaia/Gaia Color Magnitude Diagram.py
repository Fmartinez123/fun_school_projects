import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Mag10 = []
Mag20 = []
Mag50 = []

BPRP10 = []
BPRP20 = []
BPRP50 = []

par10 = []
par20 = []
par50 = []

cmap10 = []
cmap20 = []
cmap50 = []


Gaia_10pc = pd.read_csv("Gaia_10_arc_sec.csv")
Gaia_20pc = pd.read_csv("Gaia_20_arc_sec.csv")
Gaia_50pc = pd.read_csv("Gaia_50_arc_sec.csv")

#Appending data from each of the csv's

full_Mag10 = Gaia_10pc.phot_g_mean_mag.values
full_BPRP10 = Gaia_10pc.phot_bp_mean_mag.values - Gaia_10pc.phot_rp_mean_mag
full_par10 = Gaia_10pc.parallax

full_Mag20 = Gaia_20pc.phot_g_mean_mag.values
full_BPRP20 = Gaia_20pc.phot_bp_mean_mag.values - Gaia_20pc.phot_rp_mean_mag
full_par20 = Gaia_20pc.parallax

full_Mag50 = Gaia_50pc.phot_g_mean_mag.values
full_BPRP50 = Gaia_50pc.phot_bp_mean_mag.values - Gaia_50pc.phot_rp_mean_mag
full_par50 = Gaia_50pc.parallax

#We are filtering any Data points with a Mag > 16, as Gaia stated on their Website that measurements above 16
#are subject to error

for i in range(len(Gaia_10pc)):
    if full_Mag10[i] > 16:
        pass
    else:
        Mag10.append(full_Mag10[i])
        BPRP10.append(full_BPRP10[i])
        par10.append(full_par10[i])

for i in range(len(Gaia_20pc)):
    if full_Mag20[i] > 16:
        pass
    else:
        Mag20.append(full_Mag20[i])
        BPRP20.append(full_BPRP20[i])
        par20.append(full_par20[i])

for i in range(len(Gaia_50pc)):
    if full_Mag50[i] > 16:
        pass
    else:
        Mag50.append(full_Mag50[i])
        BPRP50.append(full_BPRP50[i])
        par50.append(full_par50[i])

#Determining the distance EACH star is away from Earth

distance10 = np.abs(par10)/1000
colors10 = 1/distance10

distance20 = np.abs(par20)/1000
colors20 = 1/distance20

distance50 = np.abs(par50)/1000
colors50 = 1/distance50

for i in range(len(Mag10)):
    cmap10.append(colors10[i])

for i in range(len(Mag20)):
    cmap20.append(colors20[i])

for i in range(len(Mag50)):
    cmap50.append(colors50[i])

#Plotting out the 10 Parsecs CMD

plt.figure(figsize = [8,5])
plt.title('10 Parsecs Magnitude Diagram', fontsize = 20)
plt.scatter(BPRP10,Mag10, c = cmap10 , cmap = 'inferno_r',s=15)
plt.colorbar(label = 'Distance (Parsecs)', spacing = 'proportional')
plt.minorticks_on()
plt.ylim(16.5,0)
plt.xlabel('bp-rp')
plt.ylabel('Mv')

plt.savefig("10pc-Color-mag Diagram.png")
plt.show()

#Plotting out the 20 Parsecs CMD

plt.figure(figsize = [8,5])
plt.title('20 Parsecs Magnitude Diagram', fontsize = 20)
plt.scatter(BPRP20,Mag20, c = cmap20, cmap = 'inferno_r', s=15)
plt.minorticks_on()
plt.ylim(16.5,0)
plt.colorbar(label = 'Distance (Parsecs)', spacing = 'proportional')
plt.xlabel('bp-rp')
plt.ylabel('Mv')

plt.savefig("20pc-Color-mag Diagram.png")
plt.show()

#Plotting out the 50 Parsecs CMD

plt.figure(figsize = [8,5])
plt.title('50 Parsecs Magnitude Diagram', fontsize = 20)
plt.scatter(BPRP50,Mag50, c = cmap50, cmap = 'inferno_r', s = 15)
plt.minorticks_on()
plt.ylim(16.5,0)
plt.colorbar(label = 'Distance (Parsecs)', spacing = 'proportional')
plt.xlabel('bp-rp')
plt.ylabel('Mv')

plt.savefig("50pc-Color-mag Diagram.png")
plt.show()
