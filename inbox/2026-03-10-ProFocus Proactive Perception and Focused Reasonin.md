---
title: "ProFocus: Proactive Perception and Focused Reasoning in Vision-and-Language Navigation"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.05530
priority: medium
status: unread
interest: medium
next_step: skim
---
# ProFocus: Proactive Perception and Focused Reasoning in Vision-and-Language Navigation
> 原文: [https://arxiv.org/abs/2603.05530](https://arxiv.org/abs/2603.05530)

arXiv:2603.05530v1 Announce Type: new
Abstract: Vision-and-Language Navigation (VLN) requires agents to accurately perceive complex visual environments and reason over navigation instructions and histories. However, existing methods passively process redundant visual inputs and treat all historical contexts indiscriminately, resulting in inefficient perception and unfocused reasoning. To address these challenges, we propose \textbf{ProFocus}, a training-free progressive framework that unifies \underline{Pro}active Perception and \underline{Focus}ed Reasoning through collaboration between large language models (LLMs) and vision-language models (VLMs). For proactive perception, ProFocus transforms panoramic observations into structured ego-centric semantic maps, enabling the orchestration agent to identify missing visual information needed for reliable decision-making, and to generate targeted visual queries with corresponding focus regions that guide the perception agent to acquire the required observations. For focused reasoning, we propose Branch-Diverse Monte Carlo Tree Search (BD-MCTS) to identify top-$k$ high-value waypoints from extensive historical candidates. The decision agent focuses reasoning on the historical contexts associated with these waypoints, rather than considering all historical waypoints equally. Extensive experiments validate the effectiveness of ProFocus, achieving state-of-the-art performance among zero-shot methods on R2R and REVERIE benchmarks.
