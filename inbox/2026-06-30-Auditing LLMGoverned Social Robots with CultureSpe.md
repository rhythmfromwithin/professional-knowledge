---
interest: medium
link: https://arxiv.org/abs/2606.28345
next_step: skim
priority: medium
slack_ts: '1782792820.282199'
source: cs.RO - Robotics
status: unread
title: Auditing LLM-Governed Social Robots with Culture-Specific Moral Gradients
---
# Auditing LLM-Governed Social Robots with Culture-Specific Moral Gradients
> 原文: [https://arxiv.org/abs/2606.28345](https://arxiv.org/abs/2606.28345)

arXiv:2606.28345v1 Announce Type: new
Abstract: LLM-governed social robots increasingly decide who receives real-world assistance first. As prioritization norms vary across cultures by age, status, and group size, failure to calibrate pluralistically can scale into unequal access. Yet LLM moral audits remain English-centered, rarely test embodied contexts, leaving pluralistic calibration as an urgent diagnostic gap amid intensifying LLM-robot deployment. We introduce a gradient-based audit framework for multilingual evaluation of LLM moral trade-off behavior against cultural preference gradients. Grounded in nine cross-domain social robotics reviews (>8,000 papers), we derive symmetry-controlled scenarios across care, education, and services, translating the Moral Machine Experiment's "whom to spare" into "whom to assist first" dilemmas with preserved identity trade-offs (many vs. few; young vs. old; higher vs. lower status). We audit four LLMs across four country-language pairs in four prompting regimes (57,600 decisions), benchmarked against country-specific MME preference gradients. Ordinal concordance tests whether models differentiate cultural contexts; a governance typology maps vulnerabilities in gradient differentiation, directional tendency, and deliberation. We find persistent, culturally asymmetric gradient tracking failures that prompting alone cannot reliably correct: quality calibration is nearly twice as strong for Western-language decisions as for Chinese and Japanese; high determinism in majority-first trade-offs often erases cross-cultural gradients; partial sensitivity to age- and status-based norms risks sidelining minorities. Prompting effects are uneven; only contrastive exemplars yield consistent gains, while reasoning-only prompts can worsen tracking. Our results motivate multilingual, pluralistic audits as an LLM-robot pre-deployment gate and suggest model factors are a more robust lever than prompting alone.
