---
title: "Hardware-Rooted PUF Fingerprinting for Device-Level Traceability in Knowledge Distillation"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.31968
priority: low
status: unread
interest: medium
next_step: skim
---
# Hardware-Rooted PUF Fingerprinting for Device-Level Traceability in Knowledge Distillation
> 原文: [https://arxiv.org/abs/2609.31968](https://arxiv.org/abs/2609.31968)

arXiv:2609.31968v1 Announce Type: new
Abstract: Knowledge distillation (KD) enables model transfer across heterogeneous platforms and deployment environments, yet it exposes proprietary models to distillation-based theft, where an adversary extracts intellectual property (IP) by training a student model on teacher outputs. Current defenses, such as software watermarking or hardware-based access control, either fail to survive the distillation process or lack the granularity to identify the specific device responsible for a leak. Aiming to provide post-theft accountability and traceability, we propose a novel fingerprinting framework that superimposes device-specific Physical Unclonable Function (PUF) signatures onto teacher logits during distillation. By utilizing signatures derived from Ring Oscillator (RO) PUFs measured on a Xilinx Zynq-7020 FPGA, we ensure that any student model trained via KD inherits a unique, hardware-linked identity. Our framework is architecture-agnostic, enabling reliable identity inheritance across heterogeneous structures, including Convolutional Neural Networks, Vision Transformers, and encoders. To ensure robust attribution, we implement a two-stage recovery pipeline consisting of a neural decoder and Hamming-distance refinement, maintaining high detection accuracy even under noisy conditions. Furthermore, we introduce a multi-level logit encoding scheme to support large-scale device deployment. Experimental results demonstrate that the embedded fingerprints are resilient against common post-distillation modifications. These results establish a practical system-level approach for enabling hardware-linked model traceability in distributed AI deployment environments.
