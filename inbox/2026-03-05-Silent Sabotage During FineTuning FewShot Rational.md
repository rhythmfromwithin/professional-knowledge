---
title: "Silent Sabotage During Fine-Tuning: Few-Shot Rationale Poisoning of Compact Medical LLMs"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.02262
priority: low
status: unread
---
# Silent Sabotage During Fine-Tuning: Few-Shot Rationale Poisoning of Compact Medical LLMs
> 原文: [https://arxiv.org/abs/2603.02262](https://arxiv.org/abs/2603.02262)

arXiv:2603.02262v1 Announce Type: new
Abstract: Supervised fine-tuning (SFT) is essential for the development of medical large language models (LLMs), yet prior poisoning studies have mainly focused on the detectable backdoor attacks. We propose a novel poisoning attack targeting the reasoning process of medical LLMs during SFT. Unlike backdoor attacks, our method injects poisoned rationales into few-shot training data, leading to stealthy degradation of model performance on targeted medical topics. Results showed that knowledge overwriting was ineffective, while rationale poisoning caused significant decline on the accuracy of the target subject, as long as no correct samples of the same subject appear in the dataset. A minimum number and ratio of poisoned samples was needed to carry out an effective and stealthy attack, which was more efficient and accurate than catastrophic forgetting. We demonstrate though this study the risk of SFT-stage poisoning, hoping to spur more studies of defense in the sensitive medical domain.
