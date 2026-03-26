---
interest: medium
link: https://arxiv.org/abs/2603.22299
next_step: skim
priority: high
slack_ts: '1774493862.754619'
source: cs.LG - Machine Learning
status: unread
title: 'Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer
  Local Information Scores'
---
# Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores
> 原文: [https://arxiv.org/abs/2603.22299](https://arxiv.org/abs/2603.22299)

arXiv:2603.22299v1 Announce Type: new
Abstract: Large language models (LLMs) are often confidently wrong, making reliable uncertainty estimation (UE) essential. Output-based heuristics are cheap but brittle, while probing internal representations is effective yet high-dimensional and hard to transfer.
We propose a compact, per-instance UE method that scores cross-layer agreement patterns in internal representations using a single forward pass.
Across three models, our method matches probing in-distribution, with mean diagonal differences of at most $-1.8$ AUPRC percentage points and $+4.9$ Brier score points. Under cross-dataset transfer, it consistently outperforms probing, achieving off-diagonal gains up to $+2.86$ AUPRC and $+21.02$ Brier points. Under 4-bit weight-only quantization, it remains robust, improving over probing by $+1.94$ AUPRC points and $+5.33$ Brier points on average.
Beyond performance, examining specific layer--layer interactions reveals differences in how disparate models encode uncertainty. Altogether, our UE method offers a lightweight, compact means to capture transferable uncertainty in LLMs.
