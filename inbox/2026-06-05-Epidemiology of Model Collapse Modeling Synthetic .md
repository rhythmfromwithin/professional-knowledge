---
interest: medium
link: https://arxiv.org/abs/2606.05168
next_step: skim
priority: high
slack_ts: '1780718911.954249'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Epidemiology of Model Collapse: Modeling Synthetic Data Contamination via
  Bilayer SIR Dynamics'
---
# Epidemiology of Model Collapse: Modeling Synthetic Data Contamination via Bilayer SIR Dynamics
> 原文: [https://arxiv.org/abs/2606.05168](https://arxiv.org/abs/2606.05168)

arXiv:2606.05168v1 Announce Type: new
Abstract: Training on synthetic data causes model collapse, but existing analyses treat this as single-chain degradation. In reality, the AI ecosystem involves cross-contamination: models ingest synthetic data from other models, produce new synthetic text, and contaminate shared corpora. We propose a bilayer coupled SIR/SIRS framework -- a phenomenological mean-field model treating data corpora and AI models as two interacting populations, each with susceptible, infected, and recovered compartments linked by cross-layer transmission. The SIRS variant (our primary recommendation) incorporates immunity waning, reflecting that filtered corpora and retrained models remain susceptible to re-contamination. We derive the basic reproduction number $R\_0 = \sqrt{\beta\_D \beta\_M / [(\gamma\_D+\mu\_D)(\gamma\_M+\mu\_M)]}$ via the Next Generation Matrix and apply standard epidemic threshold results to the bilayer system. Illustrative scenario-based calibration from public AI text prevalence data yields supercritical dynamics ($R\_0 > 1$) across three scenarios; Sobol sensitivity analysis identifies synthetic-text detection as the highest-leverage parameter. A bipartite-network agent-based model confirms mean-field consistency ($R^2 > 0.96$) for dense networks but degrades under heterogeneity. GPT-2 contamination chain experiments (192 runs across WikiText and Shakespeare) show dose-response degradation and diversity loss qualitatively consistent with the threshold picture. Matched-budget source-diversity experiments (1,088 runs) provide suggestive evidence that multi-source mixing modestly attenuates collapse, but the effect vanishes at lower contamination fractions. Intervention analysis identifies detection-based filtering and herd immunity as the highest-leverage strategies.
