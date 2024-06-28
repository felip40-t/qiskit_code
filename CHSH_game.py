from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer.primitives import Sampler
from numpy import pi
from numpy.random import randint

def chsh_game(strategy):
    
    # referee chooses x and y (questions) randomly:
    x, y = randint(0,2), randint(0,2)

    # use strategy to choose a and b
    a, b = strategy(x, y)

    # winning condition
    if (a != b) == (x & y):
        return 1 # win
    return 0 # lose

def chsh_circuit(x, y):
    # generate bell state first
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0,1)
    qc.barrier()

    # Alice
    if x == 0:
        qc.ry(0, 0)
    else:
        qc.ry(-pi/2, 0)
    qc.measure(0, 0)

    # Bob
    if y == 0:
        qc.ry(-pi/4, 1)
    else:
        qc.ry(pi/4, 1)
    qc.measure(1, 1)

    return qc

"""
print("(x, y) = (0, 0)")
chsh_circuit(0, 0).draw(output='mpl', filename="0_0_chsh.png")


print("(x, y) = (0, 1)")
chsh_circuit(0, 1).draw(output='mpl', filename="0_1_chsh.png")


print("(x, y) = (1, 0)")
chsh_circuit(1, 0).draw(output='mpl', filename="1_0_chsh.png")


print("(x, y) = (1, 1)")
chsh_circuit(1, 1).draw(output='mpl', filename="1_1_chsh.png")
"""
sampler = Sampler()

def quantum_strategy(x,y):
    # shots=1 runs the circuit once
    result = sampler.run(chsh_circuit(x, y), shots=1).result()
    statistics = result.quasi_dists[0].binary_probabilities()
    bits = list(statistics.keys())[0]
    a, b = bits[0], bits[1]
    return a, b


NUM_GAMES = 1000
TOTAL_SCORE = 0

for _ in range(NUM_GAMES):
    TOTAL_SCORE += chsh_game(quantum_strategy)

print("Fraction of games won:", TOTAL_SCORE / NUM_GAMES)