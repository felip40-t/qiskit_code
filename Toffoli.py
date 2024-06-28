# %%
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Statevector, Operator
from qiskit.visualization import array_to_latex
from qiskit_aer import AerSimulator
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram

# %%
Qubits = QuantumRegister(3)
Cbits = ClassicalRegister(3)

Toffoli = QuantumCircuit(Qubits, Cbits)

#Toffoli.x(0)
#Toffoli.x(1)
#Toffoli.x(2)

Toffoli.h(2)
Toffoli.cx(1,2)
Toffoli.tdg(2)
Toffoli.cx(0,2)
Toffoli.t(2)
Toffoli.cx(1,2)
Toffoli.tdg(2)
Toffoli.cx(0,2)
Toffoli.tdg(1)
Toffoli.t(2)
Toffoli.h(2)
Toffoli.cx(0,1)
Toffoli.tdg(1)
Toffoli.cx(0,1)
Toffoli.t(0)
Toffoli.s(1)

display(Toffoli.draw(output='mpl'))



# %%
U = Operator(Toffoli)

display(array_to_latex(U))

# %%
Toffoli.measure(0,0)
Toffoli.measure(1,1)
Toffoli.measure(2,2)

# %%
results = Sampler().run(Toffoli).result()
statistics = results.quasi_dists[0].binary_probabilities()
display(plot_histogram(statistics))


