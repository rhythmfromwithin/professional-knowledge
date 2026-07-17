---
interest: medium
link: https://arxiv.org/abs/2607.12050
next_step: skim
priority: medium
slack_ts: '1784258634.521299'
source: cs.RO - Robotics
status: unread
title: 'EFLUX: Elastic Multi-Robot Formation Navigation and Adaptation with Agentic
  LLMs'
---
# EFLUX: Elastic Multi-Robot Formation Navigation and Adaptation with Agentic LLMs
> 原文: [https://arxiv.org/abs/2607.12050](https://arxiv.org/abs/2607.12050)

arXiv:2607.12050v1 Announce Type: new
Abstract: Multi-robot teams operating in confined or cluttered environments must adapt both their formation geometry and group topology to navigate through complex obstacles. This adaptation requires two complementary behaviors: deformation, where the team continuously reshapes its geometry while remaining connected, and reconfiguration, where robots split into subgroups or merge back into a single formation. Existing methods often model these behaviors independently, connect them through handcrafted rules, or lack explicit geometric criteria for determining when each behavior should be invoked. However, challenging environments may require online changes in formation shape, connectivity, and effective team composition, making decoupled or rule-based approaches prone to suboptimal trajectories and deadlock. We propose EFLUX, a geometry-grounded LLM agentic framework for automatic and elastic multi-robot formation navigation. EFLUX extracts a structured scene representation and uses an LLM to reason jointly over both deformation actions, such as scaling and shearing, and reconfiguration actions, such as splitting and merging. These strategies are then translated into executable per-robot waypoints through a closed-loop generation, verification, and correction pipeline. Simulation and hardware experiments show that EFLUX enables safe, continuous, and elastic formation navigation in constrained environments, reducing deadlock and navigation failures compared with baselines while maintaining coherent multi-robot coordination.
