---
interest: medium
link: https://arxiv.org/abs/2605.21498
next_step: skim
priority: low
slack_ts: '1779683949.593719'
source: cs.CR - Cryptography and Security
status: unread
title: 'Chain Reactions: How Nonce Collisions in ECDSA Compromise Polygon MEV Searchers'
---
# Chain Reactions: How Nonce Collisions in ECDSA Compromise Polygon MEV Searchers
> 原文: [https://arxiv.org/abs/2605.21498](https://arxiv.org/abs/2605.21498)

arXiv:2605.21498v1 Announce Type: new
Abstract: ECDSA signatures form the bedrock of blockchain transaction authentication, yet their security critically depends on proper nonce generation. We uncover a critical vulnerability in the Polygon MEV ecosystem: systematic nonce reuse that enables complete private key recovery. Analyzing on-chain data reveals that searchers, driven by the need for sub-second response times in sealed-bid auctions, employ predictable nonce patterns. These patterns create linear relationships between signatures, allowing passive attackers to recover private keys using elementary algebra. We provide a compact linear-system formulation for such attacks, including the dangerous case of cross-wallet nonce collisions, and present concrete evidence of exploitable patterns on Polygon. Our findings demonstrate how protocol-induced latency pressures can lead to catastrophic cryptographic failures in production blockchain systems, where a single implementation error compromises multiple accounts simultaneously.
