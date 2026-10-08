---
title: "Route-Verify-Vote: Procedure-Conditioned Self-Consistency for Mixed-Domain Reasoning"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2610.08814
priority: high
status: unread
interest: medium
next_step: skim
---
# Route-Verify-Vote: Procedure-Conditioned Self-Consistency for Mixed-Domain Reasoning
> 原文: [https://arxiv.org/abs/2610.08814](https://arxiv.org/abs/2610.08814)

arXiv:2610.08814v1 Announce Type: new
Abstract: Compositional generalization remains challenging when language models must combine familiar reasoning operations in unfamiliar ways. The Scenario-Based Commonsense Reasoning Evaluation (SCoRE) 2026 tests this ability on three mixed domains absent from training and requires models to identify the complete set of correct options for each question.
We introduce Route-Verify-Vote (RVV), a framework for procedure-conditioned self-consistency that uses language models without parameter updates. Route uses the provided domain label to select a reasoning procedure that guides the model in representing and applying the relevant constraints. Verify prompts the model to assess each option against those constraints. Vote aggregates complete answer sets and allocates additional samples to questions with a small vote-count margin between the two most frequent sets. Samples for each question follow the same domain-specific procedure.
On the official test set, voting over 16 sampled answer sets per question achieves an exact-set accuracy of 74.6%. Adaptive RVV reaches 77.3%, and combining models on selected domain routes raises accuracy to 79.4%. The final system ranked second among participating systems. These results support domain-specific reasoning procedures and answer-set disagreement as useful tools for allocating inference-time computation in mixed-domain reasoning.
