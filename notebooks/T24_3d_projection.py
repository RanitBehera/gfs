import numpy as np
import matplotlib.pyplot as plt
import ninja as nj


SIM_NAME = "L200N64_DMO"
REDSHIFT = 0


box = nj.Simulation(name=SIM_NAME).PART(z=REDSHIFT)
pos = box.DarkMatter.Position()
box_size = box.Header.BoxSize()

fig, ax = plt.subplots(figsize=(8,8),subplot_kw={'projection': '3d'})
ax.scatter(*pos.T/1000, s=1, c='k', alpha=0.01)

ax.set_aspect('equal')
ax.set_xlim(0, box_size/1000)
ax.set_ylim(0, box_size/1000)
ax.set_zlim(0, box_size/1000)
ax.set_xlabel("x (Mpc/h)", fontsize=12)
ax.set_ylabel("y (Mpc/h)", fontsize=12)
ax.set_zlabel("z (Mpc/h)", fontsize=12)
ax.grid(False)

plt.show()