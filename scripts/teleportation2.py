
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
import numpy as np
import matplotlib.pyplot as plt

secret = QuantumRegister(1, "S")
Alice = QuantumRegister(1, "A")
Bob = QuantumRegister(1, "B")
 
clr = ClassicalRegister(3, "C")
 
qc = QuantumCircuit(secret, Alice, Bob, clr)
 
qc.h(Alice)
qc.cx(Alice, Bob)
 
qc.barrier()
 
np.random.seed(42)  
theta = np.random.uniform(0.0, 1.0) * np.pi 
varphi = np.random.uniform(0.0, 2.0) * np.pi  
 
qc.cx(secret, Alice)
qc.h(secret)
qc.barrier()
 
qc.measure(Alice, clr[1])
qc.measure(secret, clr[0])
 

with qc.if_test((clr[1], 1)):
    qc.x(Bob)
with qc.if_test((clr[0], 1)):
    qc.z(Bob)
 
qc.draw(output="mpl")
plt.show()