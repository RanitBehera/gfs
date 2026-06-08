import numpy as np

def redshift_to_time(redshift):
    z = np.array(redshift)
    z = np.sort(z)[::-1]
    return 1 / (1 + z)

if __name__ == "__main__":
    # Add the redshift in the list for which you want a snapshot
    SNAP_REDSHIFTS = [50,30,20,15,14,13,12,11,10,9,8,7,6,5,4,3,2.5,2.0,1.5,1.0,0.5,0.25,0.1,0]

    times = redshift_to_time(SNAP_REDSHIFTS)
    output_list = ','.join([f"{time:.9f}" for time in times])
    print("Number of snapshots:", len(SNAP_REDSHIFTS))
    print(f"OutputList = {output_list}")