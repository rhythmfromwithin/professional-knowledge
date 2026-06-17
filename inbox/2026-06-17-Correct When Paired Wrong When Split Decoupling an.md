---
interest: medium
link: https://arxiv.org/abs/2606.17057
next_step: skim
priority: high
slack_ts: '1781672188.622649'
source: cs.LG - Machine Learning
status: unread
title: 'Correct When Paired, Wrong When Split: Decoupling and Editing Modality-Specific
  Neurons in MLLMs'
---
# Correct When Paired, Wrong When Split: Decoupling and Editing Modality-Specific Neurons in MLLMs
> 原文: [https://arxiv.org/abs/2606.17057](https://arxiv.org/abs/2606.17057)

arXiv:2606.17057v1 Announce Type: new
Abstract: Although Knowledge Editing provides an efficient mechanism for updating the knowledge of Multimodal Large Language Models (MLLMs), we find that current paradigms still suffer from an important yet remain underexplored issue : editing decoupling failure, where entity-related knowledge can be updated when the model is triggered by multimodal inputs (text--image query pairs), however, it often reverts to outdated pre-edit facts when the paired inputs are split into unimodal ones. Our in-depth empirical analysis reveals that the entity knowledge in MLLMs is not stored as a unified representation, but is instead distributed across disentangled modality-specific pathways. As a result, updates biased toward multimodal queries fail to propagate effectively to unimodal circuits. To bridge this gap, we propose DECODE, which explicitly disentangles and localizes modality-specific neuron groups for targeted knowledge. Extensive experiments demonstrate that DECODE consistently achieves effective knowledge updates under different modality triggers, thereby mitigating editing decoupling failures.
