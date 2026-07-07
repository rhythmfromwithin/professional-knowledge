---
interest: medium
link: https://arxiv.org/abs/2607.02668
next_step: skim
priority: high
slack_ts: '1783397056.452959'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Improving LLMs via Validator-to-Generator Alignment
---
# Improving LLMs via Validator-to-Generator Alignment
> 原文: [https://arxiv.org/abs/2607.02668](https://arxiv.org/abs/2607.02668)

arXiv:2607.02668v1 Announce Type: new
Abstract: Large language models are inconsistent: varying prompts or including unrelated information can lead to unexpected changes in model outputs. The generator-validator (G-V) gap is one manifestation of this phenomenon, where LLMs generate responses that they then deem as invalid if re-queried to validate them. In this work, we introduce a new formulation of G-V consistency that involves a principled correction for utterance frequency. Specifically, generators often assign low likelihood to valid strings simply because those strings are a priori unlikely, which makes naive notions of G-V consistency unworkable. We show that under a natural model of rational agents answering questions with multiple answers, consistency of the validator with a frequency-corrected generator score emerges naturally. Our method, \emph{\FCPAname} (\FCPA), is a training objective implementing frequency-corrected G-V consistency for real-world LLMs. Our experimental results show that training with \FCPA{} substantially improves both G-V consistency and generator performance over prior methods, with gains of up to $+27$pp in Pearson correlation on IFEval and HumanEval, while preserving validator quality across all evaluated tasks.
