import numpy as np
import matplotlib.pyplot as plt
import tables
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.colors import Normalize

#MC_file = tables.open_file("Inputs/bb0nu_MC.h5",mode='r')
MC_file = tables.open_file("Inputs/Bi214_MC.h5",mode='r')

root = MC_file.root.MC
data = root
Nevents = len(data.events)

# Pull the extents so teh MC events can be sorted
DatL=[]
DatL.append(0)
for x in range(0,Nevents):
    DatL.append(data.extents[x]["last_hit"])


# for a specific event grab the hits
EVENT=2106
EVENT=2097
EVENT=2092

for EVENT in range(2106):
    print(EVENT)
    MC_Xhit = []
    MC_Yhit = []
    MC_Zhit = []
    MC_Ehit = []
    MC_Ihit = []

    for x in range(DatL[EVENT],DatL[EVENT+1]):

        MC_Xhit.append(data.hits[x]["hit_position"][0])
        MC_Yhit.append(data.hits[x]["hit_position"][1])
        MC_Zhit.append(data.hits[x]["hit_position"][2])
        MC_Ehit.append(data.hits[x]["hit_energy"])
        MC_Ihit.append(data.hits[x]["hit_time"])
    MC_Xhit = np.array(MC_Xhit)
    MC_Yhit = np.array(MC_Yhit)
    MC_Zhit = np.array(MC_Zhit)
    MC_Ehit = np.array(MC_Ehit)
    MC_Ihit = np.array(MC_Ihit)




    cmap = cm.viridis
    fig = plt.figure(figsize=(8,8))
    #ax = fig.add_subplot(111, projection='3d')
    ax = Axes3D(fig)

    sc = ax.scatter(MC_Xhit, MC_Yhit, MC_Zhit, c=MC_Ehit, s=35, cmap=cmap)

    ax.set_xlabel('X [mm]',fontsize=16)
    ax.set_ylabel('Y [mm]',fontsize=16)
    ax.set_zlabel('Z [mm]',fontsize=16)
    #plt.colorbar(sc)
    #ax.set_xlim(60,100)
    #ax.set_ylim(1050,1100)
    #ax.set_zlim(-1150,-1060)

    mx = np.mean(MC_Xhit)
    sx = np.std(MC_Xhit)
    ax.set_xlim(mx-1*sx,mx+1*sx)

    mx = np.mean(MC_Yhit)
    sx = np.std(MC_Yhit)
    ax.set_ylim(mx-1*sx,mx+1*sx)

    mx = np.mean(MC_Zhit)
    sx = np.std(MC_Zhit)
    ax.set_zlim(mx-1*sx,mx+1*sx)
    #ax.set_ylim(1050,1100)
    #ax.set_zlim(-1150,-1060)
    plt.show()
