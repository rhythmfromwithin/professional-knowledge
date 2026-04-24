---
interest: medium
link: https://arxiv.org/abs/2604.19767
next_step: skim
priority: high
slack_ts: '1777001714.376569'
source: cs.LG - Machine Learning
status: unread
title: 'Accelerating PayPal''s Commerce Agent with Speculative Decoding: An Empirical
  Study on EAGLE3 with Fine-Tuned Nemotron Models'
---
# Accelerating PayPal's Commerce Agent with Speculative Decoding: An Empirical Study on EAGLE3 with Fine-Tuned Nemotron Models
> 原文: [https://arxiv.org/abs/2604.19767](https://arxiv.org/abs/2604.19767)

arXiv:2604.19767v1 Announce Type: new
Abstract: We evaluate speculative decoding with EAGLE3 as an inference-time optimization for PayPal's Commerce Agent, powered by a fine-tuned llama3.1-nemotron-nano-8B-v1 model. Building on prior work (NEMO-4-PAYPAL) that reduced latency and cost through domain-specific fine-tuning, we benchmark EAGLE3 via vLLM against NVIDIA NIM on identical 2xH100 hardware across 40 configurations spanning speculative token counts (gamma=3, gamma=5), concurrency levels (1-32), and sampling temperatures (0, 0.5). Key findings: (1) gamma=3 achieves 22-49% throughput improvement and 18-33% latency reduction at zero additional hardware cost; (2) acceptance rates remain stable at approximately 35.5% for gamma=3 across all conditions; (3) gamma=5 yields diminishing returns (approximately 25% acceptance rate); (4) LLM-as-Judge evaluation confirms fully preserved output quality; and (5) speculative decoding on a single H100 matches or exceeds NIM on two H100s, enabling 50% GPU cost reduction.
