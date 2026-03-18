---
interest: medium
link: https://arxiv.org/abs/2603.08736
next_step: skim
priority: medium
slack_ts: '1773802296.419169'
source: cs.DC - Distributed Computing
status: unread
title: Autonomous Edge-Deployed AI Agents for Electric Vehicle Charging Infrastructure
  Management
---
# Autonomous Edge-Deployed AI Agents for Electric Vehicle Charging Infrastructure Management
> 原文: [https://arxiv.org/abs/2603.08736](https://arxiv.org/abs/2603.08736)

arXiv:2603.08736v1 Announce Type: new
Abstract: Public EV charging infrastructure suffers from significant failure rates -- with field studies reporting up to 27.5% of DC fast chargers non-functional -- and multi-day mean time to resolution, imposing billions in annual economic burden. Cloud-centric architectures cannot achieve the latency, reliability, and bandwidth characteristics required for autonomous operation.
We present Auralink SDC (Software-Defined Charging), an architecture deploying domain-specialized AI agents at the network edge for autonomous charging infrastructure management. Key contributions include: (1) Confidence-Calibrated Autonomous Resolution (CCAR), enabling autonomous remediation with formal false-positive bounds; (2) Adaptive Retrieval-Augmented Reasoning (ARA), combining dense and sparse retrieval with dynamic context allocation; (3) Auralink Edge Runtime, achieving sub-50ms TTFT on commodity hardware under PREEMPT\_RT constraints; and (4) Hierarchical Multi-Agent Orchestration (HMAO).
Implementation uses AuralinkLM models fine-tuned via QLoRA on a domain corpus spanning OCPP 1.6/2.0.1, ISO 15118, and operational incident histories. Evaluation on 18,000 labeled incidents in a controlled environment establishes 78% autonomous incident resolution, 87.6% diagnostic accuracy, and 28-48ms TTFT latency (P50). This work presents architecture and implementation patterns for edge-deployed industrial AI systems with safety-critical constraints.
