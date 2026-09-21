---
title: "TPM-Attest: Hardware-Rooted Integrity Attestation as a Kernel-Level Anti-Cheat Alternative for Linux"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.20909
priority: low
status: unread
interest: medium
next_step: skim
---
# TPM-Attest: Hardware-Rooted Integrity Attestation as a Kernel-Level Anti-Cheat Alternative for Linux
> 原文: [https://arxiv.org/abs/2609.20909](https://arxiv.org/abs/2609.20909)

arXiv:2609.20909v1 Announce Type: new
Abstract: Multiplayer PC gaming on Linux faces a structural problem: the anti-cheat systems that publishers require operate as proprietary Ring 0 kernel modules that are architecturally incompatible with Linux's security model, GPL licensing, and stable ABI guarantees. We argue the right response is not to port these invasive modules to Linux, but to replace them entirely. This paper presents TPM-Attest, a hardware-rooted remote attestation framework that uses the Trusted Platform Module (TPM) 2.0 and the Linux Integrity Measurement Architecture (IMA) to prove, cryptographically, that a client booted cleanly and ran only authorised software -- without any kernel driver, without proprietary code, and without scanning player memory. The system intercepts Epic Online Services (EOS) SDK calls via a userspace LD\_PRELOAD hook, gates session access on a live TPM quote bound to a server-issued nonce, and constructs an index-prefixed Merkle tree over the IMA log that is immune to duplicate-leaf collision attacks. Across 500 constructed tamper sessions we achieve a 100% detection rate; incremental leaf caching reduces repeat-attestation latency to under 3 seconds on real TPM 2.0 hardware. A controlled red-team evaluation against a live demo game confirms all four file-backed attack vectors are blocked while precisely characterising the two confirmed bypass conditions. The full implementation is released as open-source software.
