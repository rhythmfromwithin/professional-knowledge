---
interest: medium
link: https://arxiv.org/abs/2610.26906
next_step: skim
priority: low
slack_ts: '1792642778.374869'
source: cs.CR - Cryptography and Security
status: unread
title: 'InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference'
---
# InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference
> 原文: [https://arxiv.org/abs/2610.26906](https://arxiv.org/abs/2610.26906)

arXiv:2610.26906v1 Announce Type: new
Abstract: Variable type recovery is a critical task in binary reverse engineering, enabling downstream applications such as vulnerability discovery, malware analysis, and security enforcement. While recent Transformer-based models have demonstrated strong performance in type inference by learning instruction-level semantics, they predominantly operate within single-function boundaries (i.e. intra-procedural analysis), ignoring the rich type constraints that propagate across function calls. Empirical studies have shown that nearly 44% of variables in real-world binaries propagate across function boundaries as arguments or return values, representing a significant source of type information that intra-procedural models cannot exploit. In this paper, we propose InterType, a method that embeds inter-procedural analysis into a pre-trained Transformer model for binary type recovery. Our approach builds on CodeArt, a state-of-the-art Transformer model for stripped binary analysis, and extends it by incorporating caller-callee data flow dependencies during fine-tuning. Specifically, we extract data flow dependence for each caller-callee pair from disassembled binaries and construct training instances that provide the model with cross-function context. By exposing the Transformer to inter-procedural variable propagation patterns, our model learns to resolve types that depend on cross-function data flow. We evaluate InterType on the coreutils benchmark compiled with optimization levels O0 through O3. On O1 binaries, InterType improves recall by 2.76 percentage points, from 89.00% for the intra-procedural CodeArt baseline to 91.76%, corresponding to a 25.1% reduction in recall error rate (1 - recall).
