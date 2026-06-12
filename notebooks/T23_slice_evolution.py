import numpy as np
import matplotlib.pyplot as plt
import ninja as nj
from T22_slice_compare import get_slice

# Upto 8 Redshifts (2 rows x 4 columns)
REDSHIFTS = [10,5,3,2,1,0.5,0.1,0]
SIM_NAME = "L200N64_DMO"
AXIS = 0
SPAN = (0,1)

fig,axs = plt.subplots(2,4,figsize=(16,8), sharex=True, sharey=True)

sim = nj.Simulation(name=SIM_NAME)

for i, z in enumerate(REDSHIFTS):
    part = sim.PART(z=z)
    print(f"Reading {part.snap_name} at z={z}...")
    pos = part.DarkMatter.Position()
    box_size = part.Header.BoxSize()
    u,v = get_slice(*pos.T, axis=AXIS, boxsize=box_size, span=SPAN)

    pig = sim.PIG(z=z)
    fof_pos = pig.FOFGroups.MassCenterPosition()
    fof_u, fof_v = get_slice(*fof_pos.T, axis=AXIS, boxsize=box_size, span=SPAN)
    
    ax = axs[i//4, i%4]
    ax.scatter(u/1000, v/1000, s=1, c='k', alpha=0.01)
    ax.scatter(fof_u/1000, fof_v/1000, s=5, c='r', alpha=0.5)

    ax.set_title(f"z={z}")
    ax.set_aspect('equal')
    ax.set_xlim(0, box_size/1000)
    ax.set_ylim(0, box_size/1000)

axs[0,0].figure.supxlabel({0:"y (Mpc/h)", 1:"z (Mpc/h)", 2:"x (Mpc/h)"}[AXIS],fontsize=12)
axs[0,0].figure.supylabel({0:"z (Mpc/h)", 1:"x (Mpc/h)", 2:"y (Mpc/h)"}[AXIS],fontsize=12)
plt.suptitle(f"DM Particles Slice Projection Evolution for {SIM_NAME}", fontsize=16)

plt.show()










