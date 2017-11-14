import sys
import socket
from mpi4py import MPI

def main():
    print(socket.gethostname())

if __name__ == "__main__":
    main()
