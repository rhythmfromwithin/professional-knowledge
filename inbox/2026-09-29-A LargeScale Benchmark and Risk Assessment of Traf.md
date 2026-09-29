---
title: "A Large-Scale Benchmark and Risk Assessment of Traffic Analysis Attacks on Cloud LLM Services"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.31877
priority: low
status: unread
interest: medium
next_step: skim
---
# A Large-Scale Benchmark and Risk Assessment of Traffic Analysis Attacks on Cloud LLM Services
> 原文: [https://arxiv.org/abs/2609.31877](https://arxiv.org/abs/2609.31877)

arXiv:2609.31877v1 Announce Type: new
Abstract: Cloud-based Large language model (LLM) services create a network-level traffic side channel that can expose model, prompt, and task behavior despite encryption. From packet sizes, directions, timing, and burst structure alone, a passive local observer can infer the serving model, the user's prompt category, and the task executed by a collaborative multi-agent system. Yet current evidence is fragmented across separate datasets and settings, limiting reproducibility and comparison. We present, to our knowledge, the first unified measurement study and public benchmark of encrypted LLM traffic across both user--LLM and multi-agent executions. The large-scale benchmark contains 60,000 user--LLM interactions across 10 models and 6 prompt categories, plus 2,838 multi-agent executions covering 10 task categories and two coordination topologies. Using only encrypted packet metadata, we assess the risk of traffic analysis attack by characterizing traffic signatures, identifying the features most associated with leakage, and testing robustness under prompt reformulation, decoding-temperature changes, larger candidate model sets, and partial traffic observation. Model fingerprinting achieves 97.7\% balanced accuracy, prompt-category fingerprinting reaches 76.7\% mean accuracy, and multi-agent task fingerprinting achieves up to 90.7\% accuracy. Prompt reformulation weakens but does not remove model-specific leakage, and task fingerprints remain detectable even from a single agent's traffic.
