from qutip import *
import numpy as np

#Lattice size 

L = 3 #2 by 2 lattice
nqubits = L*L #calculates the total number of qubits on the lattice edges, for L = 2 there are 4 edges and therefore 4 qubit edges

#this creates a lattice of this form 

 #   •---•---•
 #   |       |        
 #   |       |
 #   •---•---•

#where its a 2x2 lattice, each vertex is a dot and  _ is a horizontal edge and  | is a vertical edge

#act on a single qubit and do nothing to the states of the others
def single_operator(op, index, nqubits):
    "apply operator 'op' to to qubit at 'index'"
    ops = [qeye(2) for _ in range(nqubits)] #apply the 2x2 identity matrix to all the qubits
    ops[index] = op #apply the desired operator at index
    return tensor(ops) #construct the full operator as a tensor product of the individual operators

#create the "star operator" which is the product of the sigma x of the 4 spins that make up a star on the lattice
def star(vertex,L):
    "constructs the star operator A_s"

    indices= [vertex,(vertex+L) %nqubits, #vertical edges
    (vertex+1)%nqubits,(vertex-L+nqubits)%nqubits] #horizontal edges 
    A_s = tensor([qeye(2) for _ in range(nqubits)]) #apply identity matrix to all qubits and then create the tensor product of all the identity matrices
    for idx in indices:
        A_s *= single_operator(sigmax(),idx,nqubits)
    return A_s
#create the plaquette operator which  is the product of the sigma z of the 4 spins that make up a square on the lattice
def plaq(face,L):
    "constructs the plaquette operator B_p"
    indices = [face,(face+L)%nqubits, #vertical edges
               (face+L+1)%nqubits,(face+1)%nqubits] #horizontal edges
    B_p = tensor([qeye(2) for _ in range(nqubits)])
    for idx in indices:
        B_p *= single_operator(sigmaz(),idx,nqubits)
    return B_p

#construct the hamiltonian
H = 0
for i in range(nqubits):
    H -=star(i,L)
    H -=plaq(i,L)
#diagonalize the hamiltonian
    eigenenergies,eigenstates = H.eigenstates()
    
print("Eigenenergies:",eigenenergies)
print("Eigenstates:", eigenstates)