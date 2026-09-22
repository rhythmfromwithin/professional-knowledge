---
title: "When Does Learning Beat Heuristics? A Case Study in Kubernetes Scheduler Score Plugins"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.22142
priority: medium
status: unread
interest: medium
next_step: skim
---
# When Does Learning Beat Heuristics? A Case Study in Kubernetes Scheduler Score Plugins
> 原文: [https://arxiv.org/abs/2609.22142](https://arxiv.org/abs/2609.22142)

arXiv:2609.22142v1 Announce Type: new
Abstract: Kubernetes scheduler plugins that score candidate nodes are, in production, hand-tuned heuristics. We ask whether a learned scoring function - trained on real placement decisions from a production cluster trace - can match or exceed these heuristics, and if not, why. We implement an external, HTTP-backed scoring plugin for a widely used scheduler simulator and evaluate two learned models (a Random Forest over engineered features, and a graph neural network encoder over per-job task-dependency graphs) trained on a large-scale production cluster trace. Under standard regression fit (R^2), both models improve modestly but monotonically across four feature-engineering iterations, reaching R^2 of about 0.042. However, on the metric that actually matters for scheduling - Top-1 ranking accuracy, whether the model scores the machine the production scheduler actually chose highest - both learned models are outperformed by a trivial single-feature heuristic (rank by free CPU: 74-84% vs. 65-66% for either model). We show this gap is best explained by objective mismatch: both models were trained with pointwise regression (MSE) rather than a ranking-specific objective, echoing a long-standing distinction in the learning-to-rank literature. This parallels prior evidence that RL-trained schedulers can outperform heuristics when the training objective is aligned with the deployment task, suggesting objective misalignment, not architecture, is the primary obstacle here. We further report an ablation of the occupancy reconstruction required to make offline trace data usable (naive features yield R^2 near 0), a controlled comparison isolating feature richness and data volume between the two model families, and a sensitivity analysis of inference latency and serving-container memory constraints. Code, data pipelines, and experiment scripts are released for reproducibility.
