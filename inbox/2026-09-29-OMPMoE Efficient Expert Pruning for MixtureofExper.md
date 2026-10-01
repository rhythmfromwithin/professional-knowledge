---
interest: medium
link: https://arxiv.org/abs/2609.31631
next_step: skim
priority: high
slack_ts: '1790832416.927829'
source: cs.LG - Machine Learning
status: unread
title: 'OMP-MoE: Efficient Expert Pruning for Mixture-of-Experts LLMs via Orthogonal
  Matching Pursuit'
---
# OMP-MoE: Efficient Expert Pruning for Mixture-of-Experts LLMs via Orthogonal Matching Pursuit
> 原文: [https://arxiv.org/abs/2609.31631](https://arxiv.org/abs/2609.31631)

arXiv:2609.31631v1 Announce Type: new
Abstract: Mixture-of-Experts (MoE) models enable efficient scaling of large language models but face critical deployment challenges due to massive memory requirements. Existing pruning methods either incur prohibitive search costs or neglect the dynamic interdependencies between experts. To address these challenges, we present OMP-MoE, a novel training-free compression framework for reducing expert redundancy in MoE-based LLMs. Based on observations of expert contribution patterns, we reformulate the pruning problem as a sparse signal reconstruction task solved through Orthogonal Matching Pursuit. Specifically, our method first treats individual expert contributions as dictionary atoms and selects experts that greedily minimize reconstruction error with linear computational complexity. Then, we optimize cross-layer expert allocation through a water-filling strategy that accounts for both reconstruction quality and routing stability. Finally, we introduce OMP-MoE{\dag}, an adaptive inference mechanism that dynamically adjusts expert activation based on energy prediction. Comprehensive experiments on Qwen, DeepSeek-V2, GPT-OSS, and Mixtral MoE demonstrate consistent improvements over existing methods at 25-50% pruning ratios. For Qwen3-30B-A3B at 50% compression, we retain 93.3% of original performance, achieving 33$\times$ faster search and 1.55$\times$ inference speedup. Codes will be available after acceptance.
