---
interest: medium
link: https://arxiv.org/abs/2606.07520
next_step: skim
priority: high
slack_ts: '1781065394.997189'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'TinyJudge: Unverifiable Constraint Alignment via Lightweight Specialist Ensembles'
---
# TinyJudge: Unverifiable Constraint Alignment via Lightweight Specialist Ensembles
> 原文: [https://arxiv.org/abs/2606.07520](https://arxiv.org/abs/2606.07520)

arXiv:2606.07520v1 Announce Type: new
Abstract: Instruction Following (IF) is a core capability of LLMs, requiring strict adherence to diverse constraints, ranging from verifiable ones (e.g., output length) to unverifiable ones (e.g., tone). Reinforcement learning with verifiable rewards has emerged as a paradigm for IF tasks, leveraging LLM-as-a-judge to assess unverifiable constraints. However, we empirically find that this approach remains a significant bottleneck, suffering from severe reward hacking and higher computational overhead. In this work, we first analyze the generalization capabilities of unverifiable constraints and discover that specific constraints exhibit distinct, high-generalization patterns. Motivated by this, we propose TinyJudge, a framework that employs an ensemble of specialized tiny language models ($\sim0.6B$) to provide rewards for soft constraints. By distilling expertise from frontier models into these tiny models, it achieves high-precision, lightweight evaluation. Extensive evaluations across five benchmarks demonstrate that TinyJudge outperforms the baselines by $\sim10\%$ in average performance and $12\%$ in reward precision. Crucially, it also achieves a $3\times$ speedup in total training time. Our work provides a scalable and robust path for aligning LLMs with unverifiable human instructions.
