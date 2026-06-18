---
interest: medium
link: https://arxiv.org/abs/2606.18283
next_step: skim
priority: high
slack_ts: '1781759641.909229'
source: cs.LG - Machine Learning
status: unread
title: 'Gaussian Mixture Attention: Linear-Time Sequence Mixing via Probabilistic
  Latent Routing'
---
# Gaussian Mixture Attention: Linear-Time Sequence Mixing via Probabilistic Latent Routing
> 原文: [https://arxiv.org/abs/2606.18283](https://arxiv.org/abs/2606.18283)

arXiv:2606.18283v1 Announce Type: new
Abstract: The dense token-to-token interaction pattern of standard dot-product attention remains a central bottleneck in scaling Transformer architectures to long contexts. We introduce \textbf{Gaussian Mixture Attention (GMA)}, a probabilistic attention-style sequence mixer that replaces explicit pairwise query--key comparison with routing through $K$ learned Gaussian mixture components. Queries and keys are mapped to posterior \textit{responsibility} vectors over a shared latent routing space; their overlap defines an implicit responsibility-space affinity, while values are written into and read from a $K$-slot latent memory. By exploiting the associativity of matrix multiplication, GMA avoids materializing the induced $N\times N$ affinity matrix and instead uses two responsibility matrices whose dominant activation storage scales as $\mathcal{O}(NK)$ rather than $\mathcal{O}(N^2)$ for fixed $K$. We formulate bidirectional and causal variants of GMA, provide an end-to-end differentiable parameterization of the Gaussian mixture components, and analyze its responsibility-modulated gradient structure, constrained non-negative low-rank affinity interpretation, and local routing stability. Empirically, GMA exhibits the intended fixed-$K$ linear memory scaling and is competitive with attention-style baselines on long-context classification, while causal GMA improves over tested linear/random-feature attention variants on WikiText-103 but remains behind optimized causal SDPA and Mamba in the current implementation. Analysis of learned responsibilities further shows broad component usage and moderate alignment with surface-form token categories, supporting GMA as a probabilistic, interpretable, fixed-$K$ linear-time attention-style alternative rather than a universal replacement for optimized softmax attention or state-space models.
