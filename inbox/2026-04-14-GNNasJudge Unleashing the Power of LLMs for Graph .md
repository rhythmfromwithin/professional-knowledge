---
interest: medium
link: https://arxiv.org/abs/2604.08553
next_step: skim
priority: high
slack_ts: '1776137321.829699'
source: cs.LG - Machine Learning
status: unread
title: 'GNN-as-Judge: Unleashing the Power of LLMs for Graph Learning with GNN Feedback'
---
# GNN-as-Judge: Unleashing the Power of LLMs for Graph Learning with GNN Feedback
> 原文: [https://arxiv.org/abs/2604.08553](https://arxiv.org/abs/2604.08553)

arXiv:2604.08553v1 Announce Type: new
Abstract: Large Language Models (LLMs) have shown strong performance on text-attributed graphs (TAGs) due to their superior semantic understanding ability on textual node features. However, their effectiveness as predictors in the low-resource setting, where labeled nodes are severely limited and scarce, remains constrained since fine-tuning LLMs usually requires sufficient labeled data, especially when the TAG shows complex structural patterns. In essence, this paper targets two key challenges: (i) the difficulty of generating and selecting reliable pseudo labels on TAGs for LLMs, and (ii) the need to mitigate potential label noise when fine-tuning LLMs with pseudo labels. To counter the challenges, we propose a new framework, GNN-as-Judge, which can unleash the power of LLMs for few-shot semi-supervised learning on TAGs by incorporating the structural inductive bias of Graph Neural Networks (GNNs). Specifically, GNN-as-Judge introduces a collaborative pseudo-labeling strategy that first identifies the most influenced unlabeled nodes from labeled nodes, then exploits both the agreement and disagreement patterns between LLMs and GNNs to generate reliable labels. Furthermore, we develop a weakly-supervised LLM fine-tuning algorithm that can distill the knowledge from informative pseudo labels while mitigating the potential label noise. Experiments on multiple TAG datasets demonstrate that GNN-as-Judge significantly outperforms existing methods, particularly in low-resource regimes where labeled data are scarce.
