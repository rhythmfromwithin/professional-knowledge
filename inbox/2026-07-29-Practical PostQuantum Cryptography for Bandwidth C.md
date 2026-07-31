---
interest: medium
link: https://arxiv.org/abs/2607.23007
next_step: skim
priority: low
slack_ts: '1785468996.397769'
source: cs.CR - Cryptography and Security
status: unread
title: Practical Post-Quantum Cryptography for Bandwidth Constrained or Non-Terrestrial
  Networks, and Power Constrained Devices
---
# Practical Post-Quantum Cryptography for Bandwidth Constrained or Non-Terrestrial Networks, and Power Constrained Devices
> 原文: [https://arxiv.org/abs/2607.23007](https://arxiv.org/abs/2607.23007)

arXiv:2607.23007v1 Announce Type: new
Abstract: Post-quantum (PQ) cryptographic algorithms, particularly for authentication, are more complex than classical algorithms and require larger certificates, signatures, and keys. Establishing a PQ-secure network connection increases bandwidth, memory, computation time, and energy consumption. These costs are especially severe in Non-Terrestrial Networks (NTNs), where long propagation delays, intermittent connectivity, constrained link budgets, satellite handovers, limited terminal resources, and bandwidth-constrained satellite-to-ground links amplify the overhead of certificate-based PQ authentication. Consequently, applications such as key rotation and key management may be unable to achieve acceptable handshake reliability or support NIST PQ Security Categories above Category 1. Similar limitations affect low-power IoT devices and bandwidth- or energy-constrained terrestrial networks, where PQ authentication may restrict devices to Category 1 security or prevent ambient-powered endpoints from supporting PQ authentication altogether.
This paper investigates an alternative cryptographic framework that replaces PQ digital certificates with shared secret keys (SSKs). The framework leverages shared-secret ecosystems that do not rely on asymmetric key distribution, such as 5G/6G, and combines a Key Distribution Center (KDC) (e.g., Kerberos) with a preshared-key PQ handshake (e.g., DTLS-PSK) and ephemeral PQ key establishment (e.g., ML-KEM). Compared with certificate-based PQ authentication (e.g., ML-DSA), the proposed approach reduces handshake bandwidth, endpoint RAM, computation time, and energy use while preserving PQ-secure AEAD, including forward secrecy and replay resistance. Applications include NTN-based key rotation and management, uncrewed aerial vehicle (UAV) command-and-control systems, embedded medical sensors, and supply-chain monitoring and asset-tracking platforms.
