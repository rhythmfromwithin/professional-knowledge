---
interest: medium
link: https://arxiv.org/abs/2610.23867
next_step: skim
priority: high
slack_ts: '1792556395.363959'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Composable Parametric Demographic Injection for Values Survey Simulation
---
# Composable Parametric Demographic Injection for Values Survey Simulation
> 原文: [https://arxiv.org/abs/2610.23867](https://arxiv.org/abs/2610.23867)

arXiv:2610.23867v1 Announce Type: new
Abstract: Large language models (LLMs) are increasingly used as simulated respondents in computational social science, yet accurately reproducing population-specific heterogeneous response distributions remains challenging. Existing methods such as demographic prompting are sensitive to prompt design and increase inference overhead, while parameter-based methods struggle to reuse demographic information efficiently, limiting generalization to unseen combinations. In this regard, we propose PARADE, a composable PARAmetric DEmographic injection framework that represents each demographic attribute value with a reusable and composable LoRA module. Specifically, PARADE separates task-common survey capability from demographic-specific value shifts via a shared Task LoRA and attribute-level Demographic LoRAs, with composition calibration to reduce parameter interference. At inference time, target population models can be constructed on demand by recombining the relevant modules, including demographic combinations not observed during training. Extensive experiments on the World Values Survey and SocioBench across three backbone models show that PARADE achieves strong population-level distribution alignment while maintaining competitive predictive performance, reducing KL divergence by up to 52.8% relative to the strongest baseline.
