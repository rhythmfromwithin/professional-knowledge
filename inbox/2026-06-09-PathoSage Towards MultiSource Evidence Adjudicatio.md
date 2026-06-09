---
interest: medium
link: https://arxiv.org/abs/2606.07549
next_step: skim
priority: high
slack_ts: '1780978312.450319'
source: cs.AI - Artificial Intelligence
status: unread
title: 'PathoSage: Towards Multi-Source Evidence Adjudication in Pathology via Experience-Aware
  Agentic Workflow'
---
# PathoSage: Towards Multi-Source Evidence Adjudication in Pathology via Experience-Aware Agentic Workflow
> 原文: [https://arxiv.org/abs/2606.07549](https://arxiv.org/abs/2606.07549)

arXiv:2606.07549v1 Announce Type: new
Abstract: Recent advances in Multimodal Large Language Models (MLLMs) and agent workflows have shown strong promise for computational pathology, yet reliable patch-level reasoning remains challenging. End-to-end pathology MLLMs often hallucinate morphological features, while recent agentic systems usually merge tool outputs and retrieved knowledge into a shared context, making decisions vulnerable to conflicting evidence and context contamination. We propose PathoSage, a three-stage framework that explicitly separates knowledge retrieval, evidence collection, and evidence adjudication for patch-level pathology multimodal reasoning. Its core component, Structured Evidence Deliberation, independently evaluates heterogeneous evidence from tools, performs conflict analysis, and generates the final judgment in a fresh context to reduce anchoring bias. We further introduce a training-free Beta-Bernoulli experience system with continuous credit assignment to model long-term tool reliability and construct similarity-weighted priors for future tool use. Experiments show that PathoSage effectively mitigates VQA hallucinations and classifier disagreement, outperforming strong pathology MLLM and agentic baselines. Our results highlight explicit evidence adjudication and reliability-aware tool modeling as key ingredients for robust pathology agents.
