---
interest: medium
link: https://arxiv.org/abs/2604.23106
next_step: skim
priority: low
slack_ts: '1777434599.101459'
source: cs.SE - Software Engineering
status: unread
title: 'No Test Cases, No Problem: Distillation-Driven Code Generation for Scientific
  Workflows'
---
# No Test Cases, No Problem: Distillation-Driven Code Generation for Scientific Workflows
> 原文: [https://arxiv.org/abs/2604.23106](https://arxiv.org/abs/2604.23106)

arXiv:2604.23106v1 Announce Type: new
Abstract: Existing multi-agent Large Language Model (LLM) frameworks for code generation typically use execution feedback and improve iteratively using Input/Output (I/O) test cases. However, this does not work for scientific workflows, where I/O test cases do not exist, and generating them requires solving the very problem at hand. To address this, we introduce MOSAIC, a training-free multi-agent framework for scientific code generation without I/O supervision. Instead of execution feedback, MOSAIC employs a student-teacher knowledge distillation framework that grounds generation through domain-specific examples and structured problem decomposition. To further mitigate hallucinations across chained subproblems, we introduce a Consolidated Context Window (CCW) for maintaining consistent reasoning across agents. Experiments on the SciCode benchmark show that MOSAIC improves accuracy, executability, and numerical precision over existing approaches while relying on lightweight models.
