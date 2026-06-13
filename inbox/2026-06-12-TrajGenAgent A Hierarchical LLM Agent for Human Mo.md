---
interest: medium
link: https://arxiv.org/abs/2606.12657
next_step: skim
priority: low
slack_ts: '1781324788.904969'
source: cs.DB - Databases
status: unread
title: 'TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation'
---
# TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation
> 原文: [https://arxiv.org/abs/2606.12657](https://arxiv.org/abs/2606.12657)

arXiv:2606.12657v1 Announce Type: cross
Abstract: Human mobility data is important for transportation, urban planning, and epidemic control, but large-scale trajectory collection is often costly and privacy-constrained, motivating realistic synthetic trajectory generation. Existing LLM-based generators typically rely on either prompt engineering, which preserves zero-shot reasoning but lacks fine-grained spatiotemporal grounding, or trajectory-level fine-tuning, which improves statistical precision but incurs substantial computational cost and may weaken general reasoning. We propose TrajGenAgent, a semantic-aware hierarchical LLM-agent framework for human mobility trajectory generation without model fine-tuning. TrajGenAgent uses a two-stage orchestrator-worker design: an LLM first synthesizes an individual- and weekday-conditioned activity chain from historical evidence via in-context learning, and a deterministic workflow then grounds each activity into a complete visit using personalized POI retrieval, distance-aware location selection, kinematics-aware travel-time propagation, and LLM-based duration estimation. To evaluate realism beyond aggregate spatiotemporal statistics, we introduce an anomaly-detection-based evaluation framework using two complementary detectors to assess behavioral and semantic plausibility. Experiments on benchmark and large-scale simulation datasets show that TrajGenAgent improves spatiotemporal fidelity, semantic coherence, and individual-specific behavioral realism over representative neural and LLM-based baselines, while avoiding parameter updates.
