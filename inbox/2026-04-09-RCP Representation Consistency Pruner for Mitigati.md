---
interest: medium
link: https://arxiv.org/abs/2604.04972
next_step: skim
priority: medium
slack_ts: '1775791741.980649'
source: cs.CV - Computer Vision
status: unread
title: 'RCP: Representation Consistency Pruner for Mitigating Distribution Shift in
  Large Vision-Language Models'
---
# RCP: Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models
> 原文: [https://arxiv.org/abs/2604.04972](https://arxiv.org/abs/2604.04972)

arXiv:2604.04972v1 Announce Type: new
Abstract: Large Vision-Language Models (LVLMs) suffer from prohibitive inference costs due to the massive number of visual tokens processed by the language decoder. Existing pruning methods often lead to significant performance degradation because the irreversible removal of visual tokens causes a distribution shift in the hidden states that deviates from the pre-trained full-token regime. To address this, we propose Representation Consistency Pruner, which we refer to as RCP, as a novel framework that integrates cumulative visual token pruning with a delayed repair mechanism. Specifically, we introduce a cross-attention pruner that leverages the intrinsic attention of the LLM as a baseline to predict cumulative masks, ensuring consistent and monotonic token reduction across layers. To compensate for the resulting information loss, we design a delayed repair adapter denoted as DRA, which caches the essence of pruned tokens and applies FiLM-based modulation specifically to the answer generation tokens. We employ a repair loss to match the first and second-order statistics of the pruned representations with a full-token teacher. RCP is highly efficient because it trains only lightweight plug-in modules while allowing for physical token discarding at inference. Extensive experiments on LVLM benchmarks demonstrate that RCP removes up to 88.9\% of visual tokens and reduces FLOPs by up to 85.7\% with only a marginal average accuracy drop, and outperforms prior methods that avoid fine-tuning the original model on several widely used benchmarks.
