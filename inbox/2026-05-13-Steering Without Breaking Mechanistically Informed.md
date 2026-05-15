---
interest: medium
link: https://arxiv.org/abs/2605.10971
next_step: skim
priority: high
slack_ts: '1778817947.001349'
source: cs.LG - Machine Learning
status: unread
title: 'Steering Without Breaking: Mechanistically Informed Interventions for Discrete
  Diffusion Language Models'
---
# Steering Without Breaking: Mechanistically Informed Interventions for Discrete Diffusion Language Models
> 原文: [https://arxiv.org/abs/2605.10971](https://arxiv.org/abs/2605.10971)

arXiv:2605.10971v1 Announce Type: new
Abstract: Discrete diffusion language models (DLMs) generate text by iteratively denoising all positions in parallel, offering an alternative to autoregressive models. Controlled generation methods for DLMs, imported from autoregressive models, apply uniform intervention at every denoising steps. We show this uniform schedule degrades quality, and the damage compounds when multiple attributes are steered jointly. To diagnose the failure, we train sparse autoencoders on four DLMs (124M-8B parameters) and find that different attributes commit on distinct schedules, varying in timing, sharpness, and magnitude. For instance, topic commits within the first 2\% of denoising, whereas sentiment emerges gradually over 20\% of the process. Consequently, uniform intervention wastes steering capacity on steps where the target attribute has already solidified or has yet to emerge. We propose a novel adaptive scheduler that concentrates interventions on the steps where an attribute is actively forming and leaves the rest of generation untouched. The cost-control trade-off admits a closed-form characterization: the advantage of adaptive over uniform scheduling is governed by a single dispersion statistic of the commitment distribution. Across four DLMs and seven steering tasks, our method achieves precise control without the degradation typical of uniform interventions. Especially on challenging simultaneous three-attribute control, it reaches up to 93\% steering strength, beating the strongest baseline by up to 15\% points while preserving generation quality.
