---
interest: medium
link: https://arxiv.org/abs/2609.25010
next_step: skim
priority: high
slack_ts: '1790310819.038849'
source: cs.AI - Artificial Intelligence
status: unread
title: Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where
  a No-Persona Baseline Beats Persona-Based Copy Simulation
---
# Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline Beats Persona-Based Copy Simulation
> 原文: [https://arxiv.org/abs/2609.25010](https://arxiv.org/abs/2609.25010)

arXiv:2609.25010v1 Announce Type: new
Abstract: Marketers increasingly use large language models (LLMs) as "synthetic personas" to predict how an audience will react to a piece of copy before it ships, encouraged by evidence that profile-conditioned LLMs mimic human samples. But is that prediction actually valid against real behaviour - and does the persona machinery help? We present a sim-to-real validity study using the Upworthy Research Archive - thousands of headline A/B tests on shared real traffic, with measured click-through - as held-out ground truth. We compare a ten-persona panel, grounded in the real audience's demographics, against a no-persona zero-shot baseline that simply asks the model how likely a typical reader is to click. Two findings stand out. First, ground-truth reliability is the binding constraint: most A/B tests have no statistically distinguishable winner, so validity can only be measured on the reliable subset (n = 399). Second, and counter to the persona-simulation premise, persona conditioning degrades predictive validity: the no-persona baseline ranks variants markedly better (Kendall {\tau} = 0.361, a medium effect; top-1 accuracy 49.2%) than the persona panel ({\tau} = 0.084; top-1 34.6%), with non-overlapping confidence intervals. Asking the model directly taps an accurate population-level prior; forcing it to role-play specific personas injects bias and noise. The result replicates across three independent Upworthy splits, holds in direction on a different-domain news dataset, and is robust to seed, prompt phrasing, and model choice - across three Gemini tiers and a different model family (OpenAI gpt-4.1, significant paired gap). The takeaway: for predicting aggregate engagement, a plain LLM ranker beats persona simulation - synthetic personas are not merely a weak predictor, they are worse than not using them. All numbers regenerate from a public, artifact-first replication package.
