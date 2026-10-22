---
interest: medium
link: https://arxiv.org/abs/2610.28767
next_step: skim
priority: high
slack_ts: '1792642794.774129'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'SkillEval: Learning Interpretable Ability Profiles of LLMs via Cognitive Diagnosis
  Models'
---
# SkillEval: Learning Interpretable Ability Profiles of LLMs via Cognitive Diagnosis Models
> 原文: [https://arxiv.org/abs/2610.28767](https://arxiv.org/abs/2610.28767)

arXiv:2610.28767v1 Announce Type: new
Abstract: Current evaluation of LLMs on benchmarks typically aggregates performance over individual examples into a single scalar score. This approach is overly coarse and ignores the diverse scope of skills covered by benchmark datasets. To address this limitation and better exploit benchmark data, we propose SkillEval, a new evaluation framework that performs cross-model, skill-level analysis. The framework integrates advances from two areas: (1) it leverages the meta-cognitive capabilities of LLMs to automatically discover interpretable skills from questions, and (2) it applies cognitive diagnosis models (CDMs) from psychometrics to estimate per-skill abilities of LLMs. We conduct experiments on 3,811 LLMs evaluated on 9,523 items across five benchmarks spanning diverse domains (MATH, BBH, GPQA, MuSR, IFEval). Compared to the traditional average-based evaluation paradigm, SkillEval produces reliable, more calibrated and informative yet concise model profiles that more accurately predict model behavior on unseen items. We also demonstrate the utility of SkillEval in two downstream tasks: (1) LLM routing, which dynamically assigns each query to a capable but efficient model, reducing inference cost by over 60% while achieving improved performance, and (2) Computerized Adaptive Testing (CAT), where an unseen model can be efficiently evaluated using a trained CDM. Furthermore, we show that these skill profiles provide useful insights, for example, how benchmarks share skills and how instruction-tuned models differ from their base models.
