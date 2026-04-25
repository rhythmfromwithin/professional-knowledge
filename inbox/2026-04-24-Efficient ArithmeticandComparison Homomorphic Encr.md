---
interest: medium
link: https://arxiv.org/abs/2604.19890
next_step: skim
priority: low
slack_ts: '1777087201.323849'
source: cs.CR - Cryptography and Security
status: unread
title: Efficient Arithmetic-and-Comparison Homomorphic Encryption with Space Switching
---
# Efficient Arithmetic-and-Comparison Homomorphic Encryption with Space Switching
> 原文: [https://arxiv.org/abs/2604.19890](https://arxiv.org/abs/2604.19890)

arXiv:2604.19890v1 Announce Type: new
Abstract: Fully homomorphic encryption (FHE) enables computation on encrypted data without decryption, making it central to privacy-preserving applications. However, no existing scheme efficiently supports both arithmetic and comparison operations in a unified framework. Prior approaches such as scheme switching and polynomial approximation face serious limitations: switching incurs prohibitive overhead for large inputs, while approximation methods introduce errors near critical points, restricting use in accuracy-sensitive tasks. We propose space switching method to integrate arithmetic and comparison computation seamlessly within FV-style schemes. Our approach identifies that the two types of operations require different plaintext spaces and introduces two procedures: a reduction step to transition from the number space $\mathbb{Z}\_{p^r}$ to the digit space $\mathbb{Z}\_{p}$, and a modulus-raising step to map results back to $\mathbb{Z}\_{p^r}$. This design enables continuous evaluation of arithmetic and comparison within the same scheme. Experiments show that our method achieves up to $17\times$ faster performance than scheme switching and $15\times$ faster than direct comparison on database workloads, demonstrating its practicality for real-world privacy-preserving computation. Code and artifacts are available at https://github.com/UCF-Lou-Lab-PET/Universal-BGV.
