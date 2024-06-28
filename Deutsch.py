# %%
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.result import marginal_distribution
from qiskit.circuit.library import UGate
from numpy import pi, random

# %%
def deutsch_function(case: int):
    """
    Generate a valid Deutsch function as a `QuantumCircuit`.
    Each function is either constant or balanced.
    Function 1 is balanced
    Function 2 is constant
    Function 3 is constant
    Function 4 is balanced
    """
    if case not in [1, 2, 3, 4]:
        raise ValueError("`case` must be 1, 2, 3, or 4.")

    f = QuantumCircuit(2)
    if case in [2, 3]:
        f.cx(0, 1)
    if case in [3, 4]:
        f.x(1)
    return f

# %%
display(deutsch_function(1).draw())
display(deutsch_function(2).draw())
display(deutsch_function(3).draw())
display(deutsch_function(4).draw())


# %%
def compile_circuit(function: QuantumCircuit):
    """
    Compiles a circuit for use in Deutsch's algorithm.
    """
    n = function.num_qubits - 1
    qc = QuantumCircuit(n + 1, n)

    qc.x(n)
    qc.h(range(n + 1))

    qc.barrier()
    qc.compose(function, inplace=True)
    qc.barrier()

    qc.h(range(n))
    qc.measure(range(n), range(n))

    return qc

display(compile_circuit(deutsch_function(3)).draw(output='mpl'))

# %%
def deutsch_algorithm(function: QuantumCircuit):
    """
    determine if Deutsch function is constant or balanced
    """
    qc = compile_circuit(function)

    result = AerSimulator().run(qc, shots=1, memory=True).result()
    measurements = result.get_memory()
    if measurements[0] == "0":
        return "constant"
    return "balanced"

# %%
f = deutsch_function(4)
display(f.draw(output='mpl'))
display(deutsch_algorithm(f))


