---
interest: medium
link: https://arxiv.org/abs/2606.23938
next_step: skim
priority: high
slack_ts: '1782274338.578479'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Neuro-Symbolic Drive: Rule-Grounded Faithful Reasoning for Driving VLAs'
---
# Neuro-Symbolic Drive: Rule-Grounded Faithful Reasoning for Driving VLAs
> 原文: [https://arxiv.org/abs/2606.23938](https://arxiv.org/abs/2606.23938)

arXiv:2606.23938v1 Announce Type: new
Abstract: Driving VLA models incorporating Chain-of-Thought (CoT) reasoning are attractive because they leverage pretrained VLM representations and expose intermediate decisions in natural language, yet current rationales often lack the step-by-step decision semantics needed to keep the rationale causally connected to the planned motion. We introduce Neuro-Symbolic Drive, a neuro-symbolic driving framework that supervises a driving VLA with rule-grounded reasoning traces extracted directly from classical rule-based planners. Our key observation is that rule-based planners are symbolic AI systems that already function as executable reasoning engines: they reason about active safety constraints, search over candidate maneuvers, and select a final trajectory. We instrument these planners in simulation to capture both the executed trajectory and the internal decision trace at each rule-evaluation step. Each trace is serialized into structured rule-grounded reasoning and paired with the trajectory to fine-tune Qwen3.5-4B as a driving VLA. Because these traces are derived directly from the planner states that determine the action, they ensure reasoning is structurally coupled to motion generation by construction, rather than by post-hoc alignment. On our simulator-generated benchmark, detailed rule-grounded reasoning reduces ADE@3s from 0.47 to 0.26 and miss rate from 8.30% to 6.40% under three-camera perception, and from 0.54 to 0.26 and 10.13% to 5.99% under eight-camera perception. Neuro-Symbolic Drive thus converts neuro-symbolic planning logic into structured supervision. Code base: https://github.com/XiangboGaoBarry/Neural-Symbolic-Drive.
