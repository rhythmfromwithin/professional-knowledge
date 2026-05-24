---
interest: medium
link: https://arxiv.org/abs/2605.22039
next_step: skim
priority: medium
slack_ts: '1779596249.432409'
source: cs.DC - Distributed Computing
status: unread
title: Secure and Parallel Determinant Computation for Large-Scale Matrices in Edge
  Environments
---
# Secure and Parallel Determinant Computation for Large-Scale Matrices in Edge Environments
> 原文: [https://arxiv.org/abs/2605.22039](https://arxiv.org/abs/2605.22039)

arXiv:2605.22039v1 Announce Type: new
Abstract: The advent of edge computing has enabled resource-constrained clients to delegate intensive computational tasks to distributed edge servers, especially within Internet of Things (IoT) environments. Among such tasks, Matrix Determinant Computation (MDC) remains critical for applications in control systems, cryptography, and machine learning. However, the cubic complexity of traditional determinant algorithms makes them unsuitable for real-time processing in constrained edge scenarios.
We propose a Secure Parallel Determinant Computation (SPDC) framework, which provides strong security guaranties, including privacy-preserving MDC, across N distributed edge servers. The framework achieves privacy through Composite Element Distortion (CED) - a lightweight encryption method that combines Element-wise Obfuscation (EWO) and the Panth Rotation Theorem (PRT) to conceal both structural and numerical matrix content while preserving determinant properties. Parallel LU decomposition is used to distribute encrypted matrix blocks across an arbitrary number of untrusted edge servers, enabling efficient and scalable determinant computation. A one-way communication model further reduces coordination overhead by eliminating inter-server interactions. To ensure result integrity with minimal client burden, we further introduce two verification algorithms: Q\_2, a probabilistic scalar method, and Q\_3, a deterministic and low-complexity alternative.
Mathematical analysis demonstrates that the proposed framework provides strong privacy and security guaranties, low computational overhead, and deployment flexibility - making it well-suited for secure, scalable, and real-time MDC in distributed edge-assisted systems.
