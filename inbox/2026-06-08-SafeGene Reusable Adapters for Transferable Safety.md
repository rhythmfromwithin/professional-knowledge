---
title: "SafeGene: Reusable Adapters for Transferable Safety Alignment"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2606.06519
priority: high
status: unread
interest: medium
next_step: skim
---
# SafeGene: Reusable Adapters for Transferable Safety Alignment
> 原文: [https://arxiv.org/abs/2606.06519](https://arxiv.org/abs/2606.06519)

arXiv:2606.06519v1 Announce Type: new
Abstract: Open-weight LLMs are increasingly fine-tuned into customized assistants, but downstream fine-tuning can weaken safety alignment and make models more vulnerable to malicious prompts, even when the training data is not intentionally harmful. This creates a recurring safety recovery problem as target models are repeatedly updated with new task data or user interactions. We propose SafeGene, a reusable safety-adapter module designed for cross-task reuse within each architecture-compatible model family. Rather than treating safety recovery as a model-specific repair step, SafeGene treats safety capability as an independent, reusable adapter representation decoupled from task-specific updates. This representation is obtained from aligned--degraded model discrepancies, refined into task-transferable safety vectors through data-aware layer selection, and expressed in each downstream task-adapted model via few-shot layer-wise coefficient recalibration. Experiments across multiple model families, downstream tasks, and safety judges show that SafeGene-enhanced models reduce harmful response rates while maintaining downstream performance, outperforming representative safe adaptation methods in safety--utility trade-off.
