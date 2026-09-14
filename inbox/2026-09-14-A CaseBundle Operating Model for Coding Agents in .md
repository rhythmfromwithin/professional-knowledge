---
interest: medium
link: https://arxiv.org/abs/2609.11941
next_step: skim
priority: low
slack_ts: '1789360361.899719'
source: cs.SE - Software Engineering
status: unread
title: A Case-Bundle Operating Model for Coding Agents in OpenFOAM-Based CFD
---
# A Case-Bundle Operating Model for Coding Agents in OpenFOAM-Based CFD
> 原文: [https://arxiv.org/abs/2609.11941](https://arxiv.org/abs/2609.11941)

arXiv:2609.11941v1 Announce Type: new
Abstract: General-purpose coding agents can set up computational fluid dynamics (CFD) cases, execute solvers, and manage remote jobs. Reviewable and reusable work additionally depends on persistent engineering context and evidence. We present a case-bundle operating model with two modes. Build supports agent-assisted case development under engineering review. Replay applies a reviewed case to new variants. We used this model in an OpenFOAM-7 interFoam study for screening injector designs. GPT-5.5 in Codex helped develop a case bundle containing the simulation configuration, geometry-processing and meshing procedures, remote-execution scripts, post-processing code, and review records. The bundle was replayed to execute and post-process 140 Stereolithography (STL) geometry variants on a remote high-performance computing system. A separate replay exercise used the Pi coding agent as the runtime with four different LLM backends. All four runs succeeded and produced verified results. Tool use and token consumption varied across runs. The results show how reviewed case bundles can support bounded, reusable automation with distinct roles for routine execution and engineering judgment.
