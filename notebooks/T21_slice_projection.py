import numpy as np
import matplotlib.pyplot as plt
import ninja as nj


SIM_NAME = "L200N64_DMO"
REDSHIFT = 0
SLICE_AXIS = 0      # 0 for x, 1 for y, 2 for z
SLICE_SPAN = (0.3,0.7)   # in box size unit: (0,1) for full box, (0.25,0.75) for middle half of the box, etc. 


# Read fields
part = nj.Simulation(name=SIM_NAME).PART(z=REDSHIFT)
part.print_box_info()
dm_pos = part.DarkMatter.Position(print_read=True)

box_size = part.Header.BoxSize()
box_range = np.array(SLICE_SPAN)*box_size 
axis_cdn = dm_pos[:,SLICE_AXIS]
mask = (box_range[0]<=axis_cdn) & (axis_cdn<=box_range[1])
x,y,z = dm_pos[mask].T
u,v = {0:(y,z), 1:(z,x), 2:(x,y)}[SLICE_AXIS]

# convert kpc/h to Mpc/h
u /= 1000
v /= 1000

# Plot the slice
plt.figure(figsize=(8,8))
plt.scatter(u,v,s=1,c='k',alpha=0.1)

plt.xlabel({0:"y (Mpc/h)", 1:"z (Mpc/h)", 2:"x (Mpc/h)"}[SLICE_AXIS])
plt.ylabel({0:"z (Mpc/h)", 1:"x (Mpc/h)", 2:"y (Mpc/h)"}[SLICE_AXIS])
slc_dir = {0:"x", 1:"y", 2:"z"}[SLICE_AXIS]
plt.title(f"Slice Projection of DM Particles\n{SIM_NAME} at z={REDSHIFT}\nwith {slc_dir} in [{box_range[0]:.2f}, {box_range[1]:.2f}] Mpc/h")
plt.xlim(0, box_size/1000)
plt.ylim(0, box_size/1000)

plt.show()




