---
interest: medium
link: https://arxiv.org/abs/2611.31302
next_step: skim
priority: low
slack_ts: '1795850654.226809'
source: cs.CR - Cryptography and Security
status: unread
title: Towards Efficient Attack Tree Generation from Attack Graphs for Unobservable
  Target Analysis
---
# Towards Efficient Attack Tree Generation from Attack Graphs for Unobservable Target Analysis
> 原文: [https://arxiv.org/abs/2611.31302](https://arxiv.org/abs/2611.31302)

arXiv:2611.31302v1 Announce Type: new
Abstract: Attack trees provide a structured approach to security analysis but traditionally require prior knowledge of the attacker's objective. In practice, this objective often remains hidden, even when some attacker actions are partially detected. This paper presents a methodology for generating attack trees without assuming a predefined target by modeling the threat environment as a constraint-weighted graph and applying temporal reachability analysis. The approach identifies probable attacker locations from partial observations and a time budget, carrying traversal cost as an attack-tree attribute. It then extracts target-oriented subgraphs that preserve feasible attack paths while eliminating irrelevant nodes. We demonstrate the framework across three scenarios: a single office building, a multi-building industrial complex, and a real IoT device-communication network recovered from the CICIoT2023 attack dataset. Compared with the baselines, our approach achieves a lower reduction factor while maintaining complete target preservation, substantially outperforming topology-only methods that ignore temporal constraints. We further perform a sensitivity analysis across 66 weight configurations, showing that target identification is stable when strategic value receives at least 20\% of the weight in the single building and at least 50\% in the multi-building complex, while additional experiments reveal sensitivity to perturbations of the underlying strategic-value prior.
