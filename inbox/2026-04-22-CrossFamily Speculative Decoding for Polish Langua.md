---
title: "Cross-Family Speculative Decoding for Polish Language Models on Apple~Silicon: An Empirical Evaluation of Bielik~11B with UAG-Extended MLX-LM"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2604.16368
priority: high
status: unread
interest: medium
next_step: skim
---
# Cross-Family Speculative Decoding for Polish Language Models on Apple~Silicon: An Empirical Evaluation of Bielik~11B with UAG-Extended MLX-LM
> 原文: [https://arxiv.org/abs/2604.16368](https://arxiv.org/abs/2604.16368)

arXiv:2604.16368v2 Announce Type: new
Abstract: Speculative decoding accelerates LLM inference by using a small draft model to propose k candidate tokens for a target model to verify. While effective for same-tokenizer pairs on high-bandwidth GPUs, its applicability to cross-family pairs with mismatched tokenizers and consumer-grade unified memory remains underexplored. We extend the MLX-LM framework with Universal Assisted Generation (UAG) to enable cross-tokenizer speculative decoding on Apple Silicon. We evaluate Bielik 11B-Instruct (Mistral-based) as the target model, paired with three draft models: Bielik 1.5B (Qwen-based with custom tokenizer), Qwen2.5-1.5B, and Llama 3.2-1B. Experiments on three Polish-language datasets (Wikipedia, pl\_alpaca, synthetic) use draft lengths k in {2, 4, 6} to compare naive and context-aware token translation. Results show: (1) context-aware translation consistently improves acceptance rates across all configurations; (2) the Polish-specialized Bielik 1.5B achieves lower acceptance than general-purpose Qwen2.5 and Llama 3.2 drafters; (3) throughput on Apple Silicon is content-dependent, reaching 1.7x speedup for structured text but failing for varied instructions; and (4) verification cost on unified memory does not amortize as theory predicts because both models are memory-bandwidth bound, making sequential drafting expensive relative to batched verification. We propose a hardware-aware speedup formula and characterize conditions for cross-family speculative decoding on Apple Silicon. This is the first systematic evaluation of cross-family speculative decoding for Polish LLMs and the first empirical study of UAG-based decoding on unified memory architectures.
