---
title: "Static Detection of Post-Quantum Cryptographic Algorithms in Stripped Binaries for Digital Forensic Examination and Migration Assurance"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.25122
priority: low
status: unread
interest: medium
next_step: skim
---
# Static Detection of Post-Quantum Cryptographic Algorithms in Stripped Binaries for Digital Forensic Examination and Migration Assurance
> 原文: [https://arxiv.org/abs/2608.25122](https://arxiv.org/abs/2608.25122)

arXiv:2608.25122v1 Announce Type: new
Abstract: Currently, there is no method to verify from compiled binary code whether a quantum-vulnerable algorithm has been replaced by an approved post-quantum algorithm. Cryptographic discovery tools identify algorithms by symbols, library dependencies, and runtime behaviour; however, all these signals are destroyed by stripping, statically linking, and optimising a binary. This paper presents Kestrel, a static analysis method for identifying the standardised lattice-based schemes ML-KEM and ML-DSA in stripped binary code. Kestrel identifies ML-KEM and ML-DSA by detecting the number-theoretic transform constant tables that form the read-only data upon which the arithmetic depends. The fingerprints Kestrel derives from public scheme parameters are localised by means of a normalisation-and-multiset-matching procedure; the false-positive probability is established analytically. In experiments on four independent implementation lineages and all build transformations, including compiler-level obfuscation, Kestrel achieved recall of 128 of 128 with zero false positives. Applying Kestrel to 6,224 binaries on a production Linux system disclosed twelve uncatalogued programs containing ML-KEM; these included the OpenSSH key-exchange program and the container-management stack. In several of these programs, post-quantum code entered production through the language runtime without the awareness of the projects distributing them. Kestrel distinguishes genuine post-quantum implementations from advertised claims not backed by the underlying code, attributes each detection to its originating codebase, and, in a forensic disk-image trial, recovered a detection from unallocated space after the deleted binary could no longer be reconstructed. Thus, Kestrel provides a practical basis for cryptographic migration assurance, software supply-chain inspection, and post-quantum forensic examination.
