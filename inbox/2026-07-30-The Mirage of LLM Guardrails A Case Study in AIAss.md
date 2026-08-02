---
interest: medium
link: https://arxiv.org/abs/2607.24859
next_step: skim
priority: low
slack_ts: '1785641744.926849'
source: cs.CR - Cryptography and Security
status: unread
title: 'The Mirage of LLM Guardrails: A Case Study in AI-Assisted Medical Note Manipulation'
---
# The Mirage of LLM Guardrails: A Case Study in AI-Assisted Medical Note Manipulation
> 原文: [https://arxiv.org/abs/2607.24859](https://arxiv.org/abs/2607.24859)

arXiv:2607.24859v1 Announce Type: new
Abstract: The rapid deployment of large language models (LLMs) in healthcare settings makes the reliability of their built-in guardrails against malicious queries a question of urgent practical consequence. Yet the robustness of these mechanisms against deliberate misuse (in the healthcare context) remains poorly understood. In this paper, we investigate this question empirically, using AI-assisted medical note manipulation as a concrete case study. We make four novel contributions. First, we develop a reproducible manipulation pipeline that takes publicly available seed medical note templates and use commercial LLMs to produce customized manipulated notes by substituting patient names, provider identities, dates, and medical conditions across multiple model families, input formats, and prompt phrasings. Second, we conduct a systematic empirical evaluation of LLM guardrail robustness for medical note manipulation. Our experimental results reveal substantial weaknesses and inconsistencies in contemporary commercial LLM guardrails, including low refusal rates for several model families. Third, we utilize a combination of automated metrics and human annotation-based metrics to assess the correctness of requested manipulations. Fourth, we conduct a user-study to assess the believability of manipulated medical notes, finding that the best manipulations are visually indistinguishable from original documents to human raters. Finally, we discuss implications for responsible guardrail design in LLMs, AI safety policies, and the broader ethics of deploying LLMs in healthcare settings.
