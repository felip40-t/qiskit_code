# Quantum software development internship at the University of Manchester

**Date:** Jun - Aug 2024

## Abstract 

This repository contains the code developed during an 8-week internship project focused on quantum software development using IBM’s Qiskit in Python. The project explores the implementation and limitations of various quantum error correction (QEC) codes, culminating in an analysis of the "perfect" 5-qubit code on real quantum hardware.

## Project Overview
The repository is structured to follow the progression of the internship:

- Weeks 1-4: Canonical Algorithms: Implementation of foundational quantum algorithms.

- Week 5-8: Quantum Error Correction: Deep dive into the mathematical theory and practical implementation of QEC.

## Key Implementations & Research

- 3-Qubit Codes: Developed the 3-qubit bit-flip and phase-flip codes, utilizing entanglement and syndrome measurements to identify errors via ancilla qubits.

- 9-Qubit Shor Code: Implemented the first code capable of correcting both bit-flip and phase-flip errors simultaneously by combining the 3-qubit code structures.

- The 5-Qubit Laflamme Code: Focused on the "perfect" 5-qubit code, which reaches the Quantum Hamming Bound for single-qubit error correction.

- Hardware Analysis: Conducted performance testing on the IBM Osaka QPU. While simulations on "fake" backends showed success, real-world execution revealed that current QPU noise levels (especially in encoding/decoding steps) lead to random syndrome distributions, highlighting the limitations of the 5-qubit code in non-idealised scenarios.
