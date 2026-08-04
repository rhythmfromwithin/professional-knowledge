---
title: "Bridging the Gap Between PHE and FHE: A Performance and Trade-off Analysis of The Somewhat Homomorphic BGN Cryptosystem"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.28700
priority: low
status: unread
interest: medium
next_step: skim
---
# Bridging the Gap Between PHE and FHE: A Performance and Trade-off Analysis of The Somewhat Homomorphic BGN Cryptosystem
> 原文: [https://arxiv.org/abs/2607.28700](https://arxiv.org/abs/2607.28700)

arXiv:2607.28700v1 Announce Type: new
Abstract: Homomorphic encryption (HE) enables privacy-preserving data analytics, but practitioners often face a trade-off between lightweight Partially Homomorphic Encryption (PHE) and computationally dominant Fully Homomorphic Encryption (FHE). The Boneh-Goh-Nissim (BGN) cryptosystem bridges this gap as a Somewhat Homomorphic Encryption (SWHE) scheme supporting unlimited additions and one ciphertext multiplication. Despite its algebraic elegance, practical BGN adoption has been hindered by a lack of accessible software implementations. This paper presents a comparative analysis of BGN against PHE and FHE paradigms through its integration into the lightphe Python framework, allowing deployment in just a few lines of code. We benchmark encrypted 128-dimensional vector operations under 80-bit, 112-bit and 128-bit security levels against Paillier, Damgard-Jurik, Okamoto-Uchiyama, and the FHE CKKS scheme via TenSEAL. Results reveal a computation-communication trade-off: BGN is computationally slower due to bilinear pairings compared to PHE and SIMD-optimized FHE, but retains a microscopic public key size of 3-6 KB, up to five orders of magnitude smaller than FHE. Crucially, BGN enables boundless homomorphic aggregation after a single multiplication, supporting complex tasks such as linear regression inference, Cosine Similarity, and Squared Euclidean Distance. Furthermore, an optimized precision of 2 digits suffices to match plaintext ranking baselines, overcoming the target-group discrete logarithm decryption bottleneck. By open-sourcing this pipeline in lightphe, this work establishes BGN as a practical engine for bandwidth-constrained, decentralized architectures.
