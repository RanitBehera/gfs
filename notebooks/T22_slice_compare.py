import numpy as np
import matplotlib.pyplot as plt
import ninja as nj

def get_slice(x,y,z,axis,boxsize,span):
    box_range = np.array(span)*boxsize 
    axis_cdn = {0:x, 1:y, 2:z}[axis]
    mask = (box_range[0]<=axis_cdn) & (axis_cdn<=box_range[1])
    xx,yy,zz = x[mask], y[mask], z[mask]
    u,v = {0:(yy,zz), 1:(zz,xx), 2:(xx,yy)}[axis]
    return u, v

def annotate_figure_axis(ax, axis,boxsize,title=""):
    ax.set_xlabel({0:"y (Mpc/h)", 1:"z (Mpc/h)", 2:"x (Mpc/h)"}[axis])
    ax.set_ylabel({0:"z (Mpc/h)", 1:"x (Mpc/h)", 2:"y (Mpc/h)"}[axis])
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.set_xlim(0, boxsize)
    ax.set_ylim(0, boxsize)

if __name__ == "__main__":
    REDSHIFT = 0
    AXIS = 0
    SPAN = (0.3,0.7)
    PUT_HALOS = True

    dmo = nj.Simulation(name="L200N64_DMO")
    hydro = nj.Simulation(name="L200N64_Hydro")

    dmo_pos = dmo.PART(z=REDSHIFT).DarkMatter.Position(print_read=True)
    hydro_part = hydro.PART(z=REDSHIFT).DarkMatter.Position(print_read=True)
    
    dmo_box_size = dmo.PART(z=REDSHIFT).Header.BoxSize()
    hydro_box_size = hydro.PART(z=REDSHIFT).Header.BoxSize()

    dmo_u, dmo_v = get_slice(*dmo_pos.T, AXIS, dmo_box_size, SPAN)
    hydro_u, hydro_v = get_slice(*hydro_part.T, AXIS, hydro_box_size, SPAN)

    if PUT_HALOS:
        dmo_fof_pos = dmo.PIG(z=REDSHIFT).FOFGroups.MassCenterPosition(print_read=True)
        hydro_fof_pos = hydro.PIG(z=REDSHIFT).FOFGroups.MassCenterPosition(print_read=True)

        dmo_fof_u, dmo_fof_v = get_slice(*dmo_fof_pos.T, AXIS, dmo_box_size, SPAN)
        hydro_fof_u, hydro_fof_v = get_slice(*hydro_fof_pos.T, AXIS, hydro_box_size, SPAN) 

    
    ##############################
    # PLOT
    ##############################
    fig,axs = plt.subplots(1,2,figsize=(12,6), sharex=True, sharey=True)
    axs_dmo, axs_hydro = axs

    axs_dmo.scatter(dmo_u/1000, dmo_v/1000, s=1, c='k', alpha=0.1)
    annotate_figure_axis(axs_dmo, AXIS, dmo_box_size/1000, title=f"{dmo.sim_name} at z={REDSHIFT}")

    axs_hydro.scatter(hydro_u/1000, hydro_v/1000, s=1, c='k', alpha=0.1)
    annotate_figure_axis(axs_hydro, AXIS, hydro_box_size/1000, title=f"{hydro.sim_name} at z={REDSHIFT}")

    if PUT_HALOS:
        axs_dmo.scatter(dmo_fof_u/1000, dmo_fof_v/1000, s=20, c='r', alpha=0.5, label="FoF Halos")
        axs_hydro.scatter(hydro_fof_u/1000, hydro_fof_v/1000, s=20, c='r', alpha=0.5, label="FoF Halos")


    plt.suptitle(f"Comparision of Slice Projection of DM Particles")

    plt.show()


