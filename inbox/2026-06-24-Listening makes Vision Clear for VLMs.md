---
interest: medium
link: https://arxiv.org/abs/2606.23763
next_step: skim
priority: medium
slack_ts: '1782274338.267519'
source: cs.CV - Computer Vision
status: unread
title: Listening makes Vision Clear for VLMs
---
# Listening makes Vision Clear for VLMs
> 原文: [https://arxiv.org/abs/2606.23763](https://arxiv.org/abs/2606.23763)

arXiv:2606.23763v1 Announce Type: new
Abstract: Recent work typically assesses vision--language consistency using attention distributions of answer-side tokens. However, we observe that highest attention regions are not always consistent with the intended semantic token. This probably stems from decoding drift, where language priors from previously generated answer tokens accumulate and mismatch with visual attention. Besides the priors from previous answer tokens, we find that structural tokens, e.g., modality boundary markers, may encompass the entire context and generate high attention to areas unrelated to the target. To avoid these distortions and provide consistency evaluation for large VLMs, we adopt prompt-side semantics and propose Prompt-Vision Token Activation Map (PV-TAM). PV-TAM further incorporates a filter to remove systematic bias induced by modality boundary markers. Unlike traditional methods that evaluate overlap solely through masks while ignoring activation intensity, our metrics leverage the peak distribution of attention to measure the alignment between prompts and visual regions. In experiments, PV-TAM consistently improves both attention-based and IoU-style localization metrics over answer-side baselines on various datasets.
