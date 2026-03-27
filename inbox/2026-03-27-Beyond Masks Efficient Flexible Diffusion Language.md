---
interest: medium
link: https://arxiv.org/abs/2603.23507
next_step: skim
priority: high
slack_ts: '1774581568.816959'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Beyond Masks: Efficient, Flexible Diffusion Language Models via Deletion-Insertion
  Processes'
---
# Beyond Masks: Efficient, Flexible Diffusion Language Models via Deletion-Insertion Processes
> 原文: [https://arxiv.org/abs/2603.23507](https://arxiv.org/abs/2603.23507)

arXiv:2603.23507v1 Announce Type: new
Abstract: While Masked Diffusion Language Models (MDLMs) relying on token masking and unmasking have shown promise in language modeling, their computational efficiency and generation flexibility remain constrained by the masking paradigm. In this paper, we propose Deletion-Insertion Diffusion language models (DID) that rigorously formulate token deletion and insertion as discrete diffusion processes, replacing the masking and unmasking processes in current MDLMs. DID improves training and inference efficiency by eliminating two major sources of computational overhead in MDLMs: the computations on non-informative 1) tokens inherent to the paradigm, and 2) tokens introduced in variable-length settings. Furthermore, DID offers greater flexibility by: 1) natively supporting variable-length sequences without requiring fixed-length padding, and 2) an intrinsic self-correction mechanism during generation due to insertion that dynamically adjusts token positions. To train DID, we design a score-based approach that assigns scores to token insertion operations and derive appropriate training objectives. The objectives involve subsequence counting problems, which we efficiently solve via a parallelized dynamic programming algorithm. Our experiments across fixed and variable-length settings demonstrate the advantage of DID over baselines of MDLMs and existing insertion-based LMs, in terms of modeling performance, sampling quality, and training/inference speed, without any hyperparameter tuning.
