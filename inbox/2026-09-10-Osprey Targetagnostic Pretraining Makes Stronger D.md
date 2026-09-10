---
interest: medium
link: https://arxiv.org/abs/2609.09338
next_step: skim
priority: high
slack_ts: '1789013740.902709'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Osprey: Target-agnostic Pre-training Makes Stronger Drafters in Speculative
  Decoding'
---
# Osprey: Target-agnostic Pre-training Makes Stronger Drafters in Speculative Decoding
> 原文: [https://arxiv.org/abs/2609.09338](https://arxiv.org/abs/2609.09338)

arXiv:2609.09338v1 Announce Type: new
Abstract: Speculative decoding is critical for accelerating LLM inference. However, the speedup is fragile: drafters are typically trained against a narrow distribution for a single target model, and their acceptance rate collapses under workload shifts. This is a striking inversion of modern LLM development, where target models are valued precisely for the broad generalization they acquire through large-scale pretraining. We argue that the natural remedy, pretraining, has been hard to apply to drafters because existing recipes are target-specific: the drafter consumes the target's hidden states and is distilled on the target's logits, so pretraining must be repeated for each target. We introduce Osprey, which instead bootstraps drafters from off-the-shelf pretrained small language models, treating broad pretraining as a reusable, target-agnostic asset and reducing per-target work to a lightweight adaptation step. Realizing this requires overcoming two challenges: small LMs are far deeper than a latency-bound drafter can afford, and their pretrained computation must remain intact while the drafter learns to ingest target hidden states and emit tokens in the target's vocabulary. Osprey addresses both by pruning to a shallow backbone, restoring its language-modeling capability with target-agnostic next-token pretraining, and adapting it to each target through vocabulary alignment, zero-initialized QKV expansion, and distillation from the target model's output distribution. Empirically, a single pretrained Osprey backbone transfers across targets and improves mean acceptance length by 16.1% for Qwen3-8B, 21.2% for Llama-3.3-70B-Instruct, and 22.7% for the 229B MiniMax-M2.5 (with 17.5% higher tokens per second), with the largest gains on out-of-domain and multilingual data. Our code is available at https://github.com/LeanModels/Osprey.
