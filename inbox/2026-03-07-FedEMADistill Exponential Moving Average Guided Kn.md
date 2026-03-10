---
title: "FedEMA-Distill: Exponential Moving Average Guided Knowledge Distillation for Robust Federated Learning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.04422
priority: high
status: unread
interest: medium
next_step: skim
---
# FedEMA-Distill: Exponential Moving Average Guided Knowledge Distillation for Robust Federated Learning
> 原文: [https://arxiv.org/abs/2603.04422](https://arxiv.org/abs/2603.04422)

arXiv:2603.04422v1 Announce Type: new
Abstract: Federated learning (FL) often degrades when clients hold heterogeneous non-Independent and Identically Distributed (non-IID) data and when some clients behave adversarially, leading to client drift, slow convergence, and high communication overhead. This paper proposes FedEMA-Distill, a server-side procedure that combines an exponential moving average (EMA) of the global model with ensemble knowledge distillation from client-uploaded prediction logits evaluated on a small public proxy dataset. Clients run standard local training, upload only compressed logits, and may use different model architectures, so no changes are required to client-side software while still supporting model heterogeneity across devices. Experiments on CIFAR-10, CIFAR-100, FEMNIST, and AG News under Dirichlet-0.1 label skew show that FedEMA-Distill improves top-1 accuracy by several percentage points (up to +5% on CIFAR-10 and +6% on CIFAR-100) over representative baselines, reaches a given target accuracy in 30-35% fewer communication rounds, and reduces per-round client uplink payloads to 0.09-0.46 MB, i.e., roughly an order of magnitude less than transmitting full model weights. Using coordinate-wise median or trimmed-mean aggregation of logits at the server further stabilizes training in the presence of up to 10-20% Byzantine clients and yields well-calibrated predictions under attack. These results indicate that coupling temporal smoothing with logits-only aggregation provides a communication-efficient and attack-resilient FL pipeline that is deployment-friendly and compatible with secure aggregation and differential privacy, since only aggregated or obfuscated model outputs are exchanged.
