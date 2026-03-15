---
interest: medium
link: https://arxiv.org/abs/2603.11056
next_step: skim
priority: low
slack_ts: '1773544831.395969'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'GeNeX: Genetic Network eXperts framework for addressing Validation Overfitting'
---
# GeNeX: Genetic Network eXperts framework for addressing Validation Overfitting
> 原文: [https://arxiv.org/abs/2603.11056](https://arxiv.org/abs/2603.11056)

arXiv:2603.11056v1 Announce Type: new
Abstract: Excessive reliance on validation performance during model selection can lead to validation overfitting (VO), where models appear effective during development but fail at test time. This issue is further amplified in low-data regimes and under distribution shifts, where validation signals become unreliable. Although ensemble learning is widely used to improve robustness and generalization, most ensemble construction pipelines depend heavily on validation scores, leaving them vulnerable to VO and limiting their reliability in real-world deployment scenarios. To address this, we propose GeNeX (Genetic Network eXperts), a framework that mitigates validation overfitting at both model generation and ensemble construction stages. In the generation phase, GeNeX employs a dual-path strategy: gradient-based training is coupled with genetic model evolution. Offspring networks are created via crossover of trained parents, promoting structural diversity and weight-level regeneration without relying on validation feedback. This results in a candidate pool of robust, non-overfitted models. During ensemble construction, the candidate networks are clustered by prediction behavior to identify complementary model spaces. Within each cluster, multiple diverse experts are selected using criteria such as robustness and representativeness, and fused at the weight level to form compact prototype networks. The final ensemble aggregates these prototypes, with predictions optimized via Sequential Quadratic Programming for output-level synergy. To rigorously evaluate VO resilience, we introduce a VO-aware evaluation protocol that simulates realistic deployment scenarios by enforcing distributional divergence between training and test subsets.
