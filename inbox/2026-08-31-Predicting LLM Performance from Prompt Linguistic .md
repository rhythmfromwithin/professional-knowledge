---
interest: medium
link: https://arxiv.org/abs/2608.27621
next_step: skim
priority: low
slack_ts: '1788237857.567569'
source: cs.SE - Software Engineering
status: unread
title: 'Predicting LLM Performance from Prompt Linguistic Features: An Empirical Study
  in Requirements Engineering'
---
# Predicting LLM Performance from Prompt Linguistic Features: An Empirical Study in Requirements Engineering
> 原文: [https://arxiv.org/abs/2608.27621](https://arxiv.org/abs/2608.27621)

arXiv:2608.27621v1 Announce Type: new
Abstract: Background. LLM outputs are highly sensitive to prompt formulation: small wording changes can substantially affect output quality. This matters in software engineering, where prompts guide requirements analysis, code generation, and artefact synthesis. Poor formulations yield unreliable artefacts, yet practitioners lack principled ways to assess a prompt before inference, making selection depend on costly LLM calls and trial-and-error refinement. Aims. We investigate whether measurable linguistic properties of prompts can predict LLM performance before inference, enabling low-cost prompt selection and refinement, validated on binary requirements classification targeting F1, F2, precision, and recall. Method. We generate 9,000 linguistically controlled prompt variants from 100 initial prompts by varying 30 linguistic metrics, evaluated with five open-source LLMs on 625 annotated requirements. Regression predictors are trained via stratified 10-fold cross-validation with permutation-based significance testing; feature importance analysis identifies cross-LLM and model-specific predictors. Results. Linguistic features significantly predict prompt performance across all targets (R2 in [0.38,0.42], q<0.05). Syntactic and morphosyntactic features drive most predictive signal; cross-LLM predictors include compound dependency distribution, conjunction density, and word/sentence length, reflecting sensitivity to domain vocabulary and complex structures. Conclusions. Results suggest practical implications for prompt engineering, including overlap between linguistic patterns that reduce LLM performance and those that increase human comprehension difficulty, and the irrelevance of lexical variety as a quality dimension. More broadly, linguistic profiling combined with standard regression provides an effective, interpretable, low-cost prior before costly optimisation pipelines.
