---
interest: medium
link: https://arxiv.org/abs/2607.18340
next_step: skim
priority: low
slack_ts: '1784863635.394509'
source: cs.CR - Cryptography and Security
status: unread
title: 'Quantum Cryptanalysis on IBM Quantum Hardware: Extending Even--Mansour Period
  Recovery from $N=4$ to $N=10$'
---
# Quantum Cryptanalysis on IBM Quantum Hardware: Extending Even--Mansour Period Recovery from $N=4$ to $N=10$
> 原文: [https://arxiv.org/abs/2607.18340](https://arxiv.org/abs/2607.18340)

arXiv:2607.18340v1 Announce Type: new
Abstract: We report genuine-un-compiled, textbook-faithful-quantum cryptanalysis of symmetric-cipher structures executed on real IBM quantum hardware (ibm\\_kingston, Heron generation). Using Simon's algorithm we recover the hidden period of the Even-Mansour cipher up to security parameter N = 10 on real hardware, beyond the largest previously reported real-hardware key recovery of N = 4, and we cleanly recover the periods of a 3-round Feistel (DES-family) construction at block sizes 6 and 8; a 21-qubit block-10 instance is verified in simulation and submitted to hardware. We further provide a breadth-first benchmark of five genuine quantum attacks spanning four symmetric-cipher design paradigms -- Bernstein-Vazirani (linear structure, single query), Grover (SPN key search, quadratic), and Simon (Even-Mansour, CBC-MAC forgery, and Feistel; exponential-to-polynomial in query complexity) -- validated to the classical-simulation ceiling of 25 qubits. We are deliberately explicit about scope: these attacks target reduced or structured constructions in the Q2 (quantum-query) model, asymptotically follow the birthday bound and therefore do not constitute quantum advantage over classical collision-finding, do not break full AES/RSA or 16-round DES, and rely on error mitigation rather than fault-tolerant error correction. Our contribution is the real-hardware demonstration at record structure sizes, the breadth of genuine algorithmic coverage across four paradigms, and an honest, reproducible benchmark with public artifacts.
