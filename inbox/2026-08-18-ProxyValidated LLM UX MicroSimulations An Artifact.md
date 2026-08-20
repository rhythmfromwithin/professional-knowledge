---
interest: medium
link: https://arxiv.org/abs/2608.13563
next_step: skim
priority: low
slack_ts: '1787190023.034949'
source: cs.HC - Human-Computer Interaction
status: unread
title: 'Proxy-Validated LLM UX Micro-Simulations: An Artifact-First Protocol for Early-Stage
  Decision Support'
---
# Proxy-Validated LLM UX Micro-Simulations: An Artifact-First Protocol for Early-Stage Decision Support
> 原文: [https://arxiv.org/abs/2608.13563](https://arxiv.org/abs/2608.13563)

arXiv:2608.13563v1 Announce Type: new
Abstract: Early-stage teams often lack users, time, and budget to run repeated UX studies, yet still need decision-oriented signals to iterate safely. We study an LLM-driven UX micro-simulation pipeline that generates structured customer-experience feedback (walkthrough steps, friction points, micro-survey signals) from versioned prompts, personas, tasks, and UI snapshots. Because public usability datasets with task outcomes are scarce, we validate simulated friction themes using multiple public proxy corpora (app reviews, support tweets, and open-source software issues). We propose a lightweight proxy-validation protocol with two alignment metrics: top-k Jaccard and distributional weighted-Jaccard (W), and compare lexical, TF-IDF, and multilingual embedding baselines across six proxy datasets. Embedding-based alignment yields higher W than lexical baselines on primary app-review and support-tweet proxies (e.g., W=0.128 vs 0.000 on Gojek), while top-k Jaccard is shown to overstate alignment at large k. We ablate four agent strategies (single-pass, best-of-N, hybrid, and a proposed score-then-select judge) across Azure OpenAI deployments and report bootstrap confidence intervals over 8 method-dataset pairs; these intervals reveal that the embedding W point estimate is systematically unstable under resampling at our subsample size. We also provide a failure-mode analysis of grounding and fabrication proxies, with documented calibration caveats and worked examples of outputs flagged as fabricated by an adversarial judge. Our artifact-first pipeline produces reproducible tables and figures from versioned run artifacts, supporting iterative prompt and taxonomy refinement before final paid-model calibration.
