---
title: "Challenges and Design Considerations for Finding CUDA Bugs Through GPU-Native Fuzzing"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.05725
priority: low
status: unread
interest: medium
next_step: skim
---
# Challenges and Design Considerations for Finding CUDA Bugs Through GPU-Native Fuzzing
> 原文: [https://arxiv.org/abs/2603.05725](https://arxiv.org/abs/2603.05725)

arXiv:2603.05725v1 Announce Type: new
Abstract: Modern computing is shifting from homogeneous CPU-centric systems to heterogeneous systems with closely integrated CPUs and GPUs. While the CPU software stack has benefited from decades of memory safety hardening, the GPU software stack remains dangerously immature. This discrepancy presents a critical ethical challenge: the world's most advanced AI and scientific workloads are increasingly deployed on vulnerable hardware components.
In this paper, we study the key challenges of ensuring memory safety on heterogeneous systems. We show that, while the number of exploitable bugs in heterogeneous systems rises every year, current mitigation methods often rely on unfaithful translations, i.e., converting GPU programs to run on CPUs for testing, which fails to capture the architectural differences between CPUs and GPUs. We argue that the faithfulness of the program behavior is at the core of secure and reliable heterogeneous systems design. To ensure faithfulness, we discuss several design considerations of a GPU-native fuzzing pipeline for CUDA programs.
