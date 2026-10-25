---
interest: medium
link: https://arxiv.org/abs/2610.30421
next_step: skim
priority: medium
slack_ts: '1792901839.561619'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: High-Value Training Data from Noisy, Diverse Sources
---
# High-Value Training Data from Noisy, Diverse Sources
> 原文: [https://arxiv.org/abs/2610.30421](https://arxiv.org/abs/2610.30421)

arXiv:2610.30421v1 Announce Type: new
Abstract: Training state-of-the-art models increasingly requires learning from large, heterogeneous datasets whose examples vary in quality, domain relevance, and source of supervision. Dataweighting---assigning different weights to training examples---offers a general way to control how such data influences training, but learning effective weights at scale remains challenging. We develop a scalable approach to learning dataweights: given a small, high-quality target dataset, we use metagradients through the training process to efficiently optimize training-example weights directly for performance on the target domain. To scale beyond a fixed dataset and model, we learn parametric weighting rules that generalize to new and streaming examples and transfer from smaller models to substantially larger ones. We study reward modeling as a prototypical application, where preference data may be noisy, adversarial, synthetic, or mismatched with the target domain. Learned dataweights improve held-out performance, automatically adapt reward models to specialized domains, and allow mixtures of human and synthetic supervision to outperform either source alone.
