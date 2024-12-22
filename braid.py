import numpy as np
from qutip import *
import matplotlib.pyplot as plot

#initial state of the system
initial_state=basis(2,0) #|0> state in 2d hilbert space

theta = np.pi/2 #braiding angle(can be adjusted)
braiding_operator = (-1j*theta/2*sigmax()).expm() #e^(-ithetasigmax/2)
final_state = braiding_operator*initial_state

#apply braiding operator to the initial state
print("initial state:")
print(initial_state)
print("\nbraiding operator:")
print(braiding_operator)
print("\nFinal state after braiding")
print(final_state)

#output should be a superposition of |0> and |1> with a phase factor of 1/sqrt(2)|0>-i/sqrt(2)|1>
#visualize the bloch sphere before and after braiding
b = Bloch()
b.add_states(initial_state,kind='point')
b.add_states(final_state,kind='point')
b.show()
plot.show()
eigenvalues, eigenstates = braiding_operator.eigenstates()
print("Eigenvalues:", eigenvalues)
for i, state in enumerate(eigenstates):
    print(f"Eigenstate {i} (eigenvalue = {eigenvalues[i]}):\n", state)


#mixed state
# initial_state= basis(2,0) #|0> state in 2d hilbert space
# state_2= basis(2,1) #|1> state in 2d hilbert space

# theta = np.pi/3 #braiding angle(can be adjusted)
# braiding_operator = (-1j*theta/2*sigmaz()).expm() #e^(-ithetasigmax/2)
# final_state = braiding_operator*(0.3*initial_state+0.7*state_2)

#mixed state with relative phase
# initial_state= basis(2,0) #|0> state in 2d hilbert space
# state_2= basis(2,1) #|1> state in 2d hilbert space

# theta = np.pi/3 #braiding angle(can be adjusted)
# braiding_operator = (-1j*theta/2*sigmaz()).expm() #e^(-ithetasigmax/2)
# final_state = braiding_operator*(0.3*initial_state+0.7*np.exp(-1j*2/5*np.pi)*state_2)