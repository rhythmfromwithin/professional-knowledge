---
interest: medium
link: https://arxiv.org/abs/2606.27378
next_step: skim
priority: high
slack_ts: '1782708423.129589'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Formalizing Latent Thoughts: Four Axioms of Thought Representation in LLMs'
---
# Formalizing Latent Thoughts: Four Axioms of Thought Representation in LLMs
> 原文: [https://arxiv.org/abs/2606.27378](https://arxiv.org/abs/2606.27378)

arXiv:2606.27378v1 Announce Type: new
Abstract: We introduce an axiomatic evaluation framework for latent thought representations in LLMs, comprising metrics that are independent of downstream benchmark scores and reveal representational failures that benchmark accuracy masks. Existing evaluations conflate representation quality with model capacity. Therefore, failures cannot be attributed to the representation rather than to the model that processes it. We formalize four functional axioms (Causality, Minimality, Separability, and Stability) and define a quantitative measure for each, computed directly on the representation independently of downstream accuracy. We audit open-weight LLMs across 23 reasoning tasks (e.g., Spatial Reasoning, Factual QA). We find that no candidate satisfies all four axioms simultaneously, that the representations distinguish task type reliably but cannot distinguish between two questions within the same task, and that the representations encode little information beyond what is already present in the input embedding. The failure is consistent across dense, reasoning-distilled, and RL-trained model families, indicating that the gap is structural rather than a property of model size or training procedure.
