export OMP_NUM_THREADS=2
mkdir -p stdout
outfile="stdout/restart_$(date +%Y%m%d_%H%M%S).txt"
nohup mpirun -np 4 MP-Gadget paramfile.gadget 1 > $outfile 2>&1 &
echo "Output: $outfile"
