---
interest: medium
link: https://arxiv.org/abs/2609.19242
next_step: skim
priority: high
slack_ts: '1789791394.538679'
source: cs.LG - Machine Learning
status: unread
title: Block Parallelism For Efficient Distributed Long-Context Diffusion Language
  Model Training
---
# Block Parallelism For Efficient Distributed Long-Context Diffusion Language Model Training
> 原文: [https://arxiv.org/abs/2609.19242](https://arxiv.org/abs/2609.19242)

arXiv:2609.19242v1 Announce Type: new
Abstract: Block diffusion language models (BDLMs) combine autoregressive dependencies across blocks with parallel denoising within blocks, but long-context training is constrained by distributed attention communication and activation memory. Conventional context parallelism (CP) shards the combined clean-plus-corrupted sequence by position, communicating shared clean K/V together with block-specific corrupted K/V and their gradients. We observe that the BDLM objective separates over target blocks. We introduce block parallelism (BP), a new distributed parallelism dimension that assigns each corrupted-block computation to one rank. To scale BP to long contexts, we introduce context-sharded block parallelism (CSBP), which also shards the shared clean sequence across those ranks. CSBP keeps corrupted K/V and gradients local, avoids replicated clean prefixes, and preserves BDLM training semantics. On 16 H200 GPUs at 256K context, CSBP improves throughput over the best baseline by 1.18-1.45x for supervised fine-tuning and 1.27-1.33x for conversion of autoregressive models to BDLMs, while matching or reducing peak HBM. Full-model speedup reaches 1.61x at 512K. On eight H100 GPUs, CSBP accelerates DFlash2 speculative-decoder training by 2.48x at 512K and 7.59x at 1M. In matched 12-hour DiffusionGemma 26B-A4B SFT runs, CSBP achieves higher pass rates at every trained checkpoint on SWE-bench Verified and Terminal-Bench Lite. Code: https://github.com/ScalingIntelligence/Turbo-dLLM
