---
interest: medium
link: https://arxiv.org/abs/2610.31814
next_step: skim
priority: low
slack_ts: '1792988502.953529'
source: cs.CR - Cryptography and Security
status: unread
title: 'SILMARILS-MV: Information-Theoretically Secure Multi-Verifier Signatures with
  Dealer-Free Key Issuance and Linear Aggregation for Permissioned Blockchains'
---
# SILMARILS-MV: Information-Theoretically Secure Multi-Verifier Signatures with Dealer-Free Key Issuance and Linear Aggregation for Permissioned Blockchains
> 原文: [https://arxiv.org/abs/2610.31814](https://arxiv.org/abs/2610.31814)

arXiv:2610.31814v1 Announce Type: new
Abstract: Permissioned blockchains authenticate transactions, votes and quorum certificates with computationally secure signatures, and post-quantum replacements inflate consensus traffic by orders of magnitude. Information-theoretic alternatives have required a trusted authority, quantum channels, per-signature interaction, or single-use keys with bounded transfer. We present SILMARILS-MV, a multi-verifier unconditionally secure signature in which a signature is the vector $\alpha = A\,e(m)$ and each verifier holds a secret functional $c\_i = \Gamma^T \lambda(x\_i)$ derived from virtual anchors $\Gamma$ that nobody learns. Against unbounded adversaries corrupting up to $\omega$ verifiers and any signers, and observing every decision, an honest verifier accepts a forged or invalid signature with probability at most $Q/q + 1/(q-1)$, a bound that is tight in its leading term. The scheme is strongly unforgeable, non-repudiable, transferable across unboundedly many hops, and linearly aggregatable. Keys are issued by the validators through perfectly secure MPC for $t < n/3$, without broadcast. To scale, we let the committee itself sign: in threshold notarization, finality certificates have constant size $32(\omega+1)$ bytes and per-validator issuance cost no longer depends on $n$. Arbiter-verified keys give clients 32-byte signatures, robust redistribution supports membership changes and share refresh, and verifiers can be enrolled retroactively. A certificate verifies in 2.4 microseconds. In an analytic normal-case model at 1000 validators, threshold notarization needs 71 KiB of authentication traffic per validator per block, 22x less than ML-DSA-44 for admitted verifiers. In a Rust HotStuff prototype with 100 validators, SILMARILS-MV commits 2.8x more transactions per second than ML-DSA-44 with 67x less cryptographic CPU, and Monte-Carlo attacks match the bounds.
