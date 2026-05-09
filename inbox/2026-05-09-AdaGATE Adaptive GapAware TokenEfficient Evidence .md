---
title: "AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.05245
priority: high
status: unread
interest: medium
next_step: skim
---
# AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation
> 原文: [https://arxiv.org/abs/2605.05245](https://arxiv.org/abs/2605.05245)

arXiv:2605.05245v1 Announce Type: new
Abstract: Retrieval-augmented generation (RAG) remains brittle on multi-hop questions in realistic deployment settings, where retrieved evidence may be noisy or redundant and only limited context can be passed to the generator. Existing controllers address parts of this problem, but typically either expand context additively, select from a fixed top-k set, or optimize relevance without explicitly repairing missing bridge facts. We propose AdaGATE, a training-free evidence controller for multi-hop RAG that frames evidence selection as a token-constrained repair problem. AdaGATE combines entity centric gap tracking, targeted micro-query generation, and a utility based selection mechanism that balances gap coverage, corroboration, novelty, redundancy, and direct question relevance. We evaluate AdaGATE on HotpotQA under clean, redundancy, and noise injected retrieval conditions. Across all three settings, AdaGATE achieves the best evidence F1 among the compared controllers, reaching 62.3% on clean data and 71.2% under redundancy injection, while using 2.6x fewer input tokens than Adaptive-k. These results suggest that explicit gap-aware repair, combined with token-efficient evidence selection, improves robustness in multi-hop RAG under imperfect retrieval. Our code and evaluation pipeline are available at https://github.com/eliguo/AdaGATE.
