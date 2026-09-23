---
title: "What Does Chain-of-Thought Entropy Measure? A Channel Audit of Scaffolding, Routing, and Content"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.25039
priority: medium
status: unread
interest: medium
next_step: skim
---
# What Does Chain-of-Thought Entropy Measure? A Channel Audit of Scaffolding, Routing, and Content
> 原文: [https://arxiv.org/abs/2609.25039](https://arxiv.org/abs/2609.25039)

arXiv:2609.25039v1 Announce Type: new
Abstract: Entropy over chain-of-thought tokens decides which tokens receive the policy gradient, which get pruned, and whether a run has collapsed, yet each such statistic reads a next-token distribution mixing three choices: whether to emit connective scaffolding, which connective, and what the substantive continuation should be. Designating a scaffold vocabulary subset separates the three, exactly, for entropy, Kullback--Leibler divergence, and the first-order entropy velocity of a softmax policy. We prove the raw and content conventions disagree about which position is the larger fork on an explicit open region, and bound answer diversity by the content channel plus a leakage term a measured witness certifies. Across twenty-three configurations the scaffold side carries up to 41% of the raw high-entropy set; on a matched-tokenizer ladder, coupling changes only at the math-corpus step while the scaffold's entropy share keeps growing through distillation; a closed-form forecast from one channel correlation tracks selection retention over a 54-point range to five points, unfitted. On compression, the content convention beats raw surprisal in every cell; an answer-leakage audit then corrects our own headline control: re-fed chains earn a quarter to a half of their accuracy from restated answers, and once stripped, no token scorer beats a random contiguous block.
