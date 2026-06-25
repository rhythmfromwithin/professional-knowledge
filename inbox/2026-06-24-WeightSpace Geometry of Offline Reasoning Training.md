---
interest: medium
link: https://arxiv.org/abs/2606.23740
next_step: skim
priority: high
slack_ts: '1782360752.889949'
source: cs.LG - Machine Learning
status: unread
title: Weight-Space Geometry of Offline Reasoning Training
---
# Weight-Space Geometry of Offline Reasoning Training
> 原文: [https://arxiv.org/abs/2606.23740](https://arxiv.org/abs/2606.23740)

arXiv:2606.23740v1 Announce Type: new
Abstract: Offline reinforcement-learning losses (RFT, RIFT, DFT, Offline GRPO, DPO) are widely used to distill reasoning from large teachers into smaller students, and are typically compared on downstream accuracy alone. We ask whether they are mechanistically distinct or converge to a similar weight update. Training six methods (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) on identical math rollouts from a single base model (Qwen3-4B) with attention-only LoRA, we analyze the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. We observe: (i) SFT, RFT, and RIFT have nearly colinear weight deltas (cosine >= 0.97, top-1 principal angle ~7 deg median over 144 modules) and comparable GSM8K accuracy (87-88%, n=1319; pairwise McNemar p >= 0.15); (ii) DFT diverges further in direction than any reward-weighted method despite using the same data; (iii) Offline GRPO adds a substantial component orthogonal to the SFT direction (~67% globally, up to ~86% in late layers) while staying in the SFT loss basin; (iv) DPO sits in a near-orthogonal subspace, shows a mode-connectivity barrier, and collapses late-layer CKA to ~0.46. DPO also reaches the highest accuracy in our protocol on both GSM8K (93.5%, McNemar p < 10^-9 vs. each other method) and AIME26 (30.0% vs. 3.3-10.0%); its training uses a 10x smaller learning rate than the others (the standard convention), so the update-norm and accuracy gaps reflect loss-function and optimizer choices jointly, and a learning-rate-matched DPO comparison is left for future work.
