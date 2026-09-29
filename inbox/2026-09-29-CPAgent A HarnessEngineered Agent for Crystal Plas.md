---
interest: medium
link: https://arxiv.org/abs/2609.31790
next_step: skim
priority: high
slack_ts: '1790659458.902179'
source: cs.AI - Artificial Intelligence
status: unread
title: 'CP-Agent: A Harness-Engineered Agent for Crystal Plasticity Simulation Workflows'
---
# CP-Agent: A Harness-Engineered Agent for Crystal Plasticity Simulation Workflows
> 原文: [https://arxiv.org/abs/2609.31790](https://arxiv.org/abs/2609.31790)

arXiv:2609.31790v1 Announce Type: new
Abstract: Crystal plasticity (CP) simulations predict the mechanical behavior of polycrystalline metals, yet their routine use is hindered by the manual effort of configuring heterogeneous tools, orchestrating multi-step data pipelines, and calibrating constitutive parameters against experiments. These bottlenecks impede productivity in systematic parameter studies, motivating interest in automated workflows. This study presents CP-Agent, a harness-engineered LLM-based agent that autonomously executes complete CP modeling workflows from natural-language tasks. Operating under the ReAct paradigm, the agent reasons about tool selection and sequencing while delegating numerical search to established optimizers. The harness comprises a minimal system prompt, typed tool definitions, a dispatcher, and a safety-bounded iteration loop, encoding domain knowledge through tool schemas rather than hard-coded logic. CP-Agent is demonstrated on four case studies: calibrating four slip parameters of additively manufactured stainless steel 316L against tensile data; validating the workflow against published copper benchmarks, reproducing stress-strain and texture evolution; recovering the initial crystallographic texture of copper, where the agent correctly identifies a diffuse initial texture; and reproducing the multi-pass rolling texture evolution of a Mg-Zn-Ca alloy, where the agent chains five deformation passes and recovers the experimentally observed weakened, split basal texture. In all cases, the agent inferred the correct execution sequence from the task statement, robustly across repeated runs, and delivered physically interpretable results. This work establishes harness engineering as a systematic approach to automating CP modeling workflows while maintaining physical interpretability and auditability through visible reasoning traces.
