---
interest: medium
link: https://arxiv.org/abs/2611.25069
next_step: skim
priority: medium
slack_ts: '1795328176.898229'
source: cs.CV - Computer Vision
status: unread
title: 'VisAlloc: Allocating Visual Supervision for On-Policy Self-Distillation'
---
# VisAlloc: Allocating Visual Supervision for On-Policy Self-Distillation
> 原文: [https://arxiv.org/abs/2611.25069](https://arxiv.org/abs/2611.25069)

arXiv:2611.25069v1 Announce Type: new
Abstract: On-policy self-distillation (OPSD) offers a promising approach to improving visual reasoning in multimodal large language models (MLLMs). However, not all samples benefit equally from privileged visual guidance, and uniform token supervision can dilute visually grounded signals. We propose VisAlloc, a dual-level framework combining sample-level visual filtering with token-level counterfactual reweighting. A fixed paired-teacher filter retains samples answered correctly from an evidence-centered positive crop but incorrectly from a spatially displaced negative crop. At the token level, both EMA teachers score the same student-generated response, and their absolute log-probability differences measure view sensitivity. Additional supervision targets tokens admitted by sensitivity or teacher-distribution disagreement, with shared frozen-prior, template-bigram, and student--teacher divergence gates. Inverse-frequency redistribution preserves the total additional weight within each micro-batch, while the positive teacher remains the sole distillation target. Inference requires only the full-image student. Across eight benchmarks, our 4B and 9B models achieve macro-averages of 81.44 and 84.92, outperforming Vision-OPD reproductions by 0.97 and 0.52 points, respectively. Code on GitHub: https://github.com/Kaelyn01/VisAlloc
