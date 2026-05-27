---
title: "Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.26132
priority: high
status: unread
interest: medium
next_step: skim
---
# Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline
> 原文: [https://arxiv.org/abs/2605.26132](https://arxiv.org/abs/2605.26132)

arXiv:2605.26132v1 Announce Type: new
Abstract: Can post-trained large language models (LLMs) further improve themselves using only unlabeled prompts, without external teachers or feedback from tools? We study this setting starting only from unlabeled seed questions with no ground-truth solutions, across three reasoning domains: math, science, and coding. We propose Self-Verified Distillation, a simple post-training refinement algorithm in which the model generates candidate solutions to these seed questions, filters them using prompt-based self-verification, and trains on the resulting self-curated dataset. Inspired by the UQ benchmark's use of multiple validators to screen candidate answers to hard unsolved questions, we adapt this validation-based filtering idea to self-training: the model filters its own generated solutions through a three-stage cascade of cycle-consistency, factuality, and correctness checks, accepting a solution only if it passes all stages with unanimous judge votes. We find that sampling more candidate generations and using a larger verification budget during training data construction produces higher-quality self-curated data and, in turn, better reasoning models. We then train Qwen3 models at multiple scales with Self-Verified Distillation and obtain gains across all three domains. For Qwen3-4B, our method improves aggregate held-out pass@1 by +16.7 points in math (AIME26 and HMMT), +11.1 points in science (GPQA Diamond and HLE), and +8.3 points in coding (LCBv5 and LCBv6), with gains also extending to 0.6B and 8B models. Compared to our test-time-only baseline (UQ-TTC), which improves performance by spending extra compute at inference time, Self-Verified Distillation achieves better performance in most settings while requiring only a single inference call at test time.
