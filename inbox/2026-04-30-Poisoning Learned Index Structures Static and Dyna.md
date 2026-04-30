---
title: "Poisoning Learned Index Structures: Static and Dynamic Adversarial Attacks on ALEX"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.24975
priority: low
status: unread
interest: medium
next_step: skim
---
# Poisoning Learned Index Structures: Static and Dynamic Adversarial Attacks on ALEX
> 原文: [https://arxiv.org/abs/2604.24975](https://arxiv.org/abs/2604.24975)

arXiv:2604.24975v1 Announce Type: cross
Abstract: Learned index structures achieve high performance by modeling the cumulative distribution function (CDF) of keys, but this reliance on data distributions introduces potential vulnerability to adversarial manipulation. Prior work has explored both static data poisoning and dynamic algorithmic complexity attacks (ACA), though evaluations are typically limited in scale or consider only one threat model. We present a systematic study of both attack paradigms on ALEX, a state-of-the-art dynamic learned index, under a unified and reproducible framework.
Our evaluation scales to realistic workloads with up to 200K adversarial inserts and includes multiple SOSD datasets with diverse key distributions, as well as a real-key baseline to isolate adversarial effects. Our results show a clear separation between threat models. Static poisoning has minimal impact on lookup performance in ALEX under bulk-loaded settings, while dynamic ACA induces substantial degradation, with up to 2--2.8x slowdown in lookup throughput. However, attack effectiveness is highly dataset-dependent: dense key distributions limit adversarial leverage due to duplicate-heavy insertions and ALEX's localized structure.
We highlight key evaluation considerations, including the need for control workloads and the mismatch between localized structural damage and global query metrics. These results show that robustness in learned indexes depends critically on the interaction between threat model, data distribution, and evaluation methodology.
