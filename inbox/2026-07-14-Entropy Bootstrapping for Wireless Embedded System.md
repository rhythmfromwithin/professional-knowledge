---
interest: medium
link: https://arxiv.org/abs/2607.08865
next_step: skim
priority: low
slack_ts: '1784085262.413569'
source: cs.CR - Cryptography and Security
status: unread
title: Entropy Bootstrapping for Wireless Embedded Systems
---
# Entropy Bootstrapping for Wireless Embedded Systems
> 原文: [https://arxiv.org/abs/2607.08865](https://arxiv.org/abs/2607.08865)

arXiv:2607.08865v1 Announce Type: new
Abstract: Weak randomness has broken deployed cryptography through implementation bugs, boot entropy scarcity, and backdoored generators. Inexpensive wireless sensors concentrate the risk because many boot or operate in highly deterministic conditions while relying on basic, rudimentary, or opaque RNGs. On ESP32-class boards, RF-disabled wireless device RNG register (WDEV) output is pseudorandom by specification yet passes the same statistical screens as RF-active states, showing that output tests cannot replace source-state admission. We propose a defense-in-depth boot path for ESP32-class IoT nodes that combines SRAM startup material, radio burst extraction, and asymmetric entropy capsules under explicit source-state admission. In radio burst extraction, a trusted node in the local IoT network, such as a gateway or dedicated entropy node, sends a public packet burst to open a measurement window. The client samples its own WDEV output and packet timing during that window, then credits only the local response. Capsules cover the cold-start case with a pre-provisioned asymmetric key pair. The trusted node encrypts fresh seed material to the client's public key and signs the capsule; the client verifies, decapsulates, and hashes before it has local entropy. We benchmark the ESP32 RNG under several radio operating modes, the fixed-burst extraction window, the deterministic capsule client path, and SRAM startup reads. Together, these measurements support an admission policy in which each root is credited only when its required source state and protocol checks hold.
