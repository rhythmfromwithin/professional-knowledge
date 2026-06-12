---
interest: medium
link: https://arxiv.org/abs/2606.12498
next_step: skim
priority: low
slack_ts: '1781239682.470439'
source: cs.CR - Cryptography and Security
status: unread
title: 'From Parameters to Feature Space: Task Arithmetic for Backdoor Mitigation
  in Model Merging'
---
# From Parameters to Feature Space: Task Arithmetic for Backdoor Mitigation in Model Merging
> 原文: [https://arxiv.org/abs/2606.12498](https://arxiv.org/abs/2606.12498)

arXiv:2606.12498v1 Announce Type: new
Abstract: Model merging (MM) has gained significant attention as a cost-effective approach to integrate multiple task-specific models into a unified model. However, recent work reveals that MM is highly susceptible to backdoor attacks. Existing defenses based on task arithmetic often fail to eliminate backdoors without substantially degrading clean-task performance, owing to their reliance on direct parameter-space editing. To address this gap, we propose Linear Feature Path Minimization (LFPM), a backdoor mitigation framework for model merging, which introduces an anti-backdoor task vector into the backdoored merged model. Unlike prior approaches, LFPM formulates the backdoor robustness of the merged model from a unified feature-space perspective under the Cross-Task Linearity (CTL) framework, which leverages the approximate linearity of features across tasks. This perspective guides the optimization of the anti-backdoor task to suppress backdoors while preserving clean-task performance. Furthermore, we introduce an effective optimization mechanism based on gradient accumulation and loss path-integral, ensuring robust backdoor suppression along the interpolation path. Extensive experiments demonstrate that LFPM consistently exhibits strong robustness against backdoor attacks in both full fine-tuning and Parameter-Efficient Fine-Tuning (PEFT) settings.
