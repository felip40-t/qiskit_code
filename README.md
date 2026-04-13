# Quantum Software Development Internship

**University of Manchester · Jun – Aug 2024**

Eight-week internship project exploring quantum algorithm implementation and quantum error correction (QEC) using IBM's Qiskit framework. Weeks 1–4 cover foundational quantum algorithms; Weeks 5–8 focus on the theory and practical limitations of QEC codes, culminating in tests on real IBM Quantum hardware.

All code is in Jupyter notebooks. There are no tests or production-ready components — this is exploratory research code.

---

## Notebooks

### Week 1 — Foundations

| Notebook | Description |
|---|---|
| `week_1.ipynb` | Overview notebook: GHZ states, Pauli observables, IBM Runtime sketch |
| `Quantum_circuits.ipynb` | Basic Qiskit circuits: single-qubit gates, CNOT, Sampler primitive |
| `multiple_systems.ipynb` | Multi-qubit statevectors, tensor products, partial measurement |
| `superdense_coding.ipynb` | Superdense coding protocol (2 classical bits via 1 qubit + entanglement) |
| `teleportation.ipynb` | Quantum teleportation with random input state and verification |

### Week 2 — Quantum Algorithms

| Notebook | Description |
|---|---|
| `Deutsch.ipynb` | Deutsch's algorithm: constant vs balanced one-bit function |
| `Deutsch_Josza.ipynb` | Deutsch-Jozsa: generalised to n-bit inputs |
| `Bernstein_Vazarani.ipynb` | Bernstein-Vazirani: recovers hidden bitstring in one query |
| `Toffoli.ipynb` | Toffoli gate and its 2-qubit decomposition (CSX/CX) |
| `fredkin_gate.ipynb` | Fredkin (controlled-SWAP) gate decomposed into elementary gates |
| `Ex_4_27.ipynb` | Textbook exercise: Fredkin from Toffoli gates, unitary verification |

### Week 3 — QFT and Phase Estimation

| Notebook | Description |
|---|---|
| `QFT.ipynb` | Quantum Fourier Transform: circuit construction and unitary verification |
| `Phase-estimation.ipynb` | QPE algorithm on ideal and fake backends |
| `Phase-estimation-real.ipynb` | QPE results retrieved from IBM Osaka QPU job (token removed, job ID preserved) |

### Week 4 — Quantum Error Correction: Building Blocks

| Notebook | Description |
|---|---|
| `2-qubit-bitflip-code.ipynb` | Minimal 2-qubit repetition code: error detection only |
| `3-qubit-bitflip-code.ipynb` | 3-qubit bit-flip correction code |
| `3-qubit-phaseflip-code.ipynb` | 3-qubit phase-flip correction code (Hadamard basis) |
| `422-detection-code.ipynb` | [[4,2,2]] error detecting code: detects but cannot correct errors |
| `913-shor-code.ipynb` | 9-qubit Shor code: corrects both bit-flip and phase-flip errors |
| `n-qubit-bitflip-code.ipynb` | Parameterised n-qubit repetition code |

### Week 5 — The 5-Qubit Code and Hardware Testing

| Notebook | Description |
|---|---|
| `5-qubit-code.ipynb` | [[5,1,3]] Laflamme perfect code: full encode/error/syndrome/decode pipeline, ideal simulation |
| `5-qubit-code-advanced.ipynb` | Same code on fake backend + IBM Osaka QPU. Real hardware results were noise-dominated. |
| `Steane-code.ipynb` | [[7,1,3]] Steane CSS code: corrects any single-qubit error, 6 ancilla qubits |
| `422-detection-code.ipynb` | (see Week 4) |
| `Expectation-value.ipynb` | Expectation value sampling with EstimatorV2 on a fake backend; results saved to CSV |
| `Expectation-value-QEC.ipynb` | 8-qubit variant of the above for comparing QEC stability |
| `estimator-experiment.ipynb` | EstimatorV2 job on real IBM hardware (IQP circuit); token removed |

### Results summary

Simulations on `AerSimulator` (ideal) and fake backends (`GenericBackendV2`) worked as expected for all implemented codes. Tests on the IBM Osaka QPU showed that current hardware noise levels (particularly during encoding and decoding steps) make the 5-qubit Laflamme code impractical at this scale — syndrome distributions on real hardware were near-random, indicating the physical error rate exceeds the code's correction threshold.

---

## Setup

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### IBM Quantum credentials

Several notebooks connect to IBM Quantum hardware. To run them you need an IBM Quantum account. There are two ways to authenticate:

**Option 1 — environment variable (recommended):**
```bash
export IBM_QUANTUM_TOKEN="your_token_here"
```
Then in the notebook:
```python
import os
from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService(channel='ibm_quantum', token=os.environ['IBM_QUANTUM_TOKEN'])
```

**Option 2 — saved account (persists across sessions):**
```python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(channel='ibm_quantum', token='your_token_here')
# After saving once, subsequent calls just use: QiskitRuntimeService()
```

Tokens are available from [IBM Quantum account page](https://quantum.ibm.com/account).

### Run notebooks

```bash
source .venv/bin/activate
jupyter lab
```
