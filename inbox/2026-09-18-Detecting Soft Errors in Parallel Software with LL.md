---
title: "Detecting Soft Errors in Parallel Software with LLM-tuned Instruction Duplication"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.19531
priority: medium
status: unread
interest: medium
next_step: skim
---
# Detecting Soft Errors in Parallel Software with LLM-tuned Instruction Duplication
> 原文: [https://arxiv.org/abs/2609.19531](https://arxiv.org/abs/2609.19531)

arXiv:2609.19531v1 Announce Type: new
Abstract: We propose PaRID (PaRallel Instruction Duplication), a software-directed soft error detection framework that requires only compile-time effort for multithreading parallel programs. PaRID addresses two key challenges: supporting parallel programs with mixed serial and parallel regions and minimizing performance overhead without relying on costly dynamic profiling. It combines parallel-aware code transformation with LLM-tuned performance modeling, guided by eight generalizable findings from an offline characterization study, to enable fast soft error detection in parallel applications. Evaluation on NPB benchmarks shows that PaRID reduces protection overhead from 162.79% to 59.84% on average and achieves up to 5x speedup while maintaining full error detection effectiveness.
