---
interest: medium
link: https://arxiv.org/abs/2604.11838
next_step: skim
priority: high
slack_ts: '1776310489.108459'
source: cs.LG - Machine Learning
status: unread
title: A Layer-wise Analysis of Supervised Fine-Tuning
---
# A Layer-wise Analysis of Supervised Fine-Tuning
> 原文: [https://arxiv.org/abs/2604.11838](https://arxiv.org/abs/2604.11838)

arXiv:2604.11838v1 Announce Type: new
Abstract: While critical for alignment, Supervised Fine-Tuning (SFT) incurs the risk of catastrophic forgetting, yet the layer-wise emergence of instruction-following capabilities remains elusive. We investigate this mechanism via a comprehensive analysis utilizing information-theoretic, geometric, and optimization metrics across model scales (1B-32B). Our experiments reveal a distinct depth-dependent pattern: middle layers (20\%-80\%) are stable, whereas final layers exhibit high sensitivity. Leveraging this insight, we propose Mid-Block Efficient Tuning, which selectively updates these critical intermediate layers. Empirically, our method outperforms standard LoRA up to 10.2\% on GSM8K (OLMo2-7B) with reduced parameter overhead, demonstrating that effective alignment is architecturally localized rather than distributed. The code is publicly available at https://anonymous.4open.science/r/base\_sft.
