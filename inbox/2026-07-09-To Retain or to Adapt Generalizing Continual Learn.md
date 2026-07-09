---
interest: medium
link: https://arxiv.org/abs/2607.05609
next_step: skim
priority: medium
slack_ts: '1783569540.359429'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: To Retain or to Adapt? Generalizing Continual Learning
---
# To Retain or to Adapt? Generalizing Continual Learning
> 原文: [https://arxiv.org/abs/2607.05609](https://arxiv.org/abs/2607.05609)

arXiv:2607.05609v1 Announce Type: new
Abstract: The Continual Learning (CL) literature has long been driven by the goal of mitigating catastrophic forgetting. This objective rests on a pervasive, often unstated assumption: that a lifelong learner should approximate the Joint-Task Learning (JTL) solution and retain all previously acquired knowledge. We challenge this retention-centered premise, arguing that in non-stationary environments prioritizing retention can impede real-time adaptation. Shifting the focus to the Average Lifelong Error (ALE), we formalize CL as an online optimization problem governed by the interaction between environmental and learning dynamics. We introduce Transfer Efficiency as a quantitative measure of the tension between Instability, the bias inherited from conflicting past experience, and Transient Error, the optimization cost of learning new tasks from scratch. Under mild convergence conditions, holding across linear and neural network models, this decomposition yields a Critical Task Duration: a closed-form threshold beyond which historical knowledge transitions from a warm-start advantage to an optimization liability whenever retention induces a positive stationary bias. We validate these theoretical predictions on continual image classification and reinforcement learning benchmarks. Finally, by connecting continual learning to the online learning framework of predictable sequences, we show that JTL is only one instance of a broader family of objectives, and we propose a new general class of continual learning algorithms, which we call Predictive Continual Learning. Predictive CL algorithms optimize expected future performance under an explicit, dynamically updated model of future tasks. As a proof of concept, we analyze a Window algorithm that interpolates between JTL and Independent-Task Learning (ITL), outperforming both under controlled distributional drift.
