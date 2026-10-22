---
interest: medium
link: https://arxiv.org/abs/2610.23868
next_step: skim
priority: high
slack_ts: '1792642771.928619'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Translating in style: An open-weight alternative to GPT-4 for culturally aligned
  machine translation'
---
# Translating in style: An open-weight alternative to GPT-4 for culturally aligned machine translation
> 原文: [https://arxiv.org/abs/2610.23868](https://arxiv.org/abs/2610.23868)

arXiv:2610.23868v1 Announce Type: new
Abstract: Machine translation systems often preserve meaning but systematically flatten linguistic style, a failure that is most acute when translating into non-Western languages. The RASTA framework of Havaldar et al. (2025a) addresses this through retrieval-augmented stylistic alignment, but relies on GPT-4, a closed, proprietary model. We investigate whether an open-weight translation specialist, Hunyuan-MT-7B, can serve as an open-weight alternative. We evaluate three variants of the model, the base model, a LoRA supervised fine-tune, and a GRPO-steered policy. We do this across three style dimensions (formality, politeness, and intimacy) and twelve directed language pairs, measuring style alignment with the correlation-based metric $\mathcal{A}$. We find that fine-tuning does not reliably improve alignment: the three variants are statistically indistinguishable in aggregate. The open backbone does not match RASTA-GPT-4 overall, but the shortfall is concentrated in formality and largely closes for intimacy and Chinese directions, where the open model matches or surpasses GPT-4 on individual pairs. An accessible RASTA pipeline built on an open model is thus already viable for parts of the problem.
