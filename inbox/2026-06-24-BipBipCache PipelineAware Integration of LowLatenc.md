---
interest: medium
link: https://arxiv.org/abs/2606.23941
next_step: skim
priority: low
slack_ts: '1782274335.252979'
source: cs.CR - Cryptography and Security
status: unread
title: 'BipBipCache: Pipeline-Aware Integration of Low-Latency Tweakable Encryption
  in an Embedded Cache Controller'
---
# BipBipCache: Pipeline-Aware Integration of Low-Latency Tweakable Encryption in an Embedded Cache Controller
> 原文: [https://arxiv.org/abs/2606.23941](https://arxiv.org/abs/2606.23941)

arXiv:2606.23941v1 Announce Type: new
Abstract: Consumer and embedded processors store sensitive data in on-chip SRAM caches that remain readable after power loss or physical probing unless ciphertext is maintained in the memory array itself. This paper presents BipBipCache, a direct-mapped cache controller that integrates the BipBip tweakable block cipher (TBC) to encrypt cache data and tags in real time using a C$^3$-style 24+40 bit decomposition of each 64-bit word. We reconstruct the first pipelined hardware BipBip encryptor from a decryptor-centric specification and coordinate it with a 3-cycle decryptor inside the cache datapath.
Our threat model targets confidentiality of cache-resident contents against cold-boot, bus, and SRAM readout attacks. A key architectural result is that 6-cycle encryption latency does not fully translate into 6-cycle write penalty: the first three encryptor stages overlap with tag decryption and hit detection, leaving an effective 3-cycle write commitment after hit verification. We verify encryptor and decryptor correctness against the official BipBip C++ reference (five vectors each), report FPGA resource utilization on Xilinx Artix-7 (3,356 LUTs, 16.1% of device; crypto logic ~79% of LUTs), and confirm end-to-end operation on hardware.
