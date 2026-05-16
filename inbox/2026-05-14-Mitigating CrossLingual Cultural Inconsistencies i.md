---
interest: medium
link: https://arxiv.org/abs/2605.12515
next_step: skim
priority: high
slack_ts: '1778903328.062799'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven
  Preference Optimisation
---
# Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation
> 原文: [https://arxiv.org/abs/2605.12515](https://arxiv.org/abs/2605.12515)

arXiv:2605.12515v1 Announce Type: new
Abstract: Despite their impressive capabilities, multilingual large language models (MLLMs) frequently exhibit inconsistent behaviour when the prompt's language changes. While such adaptation is generally desirable, it becomes a critical failure when a user's identity is explicitly defined. For instance, given a fixed British persona and an ambiguous everyday knowledge query about literature, the prompt's language frequently overwrites the system persona -- yielding Shakespeare in English but Cervantes in Spanish. To robustly quantify this Cross-lingual Cultural Inconsistency, we introduce Singleton Fleiss's $\kappa\_S$, a metric mathematically resilient to hallucinations. For mitigation, we propose Cross-lingual Cultural Consistent Preference Optimisation (C-3PO), a consensus-driven alignment framework. C-3PO achieves up to a 0.10-point absolute increase in $\kappa\_S$ over unaligned models, outperforming strong prompting and representation steering baselines. Empirical evaluations show this inconsistency disproportionately affects lower-resource languages like Indonesian and Persian. A layer-wise interpretability analysis reveals the underlying mechanism: by early-decoding intermediate layer representations, we find that MLLMs implicitly personalise outputs towards the prompt language's stereotypical culture as forward-pass representations stabilise.
