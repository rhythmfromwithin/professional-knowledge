---
interest: medium
link: https://arxiv.org/abs/2604.00703
next_step: skim
priority: low
slack_ts: '1775185084.585889'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'G-ICSO-NAS: Shifting Gears between Gradient and Swarm for Robust Neural Architecture
  Search'
---
# G-ICSO-NAS: Shifting Gears between Gradient and Swarm for Robust Neural Architecture Search
> 原文: [https://arxiv.org/abs/2604.00703](https://arxiv.org/abs/2604.00703)

arXiv:2604.00703v1 Announce Type: new
Abstract: Neural Architecture Search (NAS) has become a pivotal technique in automated machine learning. Evolutionary Algorithm (EA)-based methods demonstrate superior search quality but suffer from prohibitive computational costs, while gradient-based approaches like DARTS offer high efficiency but are prone to premature convergence and performance collapse. To bridge this gap, we propose G-ICSO-NAS, a hybrid framework implementing a three-stage optimization strategy. The Warm-up Phase pre-trains supernet weights ($w$) via differentiable methods while architecture parameters ($\alpha$) remain frozen. The Exploration Phase adopts a hybrid co-optimization mechanism: an Improved Competitive Swarm Optimizer (ICSO) with diversity-aware fitness navigates the architecture space to update $\alpha$, while gradient descent concurrently updates $w$. The Stability Phase employs fine-grained gradient-based search with early stopping to converge to the optimal architecture. By synergizing ICSO's global navigation capability with differentiable methods' efficiency, G-ICSO-NAS achieves remarkable performance with minimal cost. In the context of the DARTS search space, an accuracy of 97.46\% is achieved on CIFAR-10 with a computational budget of just 0.15 GPU-Days. The method also exhibits strong transfer potential, recording accuracies of 83.1\% (CIFAR-100) and 75.02\% (ImageNet). Furthermore, regarding the NAS-Bench-201 benchmark, G-ICSO-NAS is shown to deliver state-of-the-art results across all evaluated datasets.
