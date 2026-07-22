---
interest: medium
link: https://arxiv.org/abs/2607.16383
next_step: skim
priority: low
slack_ts: '1784690758.876279'
source: cs.CR - Cryptography and Security
status: unread
title: 'Identity-Bound Academic Credentials on Blockchain: On-Chain Issuer Accreditation
  with ERC-3643 and OnchainID'
---
# Identity-Bound Academic Credentials on Blockchain: On-Chain Issuer Accreditation with ERC-3643 and OnchainID
> 原文: [https://arxiv.org/abs/2607.16383](https://arxiv.org/abs/2607.16383)

arXiv:2607.16383v1 Announce Type: new
Abstract: Verifying academic credentials remains difficult: records are held by individual institutions in proprietary systems, verification is slow and manual, and counterfeit qualifications are widespread. Blockchain-based registries have been proposed as a remedy, but existing systems tend to anchor certificate hashes without binding them to a verifiable identity, without an explicit mechanism to accredit issuing institutions, and without support for correcting or revoking credentials once issued. This paper investigates whether an infrastructure designed for regulated financial instruments can be repurposed to close these gaps. We present the design of a registry for identity-bound academic credentials that composes OnchainID self-sovereign identities (ERC-734/ERC-735) with the T-REX suite (ERC-3643): its trusted-issuer registry becomes an on-chain issuer-accreditation whitelist, and each certificate is represented as a signed, updatable claim bound to a student's identity and verifiable by any third party without a wallet, while sensitive fields are kept off-chain. We make explicit the tension between a transferable-security-token standard and non-transferable credentials, clarifying which of its guarantees carry over. We validate the design with a reference implementation covering the full certificate life cycle and evaluate it in terms of gas cost, scalability, latency, and security, quantifying the overhead relative to a hash-anchoring baseline.
