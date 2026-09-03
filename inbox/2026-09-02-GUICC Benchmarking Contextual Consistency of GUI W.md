---
interest: medium
link: https://arxiv.org/abs/2609.00048
next_step: skim
priority: high
slack_ts: '1788408228.735089'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments'
---
# GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments
> 原文: [https://arxiv.org/abs/2609.00048](https://arxiv.org/abs/2609.00048)

arXiv:2609.00048v1 Announce Type: new
Abstract: GUI world models are increasingly evaluated as one-step next-screen predictors, yet their intended use is often as multi-step environments for GUI agents. This mismatch leaves a key requirement under-tested: generated states must remain contextually consistent when they are repeatedly reused for future interaction. We introduce GUI-CC, a benchmark that evaluates contextual consistency of GUI world models as agent environments rather than isolated next-screen predictors. GUI-CC contains two complementary tracks: an offline reference-action track that rolls models along real mobile GUI trajectories, and an online agent-loop track that lets fixed probing agents interact with model-generated UIs. We construct 500 offline trajectory tasks from GUIOdyssey and 200 emulator-verified online tasks across 30 mobile apps. GUI-CC evaluates transition fidelity, transition plausibility, contextual consistency, and task progress. Experiments show that plausible single-step generation does not guarantee reliable environment simulation: current models often produce usable-looking screens while failing to preserve task-relevant context or support executable multi-step rollouts.
