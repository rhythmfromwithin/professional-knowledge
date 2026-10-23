---
title: "When EVM Defaults Break: Three SDK Patterns for UTXO-Family Wallets"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.30183
priority: low
status: unread
interest: medium
next_step: skim
---
# When EVM Defaults Break: Three SDK Patterns for UTXO-Family Wallets
> 原文: [https://arxiv.org/abs/2610.30183](https://arxiv.org/abs/2610.30183)

arXiv:2610.30183v1 Announce Type: new
Abstract: Mainstream Web3 SDKs (e.g., ethers.js, viem) bundle three coupled assumptions: an account-based ledger, a single secp256k1 signer, and input-selection-free transaction construction. These assumptions fail once a chain adopts an extended-UTXO model (here, the Cell model on Nervos CKB), and once the wallet population spans heterogeneous cryptographic primitives (secp256k1, WebAuthn, Schnorr). Using CKBers' Codebase (CCC), a TypeScript SDK, this retrospective case study extracts three recurring patterns from release history and exported APIs: a Transaction Composer that makes capacity-aware input completion and fee estimation declarative, a Unified Signer Abstraction that normalizes signing across heterogeneous wallets behind one interface, and a Connector UI component that ships per-wallet onboarding as a drop-in. The contribution is the articulation of these patterns as transferable design lessons for SDKs targeting UTXO-family ledgers and heterogeneous wallet populations.
