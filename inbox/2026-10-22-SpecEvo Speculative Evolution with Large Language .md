---
interest: medium
link: https://arxiv.org/abs/2610.28706
next_step: skim
priority: high
slack_ts: '1792815247.651209'
source: cs.AI - Artificial Intelligence
status: unread
title: 'SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient
  Scientific Discovery'
---
# SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient Scientific Discovery
> 原文: [https://arxiv.org/abs/2610.28706](https://arxiv.org/abs/2610.28706)

arXiv:2610.28706v1 Announce Type: new
Abstract: LLM-driven evolutionary search is a promising paradigm for scientific discovery, but existing methods remain costly and slow, often applying expensive reasoning uniformly while underusing evidence from failed, redundant, and saturated trials. We introduce Speculative Evolution (SpecEvo), a multi-LLM framework that coordinates lightweight and frontier models through continual consolidation of search evidence. Lightweight models power both parallel Speculators, which generate and refine candidate programs, and an Advisor, which distills accumulated successes, failures, and saturated directions into persistent guidance for subsequent exploration. At sparse checkpoints, a frontier-model Navigator inspects the evolving population and intervenes through synthesis, surgical refinement, or reframing according to search stagnation. This speculate-then-consolidate workflow delegates routine exploration and evidence consolidation to inexpensive models while reserving frontier reasoning for strategic interventions whose benefits extend across many subsequent low-cost evaluations. Across 176 tasks spanning four scientific and algorithmic discovery domains, SpecEvo matches or outperforms frontier-model baselines while reducing API cost by up to 80%, achieves up to 1.5x greater evaluation efficiency than cost-efficient baselines on equation discovery, and improves over the strongest CO-Bench baseline by 3.8%. These results support trajectory-conditioned model coordination as an effective approach to cost-efficient scientific discovery.
