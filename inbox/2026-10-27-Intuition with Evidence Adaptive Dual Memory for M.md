---
title: "Intuition with Evidence: Adaptive Dual Memory for Multimodal Agents"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.33019
priority: medium
status: unread
interest: medium
next_step: skim
---
# Intuition with Evidence: Adaptive Dual Memory for Multimodal Agents
> 原文: [https://arxiv.org/abs/2610.33019](https://arxiv.org/abs/2610.33019)

arXiv:2610.33019v1 Announce Type: new
Abstract: As multimodal agents engage in sustained interactions, long-term memory serves two distinct but complementary functions: fine-grained evidence recall and internalized interpretation for global understanding. Although episodic and latent memory address these demands through explicit historical records and internalized experience, neither paradigm alone can accommodate the diverse memory affinities across tasks, owing to limitations in episodic evidence coverage and integration, and in latent factual grounding. To bridge this divide, we propose a dual-memory framework, unifying a model-native latent memory as an intuitive prior with a multi-indexed episodic memory for exact evidence reconstruction via retrieval-conditioned joint alignment. At inference, the framework adaptively composes these memories through a training-free routing mechanism driven by Jensen-Shannon Divergence (JSD) sensitivity and confidence proxies for query-dependent memory affinity. Extensive evaluations across multimodal benchmarks demonstrate state-of-the-art performance, outperforming single-paradigm baselines overall (+4.67\% over vanilla Episodic), with further analysis highlighting episodic strengths in evidence-localized tasks and latent contributions to integrating dispersed information and compensating for imperfect retrieval.
