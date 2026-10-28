---
title: "UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2610.35980
priority: low
status: unread
interest: medium
next_step: skim
---
# UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity
> 原文: [https://arxiv.org/abs/2610.35980](https://arxiv.org/abs/2610.35980)

arXiv:2610.35980v1 Announce Type: new
Abstract: Game development stresses coding agents in ways general software engineering does not: correctness depends on how engine APIs, serialized scene state, and runtime behavior interact, not on source code alone. Existing benchmarks mainly target platforms such as Godot and heavily rely on LLM judges or coarse task-level outcomes. We present UnityBench-Mini3D, a benchmark of 77 project-level Unity tasks organized around seven expert-defined skill categories rather than tutorials or genres, with three difficulty tiers. Each task pairs a complete Unity project with natural-language requirements and is evaluated using 1,178 held-out, human-authored milestone tests covering scene structure, component configuration, and runtime behavior. This in-engine evaluation provides deterministic partial credit, localizes failures, and distinguishes partial implementations from complete solutions without relying on subjective judges. Across 21 models and 9 coding harnesses, the average pass rate reaches 80.9% on easy tasks but falls to 35.2% on hard tasks, with just 57.7% overall. UnityBench-Mini3D provides a reproducible, diagnostic testbed distinguishing systems across difficulty levels.
