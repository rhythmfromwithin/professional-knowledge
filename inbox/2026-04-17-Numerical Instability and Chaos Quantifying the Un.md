---
interest: medium
link: https://arxiv.org/abs/2604.13206
next_step: skim
priority: high
slack_ts: '1776482306.723579'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Numerical Instability and Chaos: Quantifying the Unpredictability of Large
  Language Models'
---
# Numerical Instability and Chaos: Quantifying the Unpredictability of Large Language Models
> 原文: [https://arxiv.org/abs/2604.13206](https://arxiv.org/abs/2604.13206)

arXiv:2604.13206v1 Announce Type: new
Abstract: As Large Language Models (LLMs) are increasingly integrated into agentic workflows, their unpredictability stemming from numerical instability has emerged as a critical reliability issue. While recent studies have demonstrated the significant downstream effects of these instabilities, the root causes and underlying mechanisms remain poorly understood. In this paper, we present a rigorous analysis of how unpredictability is rooted in the finite numerical precision of floating-point representations, tracking how rounding errors propagate, amplify, or dissipate through Transformer computation layers. Specifically, we identify a chaotic "avalanche effect" in the early layers, where minor perturbations trigger binary outcomes: either rapid amplification or complete attenuation. Beyond specific error instances, we demonstrate that LLMs exhibit universal, scale-dependent chaotic behaviors characterized by three distinct regimes: 1) a stable regime, where perturbations fall below an input-dependent threshold and vanish, resulting in constant outputs; 2) a chaotic regime, where rounding errors dominate and drive output divergence; and 3) a signal-dominated regime, where true input variations override numerical noise. We validate these findings extensively across multiple datasets and model architectures.
