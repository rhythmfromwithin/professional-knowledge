---
title: "Delay Complexity Dimension: Learning with Delayed and Censored Labels"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.18935
priority: medium
status: unread
interest: medium
next_step: skim
---
# Delay Complexity Dimension: Learning with Delayed and Censored Labels
> 原文: [https://arxiv.org/abs/2610.18935](https://arxiv.org/abs/2610.18935)

arXiv:2610.18935v1 Announce Type: new
Abstract: We study PAC learning of binary classifiers when labels arrive after random delays and are censored beyond an observation window $W$. How many samples does this observation model require? We propose a distribution-dependent answer, the Delay Complexity Dimension (DCD). The DCD combines the VC dimension with the exact label-information rate of the observation channel. Every learner needs $\Omega(\mathrm{DCD}/\varepsilon^2)$ samples. An oracle pseudo-label ERM matches this rate on the instance family of the lower bound, up to constants and logarithmic factors. On that family the DCD is within a constant factor of the classical censored-ERM complexity, and whether the DCD rate is achievable where the two separate remains open. The theory also yields a quantization scheme under which delay information lowers the residual label variance, an expedition policy with a $(1-1/e)$ guarantee for its version-space objective, and a phenomenon with no analogue in the no-delay setting. Under a fixed collection horizon, a moderate window can strictly beat immediate labels. Experiments on synthetic data and the Criteo conversion logs support these predictions. A budget-matched test of a companion labeler-diversity prediction is reported as a negative result.
