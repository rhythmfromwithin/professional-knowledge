---
interest: medium
link: https://arxiv.org/abs/2603.14597
next_step: skim
priority: low
slack_ts: '1773802311.503659'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'D-MEM: Dopamine-Gated Agentic Memory via Reward Prediction Error Routing'
---
# D-MEM: Dopamine-Gated Agentic Memory via Reward Prediction Error Routing
> 原文: [https://arxiv.org/abs/2603.14597](https://arxiv.org/abs/2603.14597)

arXiv:2603.14597v1 Announce Type: new
Abstract: Autonomous LLM agents require structured long-term memory, yet current "append-and-evolve" systems like A-MEM face O(N^2) write-latency and excessive token costs. We introduce D-MEM (Dopamine-Gated Agentic Memory), a biologically inspired architecture that decouples short-term interaction from cognitive restructuring via a Fast/Slow routing system based on Reward Prediction Error (RPE). A lightweight Critic Router evaluates stimuli for Surprise and Utility. Routine, low-RPE inputs are bypassed or cached in an O(1) fast-access buffer. Conversely, high-RPE inputs, such as factual contradictions or preference shifts, trigger a "dopamine" signal, activating the O(N) memory evolution pipeline to reshape the agent's knowledge graph. To evaluate performance under realistic conditions, we introduce the LoCoMo-Noise benchmark, which injects controlled conversational noise into long-term sessions. Evaluations demonstrate that D-MEM reduces token consumption by over 80%, eliminates O(N^2) bottlenecks, and outperforms baselines in multi-hop reasoning and adversarial resilience. By selectively gating cognitive restructuring, D-MEM provides a scalable, cost-efficient foundation for lifelong agentic memory.
