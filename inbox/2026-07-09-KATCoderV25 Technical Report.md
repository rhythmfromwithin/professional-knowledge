---
interest: medium
link: https://arxiv.org/abs/2607.05471
next_step: skim
priority: low
slack_ts: '1783655933.750389'
source: cs.SE - Software Engineering
status: unread
title: KAT-Coder-V2.5 Technical Report
---
# KAT-Coder-V2.5 Technical Report
> 原文: [https://arxiv.org/abs/2607.05471](https://arxiv.org/abs/2607.05471)

arXiv:2607.05471v1 Announce Type: new
Abstract: We present KAT-Coder-V2.5, a coding-focused agentic model trained to act autonomously inside real, executable repositories rather than as a single-turn code generator. Its capability is bottlenecked less by model scale than by the scarcity of reproducible environments, verifiable rewards, and high-value trajectories, which we address with an end-to-end agentic post-training framework. AutoBuilder reconstructs multilingual repositories into sandboxed environments with fail-to-pass and pass-to-pass verification at scale, from which we regenerate self-contained task specifications, recover near-miss trajectories, and distill supervision through process-aware filtering, while KwaiClawEnv synthesizes large-scale tool-use trajectories from executable services and real task seeds. We further scale reinforcement learning with harness randomization, a reliability-hardened sandbox, an asymmetric actor--critic PPO with hindsight-augmented value estimation, and a harness-oriented reward framework, and unify SWE, Agent-Claw, and WebCoding experts via Multi-Teacher On-Policy Distillation. Across six software-engineering and agentic benchmarks, KAT-Coder-V2.5 delivers the best agentic tool-use result on PinchBench and ranks second only to the frontier Opus 4.8 on repository-level software engineering. Our service is available at https://streamlake.com/product/kat-coder.
