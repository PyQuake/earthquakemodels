from mpi4py import MPI
target = 0
info = MPI.Status()
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
origin = (rank - (target+1)) % size
dest = (rank + ((target+1) + size)) % size

mpi_info = MPI.Info.Create()
mpi_info.Set("add-hostfile", "hosts.txt")
print(MPI.Get_processor_name())
