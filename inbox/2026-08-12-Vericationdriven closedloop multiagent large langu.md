---
interest: medium
link: https://arxiv.org/abs/2608.07978
next_step: skim
priority: low
slack_ts: '1786674568.505769'
source: cs.SE - Software Engineering
status: unread
title: Verication-driven closed-loop multi-agent large language modelframework for
  code-compliant structural design
---
# Verication-driven closed-loop multi-agent large language modelframework for code-compliant structural design
> 原文: [https://arxiv.org/abs/2608.07978](https://arxiv.org/abs/2608.07978)

arXiv:2608.07978v1 Announce Type: new
Abstract: Multi-agent large language model(LLM)systems are applied to structural design,yet most use one-shot generation and cannot verify their output,leaving themill-suited to safety-critical tasks.Rather than trusting LLM self-correction,thisframework injects feedback from an external physics-based verier into a closedrepair loop.The framework couples a three-layernite-element verication systemwith a dual-node loop.Node 1 turns code violations into hard repair constraints,Node 2 turns a four-dimensional quality score into safety-rst soft constraints,and a retrieval-augmented code base makes every violation traceable to a clause.Overve structure types and 44 cases,code compliance rises from 56.8%to 98.6%and the composite score from 63.8 to 71.4(p<0.000001),using about 5.8%lessmaterial.Removing either node degrades performance,and compliance does notchange detectably across the two backbone LLMs tested,indicating that it ishere attributed to the external verier rather than the model.The framework,the 44-case benchmark and all experiment scripts are released as open source forreplicability.
