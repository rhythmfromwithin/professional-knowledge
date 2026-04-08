---
interest: medium
link: https://arxiv.org/abs/2604.02423
next_step: skim
priority: high
slack_ts: '1775618430.288989'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'SWAY: A Counterfactual Computational Linguistic Approach to Measuring and
  Mitigating Sycophancy'
---
# SWAY: A Counterfactual Computational Linguistic Approach to Measuring and Mitigating Sycophancy
> 原文: [https://arxiv.org/abs/2604.02423](https://arxiv.org/abs/2604.02423)

arXiv:2604.02423v1 Announce Type: new
Abstract: Large language models exhibit sycophancy: the tendency to shift outputs toward user-expressed stances, regardless of correctness or consistency. While prior work has studied this issue and its impacts, rigorous computational linguistic metrics are needed to identify when models are being sycophantic. Here, we introduce SWAY, an unsupervised computational linguistic measure of sycophancy. We develop a counterfactual prompting mechanism to identify how much a model's agreement shifts under positive versus negative linguistic pressure, isolating framing effects from content. Applying this metric to benchmark 6 models, we find that sycophancy increases with epistemic commitment. Leveraging our metric, we introduce a counterfactual mitigation strategy teaching models to consider what the answer would be if opposite assumptions were suggested. While baseline mitigation instructing to be explicitly anti-sycophantic yields moderate reductions, and can backfire, our counterfactual CoT mitigation drives sycophancy to near zero across models, commitment levels, and clause types, while not suppressing responsiveness to genuine evidence. Overall, we contribute a metric for benchmarking sycophancy and a mitigation informed by it.
