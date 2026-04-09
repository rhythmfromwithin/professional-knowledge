---
interest: medium
link: https://arxiv.org/abs/2604.05807
next_step: skim
priority: low
slack_ts: '1775703396.637219'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Constraint-Driven Warm-Freeze for Efficient Transfer Learning in Photovoltaic
  Systems
---
# Constraint-Driven Warm-Freeze for Efficient Transfer Learning in Photovoltaic Systems
> 原文: [https://arxiv.org/abs/2604.05807](https://arxiv.org/abs/2604.05807)

arXiv:2604.05807v1 Announce Type: new
Abstract: Detecting cyberattacks in photovoltaic (PV) monitoring and MPPT control signals requires models that are robust to bias, drift, and transient spikes, yet lightweight enough for resource-constrained edge controllers. While deep learning outperforms traditional physics-based diagnostics and handcrafted features, standard fine-tuning is computationally prohibitive for edge devices. Furthermore, existing Parameter-Efficient Fine-Tuning (PEFT) methods typically apply uniform adaptation or rely on expensive architectural searches, lacking the flexibility to adhere to strict hardware budgets. To bridge this gap, we propose Constraint-Driven Warm-Freeze (CDWF), a budget-aware adaptation framework. CDWF leverages a brief warm-start phase to quantify gradient-based block importance, then solves a constrained optimization problem to dynamically allocate full trainability to high-impact blocks while efficiently adapting the remaining blocks via Low-Rank Adaptation (LoRA). We evaluate CDWF on standard vision benchmarks (CIFAR-10/100) and a novel PV cyberattack dataset, transferring from bias pretraining to drift and spike detection. The experiments demonstrate that CDWF retains 90 to 99% of full fine-tuning performance while reducing trainable parameters by up to 120x. These results establish CDWF as an effective, importance-guided solution for reliable transfer learning under tight edge constraints.
