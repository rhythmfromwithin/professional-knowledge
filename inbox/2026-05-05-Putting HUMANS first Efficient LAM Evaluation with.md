---
title: "Putting HUMANS first: Efficient LAM Evaluation with Human Preference Alignment"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.00022
priority: high
status: unread
interest: medium
next_step: skim
---
# Putting HUMANS first: Efficient LAM Evaluation with Human Preference Alignment
> 原文: [https://arxiv.org/abs/2605.00022](https://arxiv.org/abs/2605.00022)

arXiv:2605.00022v1 Announce Type: new
Abstract: The rapid proliferation of large audio models (LAMs) demands efficient approaches for model comparison, yet comprehensive benchmarks are costly. To fill this gap, we investigate whether minimal subsets can reliably evaluate LAMs while reducing costs and data redundancy. Analyzing 10 subset selection methods with 18 audio models across 40 tasks covering major LAM evaluation dimensions, we show that subsets of just 50 examples (0.3% of data) can achieve over 0.93 Pearson correlation with full benchmark scores. To understand how well these scores align with what practitioners ultimately care about, user satisfaction, we collect 776 human preference ratings from realistic voice assistant conversations, finding that both subsets and full benchmark achieve only 0.85 correlation with human. To better predict preferences, we trained regression models on these selected subsets, achieving 0.98 correlation -- outperforming regression models trained on both random subsets and the full benchmark. This demonstrates that in regression modeling, well-curated subsets outpredict the full benchmark, showing quality over quantity. We open-source these regression-weighted subsets as the HUMANS benchmark, an efficient proxy for LAM evaluation that captures both benchmark performance and user preferences.
