---
interest: medium
link: https://arxiv.org/abs/2609.01687
next_step: skim
priority: high
slack_ts: '1788581034.093909'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Learning Evidence Sufficiency Boundaries for Selective Answering in Grounded
  Multi-Hop QA
---
# Learning Evidence Sufficiency Boundaries for Selective Answering in Grounded Multi-Hop QA
> 原文: [https://arxiv.org/abs/2609.01687](https://arxiv.org/abs/2609.01687)

arXiv:2609.01687v1 Announce Type: new
Abstract: Grounded question answering systems should answer only when the supplied evidence supports the answer. In multi-hop QA, this requirement is difficult because partial evidence can make an unsupported answer appear plausible. We study selective answering through evidence sufficiency boundaries: for the same question, a model should abstain under unsupported or partially supported context, answer when the context first becomes sufficient, and keep the answer stable when redundant evidence is added. We introduce Evidence Sufficiency Boundary Training, a generation-native training framework that constructs ordered evidence chains and supervises the abstain-to-answer transition directly. The method combines level supervision, a boundary flip margin, post-boundary stability, and answer recall protection. We build evidence chains from HotpotQA, 2WikiMultiHopQA, and MuSiQue, then evaluate models with chain metrics, raw QA utility, and unsupported-answer rates on external non-answerable sets. With Qwen2.5-3B-Instruct and LoRA adaptation, Evidence Sufficiency Boundary Training gives the strongest boundary localization among the tested systems, with flip accuracy of 0.807 compared with 0.781 for a token-level abstention baseline. It also achieves the lowest overall unsupported-answer rate on external non-answerable evaluation, 0.095 compared with 0.101 for the same baseline, while retaining competitive raw QA F1. The results show that grounded selective answering improves when training marks the evidence level where refusal should give way to answering.
