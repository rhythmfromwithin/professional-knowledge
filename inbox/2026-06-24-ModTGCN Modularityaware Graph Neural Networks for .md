---
interest: medium
link: https://arxiv.org/abs/2606.23694
next_step: skim
priority: high
slack_ts: '1782274338.405699'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'ModTGCN: Modularity-aware Graph Neural Networks for Text Classification'
---
# ModTGCN: Modularity-aware Graph Neural Networks for Text Classification
> 原文: [https://arxiv.org/abs/2606.23694](https://arxiv.org/abs/2606.23694)

arXiv:2606.23694v1 Announce Type: new
Abstract: Graph-based text classification models typically rely on local neighborhood aggregation and overlook global community structure, despite semantic document graphs exhibiting strong class-consistent clustering. Ignoring this can blur class boundaries and lead to over-smoothing. We propose ModTGCN, a modularity-aware graph neural network for text classification that jointly optimizes cross-entropy and a modularity-based auxiliary objective to promote class-coherent document communities while preserving discriminative representations. The modularity term is computed on a document-document similarity graph derived from transformer embeddings (pretrained or fine-tuned). To improve scalability, we decouple the original heterogeneous TextGCN graph into separate document-word and word-word components, achieving 2x-10x faster training. We further study graph construction strategies, label-aware edge reweighting, and supervision choices for modularity optimization. Experiments on five benchmarks show consistent gains, with larger improvements on complex, low homophily datasets such as Ohsumed and 20NG.
