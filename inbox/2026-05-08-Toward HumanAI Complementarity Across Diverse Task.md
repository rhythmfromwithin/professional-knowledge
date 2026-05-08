---
title: "Toward Human-AI Complementarity Across Diverse Tasks"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2605.04070
priority: low
status: unread
interest: medium
next_step: skim
---
# Toward Human-AI Complementarity Across Diverse Tasks
> 原文: [https://arxiv.org/abs/2605.04070](https://arxiv.org/abs/2605.04070)

arXiv:2605.04070v1 Announce Type: new
Abstract: Human-AI complementarity, the idea that combining human and AI judgments can outperform either alone, offers a promising pathway toward robust oversight of advanced AI systems. However, whether human-AI complementarity can be achieved on realistic tasks remains an open question. We investigate this through two approaches: hybridization and two AI assistance methods (top-2 assistance and subtask delegation), evaluated on a multi-domain dataset of 1,886 samples spanning knowledge, factuality, long-context reasoning, and deception detection. We find only modest complementarity gains. Baseline hybridization yields just +0.4 percentage points (pp) over AI alone (69.3\% vs 68.9\%), limited both by a small complementarity region (only 8.9\% of items where AI errs but humans do not) and the inability of confidence-based routing to identify it, since the model's confidence is similarly distributed across correct and incorrect predictions. Applied when AI has low confidence, top-2 assistance increases human accuracy from 28.4\% to 38.3\%, surpassing AI alone (37.7\%) -- but primarily because humans adopt correct AI suggestions, not because they successfully override AI errors. These findings suggest that the primary bottleneck is not human task accuracy per se, but the ability to route decisions to humans when it matters and to design assistance methods that enable humans to catch AI mistakes. Our quantitative and qualitative analyses pinpoint where and why each method succeeds or fails, offering concrete targets for future work. We will release our dataset and code upon request to support progress toward more effective human-AI collaboration for AI oversight.
