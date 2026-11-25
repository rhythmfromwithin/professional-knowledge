---
interest: medium
link: https://arxiv.org/abs/2611.28077
next_step: skim
priority: medium
slack_ts: '1795593786.216959'
source: cs.CV - Computer Vision
status: unread
title: 'Fairness Evaluation for Diffusion and Flow Models Should Account for the Generation
  Path: Implications for Clinical Imaging'
---
# Fairness Evaluation for Diffusion and Flow Models Should Account for the Generation Path: Implications for Clinical Imaging
> 原文: [https://arxiv.org/abs/2611.28077](https://arxiv.org/abs/2611.28077)

arXiv:2611.28077v1 Announce Type: new
Abstract: Medical image generation models are often evaluated using images produced by a single sampling procedure. However, diffusion and flow models can use different numbers of sampling steps, sampling schedules, or numerical solvers without changing their trained parameters. These changes may affect the generated images and the clinical measurements derived from them. We argue that fairness results obtained under one sampling procedure should not be assumed to hold under another, particularly when changes in sampling affect clinical task errors differently across patient groups. Building on previous work on medical image quality, accelerated sampling, generation dynamics, and generative model fairness, we examine why the sampling procedure should be considered part of the evaluated system. We define subgroup differences in clinical task error across sampling procedures and provide a mathematical example showing that two groups can have identical outputs under the exact dynamics and a reference sampler but different errors under an alternative sampler. We also extend this result to stochastic generation under shared noise. An exploratory experiment with an age-conditioned image generation model illustrates how changing the number and timing of sampling steps can alter image-derived measurements, although these differences do not establish clinical unfairness. We therefore argue that fairness evaluation should assess the sampling procedure used in practice and examine intermediate generation states when they help explain differences in clinically relevant errors across patient groups. Analysis code is available here https://github.com/rdharini2001/generation-path-fairness
