import sys
import socket
from mpi4py import MPI


def main():
    print("Calcular"+sys.argv[1]+"^"+sys.argv[2]+" mod "+sys.argv[3]+", con "+sys.argv[4]+" nodos corruptos")
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    if rank == 0:
        data = {'a': 7, 'b': 3.14}
        comm.send(data, dest=1, tag=11)
    elif rank == 1:
        data = comm.recv(source=0, tag=11)

if __name__ == "__main__":
    main()
