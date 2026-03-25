---
interest: medium
link: https://arxiv.org/abs/2603.19340
next_step: skim
priority: low
slack_ts: '1774407047.614089'
source: cs.CR - Cryptography and Security
status: unread
title: 'Benchmarking Post-Quantum Cryptography on Resource-Constrained IoT Devices:
  ML-KEM and ML-DSA on ARM Cortex-M0+'
---
# Benchmarking Post-Quantum Cryptography on Resource-Constrained IoT Devices: ML-KEM and ML-DSA on ARM Cortex-M0+
> 原文: [https://arxiv.org/abs/2603.19340](https://arxiv.org/abs/2603.19340)

arXiv:2603.19340v1 Announce Type: new
Abstract: The migration to post-quantum cryptography is urgent for Internet of Things devices with 10-20 year lifespans, yet no systematic benchmarks exist for the finalised NIST standards on the most constrained 32-bit processor class. This paper presents the first isolated algorithm-level benchmarks of ML-KEM (FIPS 203) and ML-DSA (FIPS 204) on ARM Cortex-M0+, measured on the RP2040 (Raspberry Pi Pico) at 133 MHz with 264 KB SRAM. Using PQClean reference C implementations, we measure all three security levels of ML-KEM (512/768/1024) and ML-DSA (44/65/87) across key generation, encapsulation/signing, and decapsulation/verification. ML-KEM-512 completes a full key exchange in 36.3 ms consuming 2.87 mJ--17x faster and 94% less energy than ECDH P-256 on the same hardware. ML-DSA signing exhibits high latency variance due to rejection sampling (coefficient of variation 61-71%, 99th-percentile up to 1,115 ms for ML-DSA-87). The M0+ incurs only a 1.8-1.9x slowdown relative to published Cortex-M4 results, despite lacking 64-bit multiply, DSP, and SIMD instructions. All code, data, and scripts are released as an open-source benchmark suite for reproducibility.
