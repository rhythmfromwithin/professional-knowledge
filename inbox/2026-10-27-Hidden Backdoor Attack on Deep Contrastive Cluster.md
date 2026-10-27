---
interest: medium
link: https://arxiv.org/abs/2610.33116
next_step: skim
priority: low
slack_ts: '1793076024.656049'
source: cs.CR - Cryptography and Security
status: unread
title: Hidden Backdoor Attack on Deep Contrastive Clustering
---
# Hidden Backdoor Attack on Deep Contrastive Clustering
> 原文: [https://arxiv.org/abs/2610.33116](https://arxiv.org/abs/2610.33116)

arXiv:2610.33116v1 Announce Type: new
Abstract: Deep contrastive clustering has become a representative paradigm for unsupervised image clustering, yet its security under training-time poisoning remains largely unexplored. This paper investigates a hidden backdoor threat against deep contrastive clustering and proposes HBDCC, a Hidden Backdoor attack for Deep Contrastive Clustering. Here, hidden does not indicate that the trigger is visually imperceptible, but rather that the malicious trigger-cluster association remains behaviorally dormant on clean inputs and is activated only when the trigger appears at inference time. HBDCC poisons only a small fraction of unlabeled training samples and exploits an inherent structural weakness of contrastive clustering: augmentation-persistent triggers can be repeatedly aligned across different views at the instance level and further reinforced by cluster-level consistency objectives. As a result, the poisoned model preserves normal clustering behavior on clean data, while producing severely distorted cluster assignments for triggered inputs. We provide a dual-level analysis of the backdoor implantation mechanism and evaluate HBDCC on ImageNet-10, ImageNet-Dogs, and STL-10 with representative contrastive clustering frameworks. Extensive experiments demonstrate that HBDCC can substantially degrade triggered clustering performance in a dataset-dependent manner while maintaining sufficient clean-data utility to evade standard evaluation protocols. We further conduct comprehensive studies on poisoning ratio, attack scope, trigger type, trigger size, and a lightweight knowledge-distillation-based mitigation strategy.
