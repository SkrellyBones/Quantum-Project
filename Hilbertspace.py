#script to visualize a degenerate Hilbert space, in which multiple eigenstates share the same eigenvalue

from qutip import *
import numpy as np
 # Define a 2-level system 
N = 2 #Hilbert space dimension
 # Hamiltonian with degenerate eigenvalues
H = Qobj(np.zeros((N, N))) #Zero Hamiltonian, all eigenvalues are 0 and the system has an energy level of 0
#Initial states in the computational basis 
psi0 = basis(N, 0) #|0> 
psi1 = basis(N, 1) #|1> 
eigenvalues, eigenstates = H.eigenstates()
print("Eigenvalues:", eigenvalues)
for i, state in enumerate(eigenstates):
    print(f"Eigenstate {i} (eigenvalue = {eigenvalues[i]}):\n", state)
