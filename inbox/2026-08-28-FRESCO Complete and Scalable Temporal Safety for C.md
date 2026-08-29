---
interest: medium
link: https://arxiv.org/abs/2608.26353
next_step: skim
priority: low
slack_ts: '1787986068.880929'
source: cs.CR - Cryptography and Security
status: unread
title: 'FRESCO: Complete and Scalable Temporal Safety for CHERI Application Processors'
---
# FRESCO: Complete and Scalable Temporal Safety for CHERI Application Processors
> 原文: [https://arxiv.org/abs/2608.26353](https://arxiv.org/abs/2608.26353)

arXiv:2608.26353v1 Announce Type: new
Abstract: CHERI provides hardware-enforced spatial memory safety. While prior work extends it with heap temporal safety, stack use-after-return remains unaddressed. Existing defenses fall short: compiler analysis reliably catches only references that escape as function return values, while dynamic sanitizers impose overheads that preclude production deployment.
We present FRESCO, built on the principle that a stack capability must not outlive the frame that created it. FRESCO "colors" the stack pointer with per-invocation provenance identifiers; every capability derived from it inherits that lifetime and is hardware-invalidated the moment the function exits, regardless of how or where it escaped.
Because stack frames retire orders of magnitude more frequently than heap allocations, FRESCO manages the resulting color pressure through: 1) Color Saver, a static capability-aware escape analysis that confines coloring to functions needing it, and whose core algorithm we mechanically verify in Rocq, and 2) capability-color segmentation, which partitions memory into disjoint segments, each with an independent color namespace. Color segmentation lets stack and heap temporal safety coexist on one system, making FRESCO the first hardware/software co-design to provide complete and scalable temporal safety for CHERI application processors.
We realize FRESCO on the CHERI-RISC-V QEMU full-system emulator and the out-of-order CHERI-Toooba FPGA softcore, with software support in the CHERI-enabled Clang/LLVM compiler and CheriBSD OS. FRESCO systematically prevents use-after-return, use-after-free, and double-free across the NIST Juliet Test Suite and CVEs, with only a small run-time overhead in SPEC CPU (4% g.m.), SQLite, and PostgreSQL (10-14%).
