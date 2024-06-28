from qiskit_aer.primitives import Estimator
from qiskit.quantum_info import Pauli
from qiskit import QuantumCircuit
qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0,1)
qc.draw(output='mpl') 

ZZ = Pauli('ZZ')
ZI = Pauli('ZI')
IZ = Pauli('IZ')
XX = Pauli('XX')
XI = Pauli('XI')
IX = Pauli('IX')

observables = [ZZ, ZI, IZ, XX, XI, IX]
estimator = Estimator()

job = estimator.run([qc] * len(observables), observables)

#print(job.result())

import matplotlib.pyplot as plt

data = ['ZZ', 'ZI', 'IZ', 'XX', 'XI', 'IX']

values = job.result().values

plt.plot(data, values, '-o')
plt.xlabel('Observables')
plt.ylabel('Expectation value')
plt.show()