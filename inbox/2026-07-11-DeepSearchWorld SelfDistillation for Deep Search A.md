---
interest: medium
link: https://arxiv.org/abs/2607.07820
next_step: skim
priority: high
slack_ts: '1783740361.406699'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable
  Environment'
---
# DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment
> 原文: [https://arxiv.org/abs/2607.07820](https://arxiv.org/abs/2607.07820)

arXiv:2607.07820v1 Announce Type: new
Abstract: Training tool-use agents to improve from their own experience remains challenging, as supervised fine-tuning relies on fixed teacher-distilled trajectories, while sparse-reward reinforcement learning provides weak supervision for long-horizon interactions. We present DeepSearch-Evolve, a self-distillation framework for web agents built on DeepSearch-World, a deterministic and verifiable environment with reproducible search and page-reading tools. DeepSearch-World contains 420K multi-hop QA tasks constructed from entity-level random walks and supports key agentic cognitive behaviors useful for self-evolving, including progress verification, grounded reflection, and failure recovery. DeepSearch-Evolve iteratively performs trajectory generation, filtering, data mixing, and fine-tuning to train stronger agents. Without distillation from more capable models, DeepSearch-World-9B achieves competitive performance compared with open-source agents, reaching 31.2% on BrowseComp, 61.5% on GAIA, and 93.4% on HotpotQA, showing that verifiable environments enable scalable self-evolution for long-horizon web agents. We will release the environment, 420K training pool, validation set, model, and code to facilitate future research on self-improving deep search agents.
