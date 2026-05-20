---
interest: medium
link: https://arxiv.org/abs/2605.15571
next_step: skim
priority: medium
slack_ts: '1779250484.419419'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'MaxSketch: Robust Distinct Counting in Streams via Random Projections'
---
# MaxSketch: Robust Distinct Counting in Streams via Random Projections
> 原文: [https://arxiv.org/abs/2605.15571](https://arxiv.org/abs/2605.15571)

arXiv:2605.15571v1 Announce Type: new
Abstract: Estimating the number of distinct elements in a data stream is well understood when repeated elements are identical. In modern settings, however, observations are high-dimensional and noisy, so repeated instances of the same object are only approximately similar -- for example, different images of the same individual may vary significantly at the pixel level. Classical sketches such as HyperLogLog rely on consistent hash values for identical elements and break down in this regime. Recent work on robust distinct counting in general metric spaces achieves $\widetilde{\Theta}(\sqrt{n})$ memory, which is tight in the worst case. We show that substantially improved memory guarantees are possible under geometric structure common in learned representations. We introduce MaxSketch, a simple max-linear sketch built from random Gaussian projections, and prove that it succeeds in estimating the number of distinct latent objects. Concretely, we show that under this assumption $m = \widetilde{O} (\log n / \varepsilon^2)$ random projections (and hence $\widetilde{O} (\log n/\varepsilon^2)$ memory) suffice to recover the true distinct count within a $(1+\varepsilon)$ factor. Experiments on image streams confirm that MaxSketch accurately estimates distinct counts and generalizes beyond the training regime. Our results bridge classical streaming algorithms and modern representation learning, showing how geometric structure can fundamentally reduce the complexity of distinct counting.
